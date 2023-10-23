# The begining of the detroit healt project.

from decouple import config
import spacy
import requests
from bs4 import BeautifulSoup
import telebot

BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Load the spaCy NLP model
nlp = spacy.load("en_core_web_sm")


    
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id, text="Hi! I'm Daytwa Health, your personal preventive health assistant. How can I help you today?")

@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(chat_id=message.chat.id, text="You can ask me for personalized health information or advice, and I'll provide you with relevant resources to help you maintain a healthy lifestyle.")

@bot.message_handler(func=lambda message: True)
def process_message(message):
    # Use spaCy to extract relevant keywords from the user's message
    doc = nlp(message.text)
    keywords = [token.text for token in doc if not token.is_stop and token.is_alpha]

    # Search the Verywell Health and Healthline websites for articles and resources related to the user's query
    articles = []
    for keyword in keywords:
        url = f"https://www.verywellhealth.com/search?q={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("div", class_="card-content")
        for result in results:
            title = result.find("h3", class_="card-title").text.strip()
            summary = result.find("p", class_="card-description").text.strip()
            link = result.find("a", class_="card-link")["href"]
            articles.append({"title": title, "summary": summary, "link": link})

        url = f"https://www.healthline.com/search?q={keyword}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        results = soup.find_all("div", class_="search-result")
        for result in results:
            title = result.find("h4", class_="search-result-title").text.strip()
            summary = result.find("p", class_="search-result-excerpt").text.strip()
            link = result.find("a", class_="search-result-link")["href"]
            articles.append({"title": title, "summary": summary, "link": link})

    # Return a list of relevant articles and resources, along with a brief summary of each article
    response = "Here are some articles I found on Verywell Health and Healthline:\n\n"
    for i, article in enumerate(articles):
        response += f"{i+1}. {article['title']}\n{article['summary']}\n{article['link']}\n\n"

    # Allow the user to click on a link to read the full article or ask for more information
    response += "You can click on the links to read the full articles or ask me for more information."

    # Provide personalized health information based on the user's profile and health history, if available
    # TODO: Implement personalized health information based on user profile and health history

    return response

@bot.message_handler(func=lambda message: True)
def echo(message):
    # Process the user's message and generate a response
    response = process_message(message.text)

    # Send the response back to the user
    bot.send_message(chat_id=message.chat.id, text=response)

@bot.message_handler(func=lambda message: True)
def error(message):
    bot.send_message(chat_id=message.chat.id, text="Oops! Something went wrong. Please try again later.")
    
bot.infinity_polling()

