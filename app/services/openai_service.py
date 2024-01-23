# app/services/openai_service.py

import openai
from config import OPENAI_API_KEY

class OpenAIService:
    def __init__(self, api_key=OPENAI_API_KEY):
        """
        Initialize the OpenAI service with the given API key.

        :param api_key: OpenAI API key.
        """
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt, model="text-davinci-003", max_tokens=150):
        """
        Generate a response from OpenAI based on the provided prompt.

        :param prompt: The prompt to send to OpenAI.
        :param model: The model to use for the response.
        :param max_tokens: The maximum number of tokens to generate.
        :return: The response from OpenAI.
        """
        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                max_tokens=max_tokens
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error in generating response from OpenAI: {e}")
            return None

    # Additional methods for other OpenAI services can be added here
