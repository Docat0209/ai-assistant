"""LLM"""

__all__ = ("LLM",)

from openai import OpenAI


class LLM:
    """LLM Functions"""

    def __init__(self) -> None:
        pass

    def chat(self, content: str) -> str:
        """Get LLM respone"""
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": content},
            ],
        )

        return response.choices[0].message.content
