# url shortener with python - tinyurl

import pyshorteners  # if it gives error, first run this --> !pip install pyshorteners

long_url = input("Enter the URL to shorten: ")

type_tiny = pyshorteners.Shortener()

short_url = type_tiny.tinyurl.short(long_url)

print(f"The Shortened URL is: {short_url}")
