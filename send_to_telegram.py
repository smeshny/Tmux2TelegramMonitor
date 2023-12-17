import asyncio
from telegram import Bot
from telegram.error import BadRequest, RetryAfter
import subprocess
import os
import textwrap
import time
import difflib

bot = Bot(token='your_token')
chat_id = '-your_chat_id'

pane_id = "%0"

previous_file = 'previous_tmux_session.txt'
current_file = 'current_tmux_session.txt'

def capture_tmux_session():
    return subprocess.check_output(["tmux", "capture-pane", "-p", "-t", pane_id])

def save_current_session(content):
    with open(current_file, 'w') as file:
        file.write(content)

def get_diff_content(previous_content, current_content):
    previous_lines = previous_content.splitlines()
    current_lines = current_content.splitlines()
    diff = difflib.unified_diff(previous_lines, current_lines, lineterm='')

    # Extract new lines only
    new_lines = [line[1:] for line in diff if line.startswith('+') and not line.startswith('+++')]
    return '\n'.join(new_lines)

async def send_to_telegram(content):
    chunks = textwrap.wrap(content, 2000)
    for chunk in chunks:
        try:
            if chunk.strip():
                await bot.send_message(chat_id=chat_id, text=chunk)
        except BadRequest as e:
            print("Error sending message:", e)
        except RetryAfter as e:  # Correctly reference RetryAfter
            print(f"Flood limit exceeded. Waiting for {e.retry_after} seconds.")
            await asyncio.sleep(e.retry_after)  # Wait for the specified time
            await bot.send_message(chat_id=chat_id, text=chunk)  # Retry sending the message


if __name__ == "__main__":
    loop = asyncio.get_event_loop()  
    while True:
        tmux_content = capture_tmux_session().decode('utf-8')
        save_current_session(tmux_content)

        if os.path.exists(previous_file):
            with open(previous_file, 'r') as file:
                previous_content = file.read()

            new_content = get_diff_content(previous_content, tmux_content)
            if new_content:
                loop.run_until_complete(send_to_telegram(new_content))

        # Rename current session file to previous for next comparison
        os.rename(current_file, previous_file)

        time.sleep(1)  # Check every second