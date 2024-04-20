import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY = "AIzaSyA3jzmpZumOcoKP410N_WfonXtVfEkoNPU"

genai.configure(api_key=GOOGLE_API_KEY)
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

model = genai.GenerativeModel('gemini-pro')
def translate(start_lang, end_lang, text):
  response = model.generate_content(f'Translate from {start_lang} to {end_lang}, "{text}"')
  return response.text

