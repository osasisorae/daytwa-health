# The begining of the detroit healt project.

from decouple import config
import telebot
from engine import DaytwaBot
from default_prompts import helper_mgs, start_msg, myprofile_msg

# Initialize Telegram Bot
BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize Health Bot
daytwa_bot = DaytwaBot()

    
@bot.message_handler(commands=['start'])
def start(message):
    sent_msg = bot.send_message(chat_id=message.chat.id, text=start_msg)
    bot.register_next_step_handler(sent_msg, echo)

@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(chat_id=message.chat.id, text=helper_mgs)

@bot.message_handler(commands=['myprofile'])
def myprofile(message):
    sent_msg = bot.send_message(chat_id=message.chat_id, text=myprofile_msg)
    bot.register_next_step_handler(sent_msg, profiler)

def profiler(message):
    """TODO: 
    1. Get user id and info, 
    2. Store info on database
    3. Ask user a question from a random question database
    4. Get user question - answer response from chat, split and store in data base.
    5. Provide a way to exit this block eg (/start, /exit, /thanks)
    """

def echo(message):
    # Process the user's message and generate a response
    response = daytwa_bot.query_vector(message.text)

    # Send the response back to the user
    sent_msg = bot.send_message(chat_id=message.chat.id, text=response)
    bot.register_next_step_handler(sent_msg, echo)

    # Provide personalized health information based on the user's profile and health history, if available
    
    # TODO: Implement personalized health information based on user profile and health history
    
bot.infinity_polling()

