import os
from openai import OpenAI

def main() -> None:
    """Simple command-line chat using OpenAI's API."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Set the OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)
    print("Type 'exit' or 'quit' to stop.")
    while True:
        user = input("You: ").strip()
        if user.lower() in {"exit", "quit"}:
            break
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user}],
        )
        print("AI:", response.choices[0].message.content)

if __name__ == "__main__":
    main()
