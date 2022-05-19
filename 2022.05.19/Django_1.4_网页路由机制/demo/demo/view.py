from django.http import HttpResponse


def index(request):
    s = "<h3>欢迎</h3><a href='A'>Page A</a><br><a href='B'>Page B</a>"
    return HttpResponse(s)


def showA(request):
    s = "<h3>Page A</h3><a href='/'>Back</a>"
    return HttpResponse(s)


def showB(request):
    s = "<h3>Page B</h3><a href='/'>Back</a>"
    return HttpResponse(s)
