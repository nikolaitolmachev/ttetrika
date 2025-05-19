import requests
import re
import csv
import time
from bs4 import BeautifulSoup


BASE_URL = 'https://ru.wikipedia.org/'
URL = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

def is_russian_letter(char: str) -> bool:
    return bool(re.match(r'[А-Яа-я]', char))

def scrape() -> dict:
    result = {}

    current_url = URL

    while True:
        print(current_url)

        resp = requests.get(current_url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        letters = soup.select('div.mw-category.mw-category-columns > div.mw-category-group')
        for letter in letters:
            current_letter = letter.select('h3')[0].text.strip()
            print(f'Current letter: {current_letter}')

            if not is_russian_letter(current_letter):
                print('STOP')
                return result

            print('Doing...')
            if result.get(current_letter) is None:
                result[current_letter] = 0

            rows = letter.select('ul > li')
            print(len(rows))
            result[current_letter] += len(rows)

        links = soup.select('div#mw-pages > a')
        if len(links) > 1:
            current_url = BASE_URL + links[1]['href']
        else:
            break

        time.sleep(1)
        print()

    return result

def main():
    result = scrape()

    with open('beasts.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        for key, value in result.items():
            writer.writerow([key,value])


if __name__ == "__main__":
    main()