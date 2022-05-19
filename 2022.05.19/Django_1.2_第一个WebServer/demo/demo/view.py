from django.http import HttpResponse


def hello(request):
    s = "测试"
    return HttpResponse(s)
