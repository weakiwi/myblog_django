from django.shortcuts import render
from urllib.error import URLError, HTTPError
import json
from urllib.request import Request, urlopen
from some_api.models import Book

# Create your views here.
def get_user_collection(request) :
    response = urlopen("https://api.douban.com/v2/book/user/34262520/collections?count=5")
    response = json.loads(response.read().decode('utf-8'))
    a = Book.objects.all();
    a.delete()
    tmp_arr = []
    for i in response["collections"] :
       Book.objects.create(title = i["book"]["title"], url = i["book"]["alt"])
       tmp_arr.append({i["book"]["title"] : i["book"]["alt"]})

    return render(request,'done.html',{"result" : json.dumps(tmp_arr)})
