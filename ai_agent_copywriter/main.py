import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("AI_API_KEY"))
MODEL = "gpt-4o-mini"

def ask(history: list[dict], text: str) -> str:
    """Adds a line to the story, asks the model a question, and remembers the answer"""
    history.append({"role": "user", "content": text})
    response = client.chat.completions.create(
        model=MODEL,
        messages=history,
    )
    answer = response.choices[0].message.content
    history.append({"role": "assistant", "content": answer})
    return answer

SYSTEM_PROMPT = """
You are a professional SMM copywriter. You write in Russian.
Live texts, without stationery. Don't invent facts about the product.
When a user asks to change something - rewrite the LAST post,
and don't create a new one from scratch, and display only the finished text.
"""
BASE_RULES = """You are a professional SMM copywriter. You write in Ukrainian.
Live texts, without stationery. Don't invent facts about the product.
When a user asks to change something - rewrite the LAST post,
and don't create a new one from scratch, and display only the finished text."""

PLATFORMS: dict[str, tuple[str, str]] = {
"1": ("Instagram", """Platform: Instagram.
    A catchy first line, 2-3 short paragraphs, a call to action,
    4-6 emojis, exactly 5 hashtags at the end. Up to 600 characters."""),
"2": ("TikTok", """Platform: TikTok.
    A video script up to 30 seconds: HOOK in the first 2 seconds,
    then 3-4 scenes in the format [Scene 1] ..., at the end - a surprise
    or a call. 3 trending hashtags."""),
"3": ("Telegram", """Platform: Telegram-channel.
    Post-note: first line - title, conversational tone,
    1-3 emojis, no hashtags, up to 700 characters.
    At the end - a question for readers."""),
}

history = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    user_input = input("User:\n").strip()
    print(f"\nCopywriter:\n{ask(history, user_input)}\n")



