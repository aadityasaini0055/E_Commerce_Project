# database/db_connection.py

import mysql.connector
import sys
import os

# Root folder ko path mein add karo taaki config.py mile
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_CONFIG

def get_connection():
    """MySQL se connection banao aur return karo"""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("Database se connect ho gaye!")
        return conn
    except mysql.connector.Error as e:
        print(f"Database connect nahi hua!")
        print(f"Error: {e}")
        print(f"Check karo: MySQL chal raha hai? Password sahi hai?")
        sys.exit(1)
