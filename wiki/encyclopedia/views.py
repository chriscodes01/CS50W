from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    # Search
    if request.method == "POST":
        entry = util.get_entry(request.POST.get("q"))
        return render(request, "encyclopedia/entry.html", {"entry" : entry})
        
    # Home Page
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
    })

#def entry(request, entry):
    #return render(request, "encyclopedia/entry.html", {
        #"entry": util.get_entry(entry)
    #})

