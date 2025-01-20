### Program imports
import datetime as dt
from datetime import date, datetime, timedelta
import os
import sys
import pygame
import os
import gspread
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


## Working directory configuration
"""
This section configures the working directory
    to ensure the script runs in the current file location.
"""
# Get the current working directory (where the script is located)
current_directory = os.path.dirname(os.path.abspath(__file__))
# Change the current working directory
os.chdir(current_directory)
# Now you can perform operations in the current directory
print(f"Current working directory is: {os.getcwd()}")

## Backend import to frontend
"""
This section enables us to import main.py into the main_window.py 
    even though it is not in the same folder
"""

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(
            __file__), '..'
            )
        )
    )

## A Music file configuration
def initialize_audio():
    pygame.mixer.init()
    music_path = "Left_Sock_Paradise.mp3"
    pygame.mixer.music.load(music_path)

## Google Sheets database configuration
# Path to the service account key JSON file (update this path)
SERVICE_ACCOUNT_FILE = "databaseinf-d7ee9d31da7b.json"
# Define scopes for Google APIs
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
# Authenticate using the service account
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# Google Drive and Sheets API clients
drive_service = build("drive", "v3", credentials=creds)
gc = gspread.authorize(creds)