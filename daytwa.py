# The begining of the detroit healt project.

from decouple import config

import telebot

BOT_TOKEN = config('BOT_TOKEN')
print(BOT_TOKEN)
bot = telebot.TeleBot(BOT_TOKEN)


    
@bot.message_handler(commands=['start'])
def start(message):
    print('I got here')
    bot.send_message(chat_id=message.chat.id, text="Hi! I'm a health chatbot. How can I help you today?")

@bot.message_handler(commands=['help'])
def helper(message):
    print('now here')
    bot.send_message(chat_id=message.chat.id, text="You can ask me for health information or advice, and I'll do my best to provide you with relevant resources.")

@bot.message_handler(func=lambda message: True)
def process_message(message):
    print('Maybe here')
    # Use NLP and machine learning algorithms to understand the user's intent and extract relevant keywords
    # Search the Verywell Health and Healthline websites for articles and resources related to the user's query
    # Return a list of relevant articles and resources, along with a brief summary of each article
    # Allow the user to click on a link to read the full article or ask for more information
    # Provide personalized health information based on the user's profile and health history, if available
    return "Here are some articles I found on Verywell Health and Healthline: ..."

@bot.message_handler(func=lambda message: True)
def echo(message):
    print('definitely here')
    # Process the user's message and generate a response
    response = process_message(message.text)

    # Send the response back to the user
    bot.send_message(chat_id=message.chat.id, text=response)

@bot.message_handler(func=lambda message: True)
def error(message):
    print('what an error')
    bot.send_message(chat_id=message.chat.id, text="Oops! Something went wrong. Please try again later.")
    
bot.infinity_polling()

