# AI Telegram Bot

This project is a Telegram bot that utilizes GPT model to interact with users via text and voice messages. It allows users to have conversations with the AI, and it can also recognize and transcribe voice messages.

## Features

- **Text Conversations**: Users can chat with the AI using text messages.
- **Voice Recognition**: Users can send voice messages, which the bot converts to text and processes.
- **Conversation History**: The bot maintains a conversation history for context in discussions.
- **Proxy Support**: Optionally connect through a proxy for API requests.
- **Configurable Settings**: Customize settings through environment variables.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Project Structure

- **`src/main.py`**: The entry point of the bot.
- **`tests/`**: Directory for tests.

## Installation

### Docker

You can run the bot using Docker. Follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/ai_telegram_bot.git
   cd ai_telegram_bot
   ```

2. **Build the Docker image**:

   ```bash
   docker build -t ai_telegram_bot .
   ```

3. **Create a `.env` file in the root directory with the following variables**:

   ```
   aibot_token=YOUR_TELEGRAM_BOT_TOKEN
   aibot_admin_id=YOUR_ADMIN_ID
   aibot_proxy=YOUR_PROXY (optional)
   aibot_api_key=YOUR_API_KEY (optional)
   ```

4. **Run the Docker container**:

   ```bash
   docker run --env-file .env ai_telegram_bot
   ```

### Docke compose

You can run the bot using Docker compose. Follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/ai_telegram_bot.git
   cd ai_telegram_bot
   ```

2. **Create a `.env` file in the root directory with the following variables**:

   ```
   aibot_token=YOUR_TELEGRAM_BOT_TOKEN
   aibot_admin_id=YOUR_ADMIN_ID
   aibot_proxy=YOUR_PROXY (optional)
   aibot_api_key=YOUR_API_KEY (optional)
   ```

3. **Run the Docker container**:

   ```bash
   docker compose up
   ```

### Local Installation (Optional)

1. Install dependencies using [PDM](https://pdm-project.org/en/latest/#installation):

   ```bash
   pdm install
   ```

2. Run the bot:

   ```bash
   pdm run python src/main.py
   ```

## Usage

- Start a chat with the bot on Telegram.
- Send text messages to receive responses from the AI.
- Send voice messages for the bot to transcribe and respond.

## Contributing

Contributions are welcome! Please create a pull request for any changes you'd like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
