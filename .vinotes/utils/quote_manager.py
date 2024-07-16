# purpose: when the function get_quote is called, return a {quote, author}
# command: none

import json, random

quotes = None

with open(".vinotes/utils/quotes.json", "r") as data:
    quotes = json.load(data)

def get_quote():
    quote_rand_index = random.randint(0, len(quotes)-1)
    return quotes [quote_rand_index]
