### Task 1- Data Ingestion and  Data Preprocessing

## Project Overview

# 1. Repository Setup

- Create a GitHub repository with a dedicated branch: feature/task-1.
- Committ progress at least three times a day with descriptive messages.

#  Data Ingestion and  Data Preprocessing
This repository contains code Set up a data ingestion system to fetch messages from multiple  Ethiopian-based Telegram e-commerce channels.

## Steps:
- Identify and connect to relevant Telegram channels using a custom scraper.
- Implement a message ingestion system to collect text, images, and documents as they are posted in real time.
- Preprocess text data by tokenizing, normalizing, and handling Amharic-specific linguistic features.
- Clean and structure the data into a unified format, separating metadata from message content.
- Store preprocessed data in a structured format for further analysis


# How to Use
- Clone the Repository:
git clone https://github.com/hanaDemma/Realtime-data-extraction-from-telegram-channel-week-5.git

- Switch to Task-1 Branch:

git checkout feature/task-1

- Run the Notebook:

    - Install dependencies:

        pip install -r requirements.txt

    - Open and execute the Jupyter notebook.

# Key Files
- telegram_scrapping.ipynb: Contains data scaping, ingestion 
- requirements.txt: List of required Python libraries.
- README.md: Project documentation.

# Technologies Used
- Libraries:
    - pandas, telethon, dotenv,asyncio

# Task-2 Label a Subset of Dataset in CoNLL Format
The objective of this phase is  labeling a portion of the provided dataset in the CoNLL format and save the text in a plain text file in the CoNLL format

# Development Instructions
- Create a feature/task-2 Branch for development.
- Commit progress regularly with clear and detailed commit messages.
- Merge updates into the main branch via a Pull Request (PR).