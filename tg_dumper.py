from asyncio import sleep
import asyncio

from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

# Use your own values from my.telegram.org
api_id = '333333'
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# The name of the group from which you want to download messages
group_name = 'lixiangautorussia'
category_hashtag = 'Общая'

client = TelegramClient('session_name', api_id, api_hash)


# Function to convert a message object to HTML, formatted as Bootstrap cards
def message_to_html(message, index):
    # Format the date as dd.mm.yyyy
    formatted_date = message.date.strftime('%d.%m.%Y')

    return f"""
<div class="card mb-3">
  <div class="card-header">
    Category: {message.peer_id}, message #{index} (ID: {message.id}) - {formatted_date}
  </div>
  <div class="card-body">
    <blockquote class="blockquote mb-0">
      <p>{message.message}</p>
    </blockquote>
  </div>
</div>
"""

async def main_hashtag():
    # Connect to the client
    await client.start()

    # Get the target group entity
    target_group = await client.get_entity(group_name)

    # Open the HTML file and write the header part of the HTML template
    with open(f'telegram_group_messages_{category_hashtag}.html', 'w', encoding='utf-8') as file:
        file.write("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Telegram Group Chat History</title>
    <!-- Include Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container mt-5">
    """)

    # Initialize the offset_id
    offset_id = 0
    message_index = 1

    # Loop to fetch messages from the beginning to the end
    while True:
        # Fetch a batch of messages starting with the oldest (offset_id is 0 initially)
        messages = await client.get_messages(target_group, offset_id=offset_id, limit=100, reverse=True)
        if not messages:
            print("No more messages left")
            break  # No more messages left

        print("Fetched ", len(messages), "messages")

        # Process messages in reverse order to start from the beginning
        for message in reversed(messages):
            try:
                # Only process if the message has the category hashtag or pattern
                # if message.message in message.message: # and category_hashtag
                # Convert the message to HTML format with Bootstrap styling
                message_html = message_to_html(message, message_index)

                print(message_index, message.message)

                # Append the message to the HTML file
                with open(f'telegram_group_messages_{category_hashtag}.html', 'a', encoding='utf-8') as file:
                    file.write(message_html + '\n')

                # Increment the message index for the next message
                message_index += 1
            except:
                print("Message handling error, going next...")

        # Update the offset_id to the id of the last message in the batch
        offset_id = messages[-1].id

        # Sleep for some time to avoid hitting the API limits
        print("Delay 10 secs...")
        await asyncio.sleep(10)

    # Write the footer part of the HTML template and close the file
    with open(f'telegram_group_messages_{category_hashtag}.html', 'a', encoding='utf-8') as file:
        file.write("""
    </div>
</body>
</html>
    """)

    print("Finished. Messages saved to HTML file.")

    # Disconnect the client when done
    await client.disconnect()


# Run the main function
loop = asyncio.get_event_loop()
loop.run_until_complete(main_hashtag())
