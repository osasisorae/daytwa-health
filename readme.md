# Daytwa Health Project: A Retrieval Augmented Generation Chat Agent

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
  - [Creating Your Health Profile](#creating-your-health-profile)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)
- [Environment Variables](#environment-variables)

## Introduction
The Daytwa Health Project is a Telegram-based chatbot designed to provide information and guidance on preventive health. It can help users create their health profiles, answer health-related questions, and provide personalized health advice.

## Features
- **Interactive Chatbot**: Engage in conversations with the chatbot via the Telegram messaging platform.
- **Personalized Health Advice**: Receive personalized health information based on your health profile and responses.
- **Web Scraping**: Gather health-related information from various online sources to provide accurate advice.

## Getting Started
### Prerequisites
Before you begin, ensure you have the following prerequisites:
- [Python](https://www.python.org/) 3.x
- [Decouple](https://pypi.org/project/python-decouple/)
- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)

### Installation
1. Clone this repository:
   ```shell
   git clone https://github.com/yourusername/daytwa-health.git
   ```

2. Install required Python dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Usage

### Commands
- `/chat`: Start a conversation with the chatbot.
- `/start`: Get instructions and assistance from the chatbot.
- `/myprofile`: Initiate the process of creating your health profile.

### Creating Your Health Profile
1. Start a conversation with the chatbot using the `/myprofile` command.
2. Follow the instructions to format your health profile by asking health-related questions and providing detailed answers.

## Architecture
The project's architecture includes the following components:

- Telegram Bot Interface
- DaytwaBot (Engine)
- Environment Variables
- Apify Integration
- Document Store
- Vectorstore Index
- External Services

For a detailed architectural overview, refer to the Architecture document.

## Contributing
We welcome contributions to the project. If you'd like to contribute, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the MIT License.

## Environment Variables
Make sure to set the following environment variables in your `.env` file:

- `BOT_TOKEN`: Your Telegram Bot token.
- `OPENAI_API_KEY`: Your OpenAI API key.
- `APIFY_API_TOKEN`: Your Apify API token.