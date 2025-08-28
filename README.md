# automakeaccgog

This repository demonstrates a very simple AI implemented as a perceptron
that learns the OR logic gate.

## Running the example

Run the unit tests to train the perceptron and verify its predictions:

```bash
python -m unittest
```

## Command-line chat

A small script is included to chat with OpenAI's API from the command line.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your API key in an environment variable `OPENAI_API_KEY`.
3. Start the chat:
   ```bash
   python chat.py
   ```
   Type `exit` or `quit` to stop.

## Minecraft AFK bot

`minecraft_afk_bot.js` keeps a Minecraft account online by connecting to a
server and automatically reconnecting if the connection drops. It uses the
[mineflayer](https://github.com/PrismarineJS/mineflayer) library.

### Usage

1. Install dependencies:
   ```bash
   npm install
   ```
2. Set your Minecraft credentials (if using an offline account, only the
   username is required):
   - **Windows CMD**
     ```cmd
     set MC_USERNAME=YourName
     set MC_PASSWORD=YourPassword   # optional
     set MC_AUTH=microsoft          # optional, default is offline
     ```
   - **bash/zsh**
     ```bash
     export MC_USERNAME=YourName
     export MC_PASSWORD=YourPassword  # optional
     export MC_AUTH=microsoft         # optional, default is offline
     ```
3. Start the bot:
   ```bash
   node minecraft_afk_bot.js
   ```

The script connects to `ramadhansipaling.aternos.me:48224` by default and will
reconnect every 10 seconds if disconnected. Please ensure that running bots is
allowed on the target server.
