# Tmux2TelegramMonitor
A real-time monitoring tool that tracks tmux session changes and sends alerts to Telegram. Ideal for system administrators and developers, it ensures immediate updates on session activities, combining tmux's efficiency with Telegram's instant messaging.

## Features

- Real-time monitoring of `tmux` sessions.
- Instant alerts to a Telegram chat upon session changes.
- Easy to set up and use in any server or development environment.


## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software:

- Python 3
- `tmux`: https://github.com/tmux/tmux/wiki
- A Telegram bot token and chat ID:
  - Telegram Bot Tutorial: https://core.telegram.org/bots/tutorial
  - How to get chatID: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id

## Installing

A step-by-step guide to get a development env running:

**Clone the repository:**
```
git clone https://github.com/smeshny/Tmux2TelegramMonitor.git
```
**Navigate to the project directory:**
```
cd Tmux2TelegramMonitor
```
**Install required dependencies:**
```
pip install -r requirements.txt
```
**Configure your **Telegram bot token** and **chat ID** in the `send_to_telegram.py`:**
```
bot = Bot(token='your_token')
chat_id = '-your_chat_id'
```
### tmux session
**Start the tmux Process:**
Open your terminal and start tmux by typing `tmux`.

Launch the process you wish to monitor.

**Create a New tmux Window:**
To create a new window in tmux, you can press `Ctrl+b+c`. This will create a new window within the same tmux session.

**Obtain the Window Identifier you want to monitoring:**
To get the identifier of the window that you need to monitor, you can use the command `tmux list-windows`. This will list all windows in the current session along with their identifiers.
If you want to get the identifier of a specific pane within a window, you can use `tmux list-panes -a`, which shows the identifiers for all panes in all windows and sessions. 

The identifier will be in the format **%<number>, like %0 or %1.**

**Configure your `pane_id` for monitoring in `send_to_telegram.py`:**
```
pane_id = "%0"
```

**Start monitoring script:**
```
chmod +x tmux_to_telegram_loop.sh
```

```
./tmux_to_telegram_loop.sh
```
