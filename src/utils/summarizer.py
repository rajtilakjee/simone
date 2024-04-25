from __future__ import annotations

import json

import requests


class Summarizer:
    def __init__(self, api_key, transcription_filename):
        self.api_key = api_key
        self.transcription_filename = transcription_filename

    def generate_summary(self):
        with open(self.transcription_filename, "r") as file:
            content = file.read()

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            data=json.dumps(
                {
                    "model": "google/gemma-7b-it:free",
                    "messages": [
                        {
                            "role": "system",
                            "content": "Give top 3 important keywords for the provided content.",
                        },
                        {"role": "user", "content": content},
                    ],
                },
            ),
        )

        response_text = response.text
        response_dict = json.loads(response_text)
        summary = response_dict["choices"][0]["message"]["content"]
        return summary
