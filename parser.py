import requests
from bs4 import BeautifulSoup
import html_text


def parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='pi_text') # c HTML-тегами выводит текст записи

    title = soup.title.text  # заголовок записи с выводом группы
    text = html_text.extract_text(str(data))  # текст самой записи
    return title + '\n\n' + text


# -----------------------TEST-------------------------

post_url = input()
post_out = parser(post_url)

print(post_out)

# -----------------------END----------------------------
