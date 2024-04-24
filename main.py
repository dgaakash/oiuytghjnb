from pyrogram import Client
import asyncio
import os

# Your API credentials
api_id = os.getenv("APP_ID")
api_hash = os.getenv("API_HASH")

# Your string session
string_session = os.getenv("STRING")

# List of messages
messages = [
    "/scrime", "/sexplore", "/shunt", "/sfight", "/propose",
    "completed a loop sleeping for 10 Minutes...."
]

# Create a Pyrogram Client with the string session
app = Client("User-bot",
             session_string=string_session,
             api_id=api_id,
             api_hash=api_hash)


# Function to send messages
async def send_messages():
  for message in messages:
    chat_id = -1002043039311
    await app.send_message(chat_id, message)
    await asyncio.sleep(1)  # Adjust this delay if needed


# Main function
async def main():
  while True:
    await send_messages()
    print("Messages sent. Waiting for 10 minutes...")
    await asyncio.sleep(600)  # Sleep for 10 minutes


# Start the client
async def start_client():
  await app.start()
  await main()


# Run the client
asyncio.run(start_client())
