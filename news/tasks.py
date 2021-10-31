import time

import requests
from celery import shared_task
import bs4
from django.db import IntegrityError

from news.models import News, Category
from accounts.models import User

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Accept-Language': 'ru',
}


@shared_task
def parser():
    fetch_politics()
    fetch_society()
    fetch_culture()
    fetch_economy()
    fetch_science()
    fetch_other()


def fetch_politics():
    ria_url = 'https://ria.ru/politics/'
    resp = requests.get(ria_url, headers)
    time.sleep(5)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    container = soup.select("div.list-item")
    url_list = list()
    for _ in container:
        url_list.append(_.select_one('a.list-item__image').get('href'))
    for url in url_list:
        resp = requests.get(url, headers)
        time.sleep(5)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        try:
            title = soup.select_one('div.article__title').text
            photo = soup.select_one('img').get('src')
            text_container = [x.text for x in soup.select('div.article__text')]
            text = ''.join(text_container)
            cat = Category.objects.filter(pk=1).first()
            user = User.objects.filter(pk=5).first()
            news = News(title=title, text=text, photo=photo, author=user, category=cat)
            try:
                news.save()
            except IntegrityError:
                pass
        except AttributeError:
            pass


def fetch_culture():
    ria_url = 'https://ria.ru/culture/'
    resp = requests.get(ria_url, headers)
    time.sleep(5)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    container = soup.select("a.cell-list-f__item-link.color-font-hover-only")
    url_list = list()
    for _ in container:
        url_list.append(_.get('href'))
    for url in url_list:
        resp = requests.get(url, headers)
        time.sleep(5)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        try:
            title = soup.select_one('div.article__title').text
            photo = soup.select('img')[1].get('src')
            text_container = [x.text for x in soup.select('div.article__text')]
            text = ''.join(text_container)
            cat = Category.objects.filter(pk=2).first()
            user = User.objects.filter(pk=5).first()
            news = News(title=title, text=text, photo=photo, author=user, category=cat)
            try:
                news.save()
            except IntegrityError:
                pass
        except AttributeError:
            pass


def fetch_science():
    ria_url = 'https://ria.ru/science/'
    resp = requests.get(ria_url, headers)
    time.sleep(5)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    container = soup.select("a.cell-list-f__item-link.color-font-hover-only")
    url_list = list()
    for _ in container:
        url_list.append(_.get('href'))
    for url in url_list:
        resp = requests.get(url, headers)
        time.sleep(5)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        try:
            title = soup.select_one('div.article__title').text
            photo = soup.select('img')[1].get('src')
            text_container = [x.text for x in soup.select('div.article__text')]
            text = ''.join(text_container)
            cat = Category.objects.filter(pk=3).first()
            user = User.objects.filter(pk=5).first()
            news = News(title=title, text=text, photo=photo, author=user, category=cat)
            try:
                news.save()
            except IntegrityError:
                pass
        except AttributeError:
            pass


def fetch_society():
    ria_url = 'https://ria.ru/society/'
    resp = requests.get(ria_url, headers)
    time.sleep(5)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    container = soup.select("div.list-item")
    url_list = list()
    for _ in container:
        url_list.append(_.select_one('a.list-item__image').get('href'))
    for url in url_list:
        resp = requests.get(url, headers)
        time.sleep(5)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        try:
            title = soup.select_one('div.article__title').text
            photo = soup.select_one('img').get('src')
            text_container = [x.text for x in soup.select('div.article__text')]
            text = ''.join(text_container)
            cat = Category.objects.filter(pk=4).first()
            user = User.objects.filter(pk=5).first()
            news = News(title=title, text=text, photo=photo, author=user, category=cat)
            try:
                news.save()
            except IntegrityError:
                pass
        except AttributeError:
            pass


def fetch_economy():
    ria_url = 'https://ria.ru/economy/'
    resp = requests.get(ria_url, headers)
    time.sleep(5)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    container = soup.select("div.list-item")
    url_list = list()
    for _ in container:
        url_list.append(_.select_one('a.list-item__image').get('href'))
    for url in url_list:
        resp = requests.get(url, headers)
        time.sleep(5)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        try:
            title = soup.select_one('div.article__title').text
            photo = soup.select_one('img').get('src')
            text_container = [x.text for x in soup.select('div.article__text')]
            text = ''.join(text_container)
            cat = Category.objects.filter(pk=5).first()
            user = User.objects.filter(pk=5).first()
            news = News(title=title, text=text, photo=photo, author=user, category=cat)
            try:
                news.save()
            except IntegrityError:
                pass
        except AttributeError:
            pass


def fetch_other():
    ria_url = 'https://ria.ru/world/'
    resp = requests.get(ria_url, headers)
    time.sleep(5)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    container = soup.select("div.list-item")
    url_list = list()
    for _ in container:
        url_list.append(_.select_one('a.list-item__image').get('href'))
    for url in url_list:
        resp = requests.get(url, headers)
        time.sleep(5)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        try:
            title = soup.select_one('div.article__title').text
            photo = soup.select_one('img').get('src')
            text_container = [x.text for x in soup.select('div.article__text')]
            text = ''.join(text_container)
            cat = Category.objects.filter(pk=6).first()
            user = User.objects.filter(pk=5).first()
            news = News(title=title, text=text, photo=photo, author=user, category=cat)
            try:
                news.save()
            except IntegrityError:
                pass
        except AttributeError:
            pass
