import collections
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import json

orelsan = 1286
grand_corps_malade = 1712


def extract_lyrics(url):
    print(f"Extracting lyrics {url}...")
    r = requests.get(url)

    if r.status_code != 200:
        print("Error")
        return []

    soup = BeautifulSoup(r.content, 'html.parser')
    lyrics = soup.find("div", id="lyrics-root")
    if not lyrics:
        return extract_lyrics(url)

    all_words = []
    for sentence in lyrics.stripped_strings:
        sentence_words = [word.strip(",").strip(".").lower() for word in sentence.split() if "[" not in word and "]" not in word and "lyrics" not in word]
        all_words.extend(sentence_words)

    return all_words


def get_all_urls():
    page_nb = 1
    links= []
    while True:
        r = requests.get(f"https://genius.com/api/artists/1286/songs?page={page_nb}&sort=popularity")

        if r.status_code == 200:
            print(f"Page {page_nb}")
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            
            links.extend([song.get("url") for song in songs])

            page_nb += 1

            if not next_page:
                print("End of pages")
                break

    print(f"Found {len(links)} links")
    return links


def get_all_words():
    urls = get_all_urls()
    words = []
    for url in urls:
        lyrics = extract_lyrics(url)
        words.extend(lyrics)
    
    with open("data-orelsan.json", "w") as f:
        json.dump(words, f, indent=4)

    # with open("data.json", "w") as f:
    #     words = json.load(f)

    counter = collections.Counter([w for w in words if len(w) > 10])
    pprint(counter.most_common(15))

get_all_words()