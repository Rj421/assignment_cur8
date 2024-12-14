import os
from groq import Groq


def call_groq(content):
    client = Groq(
        api_key="your_api_key", #please replace with api key
    )

    prompt = f"""
    Prompt: You are given with a long blog. Your job is to suggest three title based on that.
    Blog: {content}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content