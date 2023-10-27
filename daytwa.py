# The begining of the detroit healt project.

from decouple import config
import telebot
from engine import DaytwaBot
from default_prompts import helper_mgs, start_msg, myprofile_msg, questions_and_answers
from database import Profiler
from utils import extract_question_answer
import random

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
    bot.send_message(chat_id=message.chat.id, text=helper_mgs)

@bot.message_handler(commands=['myprofile'])
def myprofile(message):
    q_n_a = random.choice(questions_and_answers)
    
    sent_msg = bot.send_message(chat_id=message.chat.id, text=myprofile_msg)
    bot.send_message(message.chat.id, q_n_a, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, profiler)

def profiler(message):
    
    # Check if the message is the /myprofile command
    if message.text.startswith('/chat'):
        chat(message)
    else:
        
        # Get the user ID from chat
        user_id = message.from_user.id
        
        # Initialize the profiler for current user
        profiler_db = Profiler(user_id=user_id)
        
        # Get message from chat and format.
        try:
            data = extract_question_answer(message.text)
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

