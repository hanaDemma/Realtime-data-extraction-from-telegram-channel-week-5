import nest_asyncio
import os
import csv
import re
import asyncio
from telethon import TelegramClient, events
from dotenv import load_dotenv

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv('.env')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')

# Initialize the Telegram client
client = TelegramClient('scraping_session', api_id, api_hash)

# Define directories for saving data
csv_file = 'telegram_data.csv'
image_folder = 'telegram_images'
document_folder = 'telegram_documents'
os.makedirs(image_folder, exist_ok=True)  # Create folder if it doesn't exist
os.makedirs(document_folder, exist_ok=True)