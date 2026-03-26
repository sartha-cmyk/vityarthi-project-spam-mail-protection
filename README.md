# Spam-Mail-Protection

## Project Overview

The Spam Mail Protection System is a simple python-based application that detects spam emails using keyword analysis and scoring techniques. This project identifies whether an email message is spam, suspicious, or not spam based on predefined spam-related keywords such as free, win, money, offer, prize or urgent etc.

The system is built using basic python programming concepts. It demonstrates how real-world problems like spam detection can be solved using programming and coding.

This project is developed as part of the VITyarthi BYOP assignment to solve a real-world cybersecurity problem using Python and Machine Learning.

## Problem Statement

Spam email and messages are a common issue in digital communication.
Users frequently receive emails containing fake offers, lottery messages, urgent financial requests, and suspicious links that may lead to fraud or data theft.

The goal of this project is to create a simple and easy-to-use system that can detect spam emails and help users identify fruadulent messages using basic Python knowledge.

## Features
1. Detects spam emails using keyword-based scoring
2. Classifies emails as: spam, suspicious or not spam
3. Menu-driven program
4. Checks single email message, multiple emails from file, adds new spam keywords, saves results to file and displays spam word list.

## Installation and Setup

#### Step 1: Install Python
Download and install Python from: https://www.python.org/downloads/

#### Step 2: Download the Project
Clone the repository from GitHub:
https://github.com/sartha-cmyk/Spam-Mail-Protection.git

Go to project folder:cd spam-mail-protection

#### Step 3: Run the Program
python spam_mail_protection.py 
The program will start and show the menu.

## How to Use
After running the program, you will see the menu:

Spam Mail Protection System

1. Check Single Email
2. Check Emails from File
3. Add Spam Word
4. Save Email Result
5. Show Spam Words
6. Exit

### Option 1: Check Single Email
Enter any email message and the system will classify it.

Example:
Enter Email Message: Congratulations you win the lottery !!!!!

Output:
Spam Score: 2
Result: SUSPICIOUS

### Option 2: Check Emails from File
The program reads emails from emails.txt and detects spam automatically.

Example emails.txt: 
Congratulations you win free money
Meeting tomorrow at 10am
Limited offer claim prize
Project discussion

Output:
SPAM
NOT SPAM
SPAM
NOT SPAM

### Option 3: Add Spam Word
User can add new spam keywords.

Example:
Enter new spam word: bitcoin

The system will now detect emails containing 'bitcoin' as spam.

### Option 4: Save Email Result
Stores email classification in results.txt.

Example: Hello free offer

Saved in file SPAM

### Option 5: Show Spam Words
Displays all spam keywords used in the system.

### Option 6: Exit
Closes the program.


