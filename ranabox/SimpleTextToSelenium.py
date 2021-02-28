import openai
import random
from os import path

from openai.api_resources.engine import Engine

openai.api_key = "" # find your own key by joining the waiting list
                    # at https://beta.openai.com/?demo=1

from gpt import GPT
from gpt import Example

gpt = GPT(engine = "davinci",
            temperature= 0.7,
            max_tokens=258)

gpt.add_example(Example('This was my space and I chose to write this. Nothing else, but exactly this.'))