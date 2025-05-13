import requests
from bs4 import BeautifulSoup

def get_meaning(word):
    url = f"https://www.dictionary.com/browse/{word}"
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        meaning = soup.find("span", class_="one-click-content")
        if meaning:
            return meaning.text.strip()
        else:
            return "Meaning not found."
    except:
        return "Error fetching meaning."