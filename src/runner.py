#!/bin/env python3
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# =====================
# models
# =====================
# text-ada-001
# text-babbage-001
# text-curie-001
# text-davinci-003
# =====================

response = openai.Completion.create(
  model="text-ada-001",
  prompt="Brainstorm some ideas combining VR and fitness:",
  temperature=0,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
)

print(response)