from django.shortcuts import render
import re

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "regex/index.html")

    
def query(request):
    query = request.POST["query"]
    text = request.POST["text"]
    textMatch = re.findall(r""+query, text)
    context = {"textMatch": "".join(textMatch)}
    return render(request, "regex/index.html", context)