from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import json
from libgen.book import Book

baseurl = "http://libgen.is"
import urllib.parse


def search(request):
    firstpartofurl = "/search.php?req="
    secondpartofurl = "&open=0&res=25&view=detailed&phrase=1&column=def&page="
    searchquery = request.GET.get('query')
    page = 1
    finalurl = baseurl+firstpartofurl+searchquery+secondpartofurl+str(page)
    page = requests.get(finalurl)
    soup = BeautifulSoup(page.content, 'html.parser')
    booklist=[]
    tables = soup.find_all('table', {'rules': 'cols', 'width': '100%'})
    for i in range(0,len(tables),2):
        imageurl = baseurl+tables[i].find('img')['src']

        trs = tables[i].find_all('tr')
        print(len(trs))
        del trs[0]

        title=trs[0].find_all('td')[2].text
        author=trs[1].find_all('td')[1].text
        print(title)
        print(author)
        year=int(trs[4].find_all('td')[1].text)
        link = trs[0].find_all('td')[2].find('a')['href']
        print(year)
        language=trs[5].find_all('td')[1].text

        link=link[2:]
        bookurl=urllib.parse.urljoin(baseurl,link)
        book =Book(title,author,year,language,imageurl,bookurl)
        booklist.append(book.toJSON())
    return HttpResponse(json.dumps(booklist))
def description(request):
    url =  request.GET.get('url')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    td = soup.find_all('td',{'colspan' : '4'})
    print(td[0].text)
    description = td[0].text
    downloadlink = soup.find('a',{'title' : 'gen.lib.rus.ec'})['href']
    

    downloadlink=downloadlink.strip()   
    response = {

        'description' : description,
        'downloadlink' : downloadlink
    }
    return HttpResponse(json.dumps(response))
def download(request):
    url = request.GET.get('url')
    page = requests.get(url)
    print(url)
    soup = BeautifulSoup(page.content,'html.parser')
    downloadlink= soup.find('a')['href']
    downloadlink=urllib.parse.urljoin(url,downloadlink)
    response = {
        'downloadlink' : downloadlink
    }
    return HttpResponse(json.dumps(response))
