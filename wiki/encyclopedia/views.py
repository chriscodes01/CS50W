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

