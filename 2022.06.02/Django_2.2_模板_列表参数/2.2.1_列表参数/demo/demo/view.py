from django.shortcuts import render


def show(request):
    s = [{"name": "xxx", "sex": "male", "age": 20}, {"name": "yyy", "sex": "female", "age": 20}]
    d = {"items": s}
    return render(request, "show.html", d)
