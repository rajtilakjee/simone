from __future__ import annotations

import json

import requests


class Blogger:
    def __init__(self, api_key, transcription_filename, output_filename):
        self.api_key = api_key
        self.transcription_filename = transcription_filename
        self.output_filename = output_filename

    def generate_blogpost(self):
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
                            "content": "Generate a blogpost for the provided content.",
                        },
                        {"role": "user", "content": content},
                    ],
                },
            ),
        )

        response_text = response.text
        response_dict = json.loads(response_text)
        blogpost = response_dict["choices"][0]["message"]["content"]

        with open(self.output_filename, "w") as file:
            file.write(blogpost)
