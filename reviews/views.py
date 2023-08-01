from django.shortcuts import render

def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})

def search(request):
    search = request.GET.get('search')
    return render(request, "search.html", {"search": search})