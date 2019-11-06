from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from bs4 import *
import json
from libgen.book import Book
baseurl = "http://libgen.is"


def search(request):
    firstpartofurl = "/search.php?req="
    secondpartofurl = "&open=0&res=25&view=detailed&phrase=1&column=def&page="
    searchquery = request.GET.get('query')
    page = 1
    finalurl = baseurl+firstpartofurl+searchquery+secondpartofurl+str(page)
    page = requests.get(finalurl)
    soup = BeautifulSoup(page.content, 'html.parser')
    book = Book('a', 'b', 'c', 'd', 'e', 'f')
    tables = soup.find_all('table', {'rules': 'cols', 'width': '100%'})
    imageurl = tables[0].find('img')['src']
    trs = tables[0].find_all('tr')
    del trs[0]
    title = tds[3].text
    booklist = [book.toJSON(), book.toJSON()]

    return HttpResponse(title)
