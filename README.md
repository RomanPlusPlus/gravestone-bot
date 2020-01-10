# Gravestone Bot. A chat bot to speak with the dead

## 0. Intro

Have you ever dreamed of having a conversation with a person from the distant past? Aristotle, William Shakespeare, Benjamin Franklin, Ada Lovelace … any person of your choice. 

The long-term goal of this project is to make it a reality. 

It should work as follows:

1. Collect all the writings of the historical person in one place
2. Give it to Gravestone Bot
3. The Bot will try to reconstruct the person’s mind 
4. If you ask the Bot some question, it should provide an answer that is authentic to the historical person.

At the current stage of development, Gravestone Bot is nothing but a search engine that finds text fragments most relevant to the user’s question. 
We plan to iteratively expand the Bot’s capabilities, to make the conversation more natural and more authentic. 

## 1. How to use it 
### 2. Running the bot with sample texts

Linux:

0. Click "Clone or Download" > "Download ZIP"
1. Unpack the zip
2. cd to the unpacked folder
3. launch it: `python3 launcher.py`
4. Ask some question and press Enter

The bot was tested on Ubuntu 16.04 and Python 3.7.3. 

### 3. Creating a bot with your texts

0. convert your texts to .txt. Currently only English language is supported.  
1. ensure that the encoding is UTF-8
2. Navigate to the Gravestone Bot folder
3. Backup the `input_texts` folder to a safe place 
4. Delete the `input_texts` contents
5. paste your texts into it
6. Launch the bot

The more texts you feed to the bot, the better will be the quality of the answers. 
