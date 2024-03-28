import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import json

import time, os, sys


f = open("gemini_ai.json", 'r')
data = json.load(f)

api = data['api_gemini_ai']
model = data['model']

print(f"Loading API gemini ai: {api}")
try:
  genai.configure(api_key=api)
  model_tam = genai.GenerativeModel("gemini-pro")
  report = model_tam.generate_content("hello")
except:
  print(
      "Your API is invalid or your internet is not working, PLEASE CHECK AND TRY AGAIN!!!  "
  )
  time.sleep(10)
  sys.exit()

print(f"Setup the model Gemini AI: {model}")
if model == "gemini-pro-vision-latest":
  print(f"We not support this model: {model}")
  print("HINT:")
  print('''
  *We support model:
    gemini-1.0-pro
    gemini-1.0-pro-001
    gemini-1.0-pro-latest
    gemini-pro
  *We not support model:
    gemini-1.0-pro-vision-latest
    gemini-pro-vision
  ''')
  time.sleep(10)
  sys.exit()
elif model == "gemini-pro-vision":
  print(f"We not support this model: {model}")
  print("HINT:")
  print('''
  *We support model:
    gemini-1.0-pro
    gemini-1.0-pro-001
    gemini-1.0-pro-latest
    gemini-pro
  *We not support model:
    gemini-1.0-pro-vision-latest
    gemini-pro-vision
  ''')
  time.sleep(10)
  sys.exit()
try:
  model = genai.GenerativeModel(model)
  report = model.generate_content("hello?")
except:
  print("Please check your model name and try again!!")
  print("HINT:")
  print('''
  *We support model:
    gemini-1.0-pro
    gemini-1.0-pro-001
    gemini-1.0-pro-latest
    gemini-pro
  *We not support model:
    gemini-1.0-pro-vision-latest
    gemini-pro-vision
  ''')
  time.sleep(10)
  sys.exit()

print("Done! Your Python Gemini AI is ready. Wait 5 second to start")

time.sleep(5)

os.system("cls")

print("Type bye to exit")
print("-------------------------------------------------------")
while True:
  prompt = input("You: ")
  if prompt == "bye":
    print("Good bye!")
    time.sleep(5)
    break
  #chat_bot = to_markdown(model.generate_content(prompt).text)
  chat_bot = model.generate_content(prompt).text
  print("Gemini AI: ", chat_bot)
  print("-------------------------------------------------------")
