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
