from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def mdToHtml(entry):
    title = util.get_entry(entry)
    markdowner = Markdown()

    if title == None:
        return None
    else:
        return markdowner.convert(title)

def entry(request, entry):
    content = mdToHtml(entry)

    if content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry,
            "content": content
    })

def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        content = mdToHtml(query)

        if content == True:
            return render(request, "encyclopedia/entry.html", {
                "entry": query,
                "content": content
            })
        else:
            database = util.list_entries()
            results = []
            for entry in database:
                if query.lower() in entry.lower():
                    results.append(entry)
            return render(request, "encyclopedia/search.html", {
                "results": results
            })

def create(request):
    return render(request, "encyclopedia/create.html")
