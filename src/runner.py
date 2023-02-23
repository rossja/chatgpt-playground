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
prompt = "complete this sentence: \"This is...\""
#prompt = "brainstorm 5 slogans for an airport."
temperature = 0
max_tokens = 150
top_p = 1
frequency_penalty = 1
presence_penalty = 1

ada_response = openai.Completion.create(
  model="text-ada-001",
  prompt=prompt,
  temperature=temperature,
  max_tokens=max_tokens,
  top_p=top_p,
  frequency_penalty=frequency_penalty,
  presence_penalty=presence_penalty
)
print("ada:%s\n\n" % ada_response.choices[0].text)

babbage_response = openai.Completion.create(
  model="text-babbage-001",
  prompt=prompt,
  temperature=temperature,
  max_tokens=max_tokens,
  top_p=top_p,
  frequency_penalty=frequency_penalty,
  presence_penalty=presence_penalty
)
print("babbage:%s\n\n" % babbage_response.choices[0].text)

curie_response = openai.Completion.create(
  model="text-curie-001",
  prompt=prompt,
  temperature=temperature,
  max_tokens=max_tokens,
  top_p=top_p,
  frequency_penalty=frequency_penalty,
  presence_penalty=presence_penalty
)
print("curie:%s\n\n" % curie_response.choices[0].text)

davinci_response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=temperature,
  max_tokens=max_tokens,
  top_p=top_p,
  frequency_penalty=frequency_penalty,
  presence_penalty=presence_penalty
)
print("davinci:%s\n\n" % davinci_response.choices[0].text)