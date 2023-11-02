# The begining of the detroit healt project.

from decouple import config
import telebot
from engine import DaytwaBot, CVAnalytics
from default_prompts import helper_mgs, start_msg, myprofile_msg, questions_and_answers, healt_equity_intro
from database import Profiler, Vectorizer
import random
from utils import Utilities
import time

# Initialize the utilities helper
utilities = Utilities()

# Initialize the cv analytics
cv_analytics = CVAnalytics()

# Initialize Telegram Bot
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize Health Bot
daytwa_bot = DaytwaBot()

    
@bot.message_handler(commands=['chat'])
def chat(message):
    sent_msg = bot.send_message(chat_id=message.chat.id, text=start_msg)
    bot.register_next_step_handler(sent_msg, echo)

@bot.message_handler(commands=['start'])
def start(message):
    if message.text.startswith('/train'):
        train(message)
    bot.send_message(chat_id=message.chat.id, text=helper_mgs)
    
@bot.message_handler(commands=['apply'])
def health_equity_apply(message):
    bot.register_next_step_handler(
        bot.send_message(
            chat_id=message.chat.id, 
            text=healt_equity_intro, 
            parse_mode="Markdown"
        ),
        health_equity_applicants
    )
    
def health_equity_applicants(message):
   
    try:
        # Check if the document is a PDF
        if message.document.mime_type == 'application/pdf':
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            user_id = message.from_user.id  

            # Specify a path to save the PDF locally
            local_path = f'resumes/file_{user_id}.pdf'

            # Save the downloaded file to your local storage
            with open(local_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.reply_to(message, "PDF file successfully received and stored.")
            time.sleep(0.5)
            bot.send_message(chat_id=message.chat.id, text="We're having a look at your CV, Please hold.", parse_mode="Markdown")
            summary = cv_analytics.summarize(local_path) # Check applicants eligbility.
            bot.send_message(chat_id=message.chat.id, text=".", parse_mode="Markdown")
            # Store the summary as a vetor.
            vectorizer = Vectorizer(user_id=user_id, data_type='summaries') # Initialize vectorizer
            bot.send_message(chat_id=message.chat.id, text="..", parse_mode="Markdown")
            vectorizer.store_cv_summary(summary=summary) # Store embedded summary
            bot.send_message(chat_id=message.chat.id, text="...", parse_mode="Markdown")
            # Delete the pdf file.
            utilities.delete_cv_file(local_path)
            
            bot.register_next_step_handler(
                bot.send_message(
                    chat_id=message.chat.id,
                    text=summary,
                    parse_mode="Markdown"
                    ),
                start
            )
        else:
            bot.reply_to(message, "Please send a PDF document.")
    except Exception as e:
        print(e)
        bot.reply_to(message, "An error occurred while processing the document.")

@bot.message_handler(commands=['train'])
def train(message):
    # TODO: Check the database to see if its up to 3 months
    # Start the training process.
    bot.register_next_step_handler(
        bot.send_message(
            chat_id=message.chat.id,
            text="We're curating training materials, check back soon.",
            parse_mode="Markdown"
        ),
        start
    )

@bot.message_handler(commands=['myprofile'])
def myprofile(message):
    q_n_a = random.choice(questions_and_answers)
    
    sent_msg = bot.send_message(chat_id=message.chat.id, text=myprofile_msg)
    bot.send_message(message.chat.id, q_n_a, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, profiler)

def profiler(message):
    
    # Check if the message is the /chat command
    if message.text.startswith('/chat'):
        chat(message)
    # Check if the message is the /start command
    elif message.text.startswith('/start'):
        start(message)
    else:
        
        # Get the user ID from chat
        user_id = message.from_user.id
        
        # Initialize the profiler for current user
        profiler_db = Profiler(user_id=user_id)
        
        # Get message from chat and format.
        try:
            data = utilities.extract_question_answer(message.text)
        except ValueError:
            # send error message to chat.
            msg = bot.send_message(chat_id=message.chat_id, text="Invalid format. Please use the format 'Question? - Answer'.")
            bot.register_next_step_handler(msg, profiler)
        
        # Store the user profile on the vector database.
        profiler_db.store_profile(data=data)        

        """TODO: 
        6. Close the Profiler client
        """

def echo(message):
    # Get the user ID from chat
    user_id = message.from_user.id

    # Check if the message is the /myprofile command
    if message.text.startswith('/myprofile'):
        myprofile(message)
    # Check if the message is the /start command
    elif message.text.startswith('/start'):
        start(message)
    # Check if the message is the /start command
    elif message.text.startswith('/chat'):
        chat(message)
    else:
        # Initialize the profiler for the current user
        profiler_db = Profiler(user_id=user_id)

        # Check the database to augment user question
        question, answer = profiler_db.retrieve_profile(message.text)
        # Provide personalized health information based on the user's profile and health history, if available
        prompt = f"Heres a question: {message.text}. Here's some info about me: {answer}"
        
        print("Question:", question)
        print("Answer:", answer)
        print("Propmt:", f"Heres a question: {message.text}. Here's some info about me: {answer}")

        # Process the user's message and generate a response
        response = daytwa_bot.query_vector(prompt)

        # # Send the response back to the user
        sent_msg = bot.send_message(chat_id=message.chat.id, text=response)
        bot.register_next_step_handler(sent_msg, echo)


bot.infinity_polling()

