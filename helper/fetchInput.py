import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_input(day, year = 2021):
    client_secret = os.getenv("ADVENT_SESSION")

    url = "https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input"

    cookies = {"session": client_secret}

    response = requests.get(url, cookies=cookies)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        data = response.text  # The content of the response
        return data
    else:
        print(f"Request failed with status code {response.status_code}")

