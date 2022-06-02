from django.shortcuts import render


def index(request):
    name = "xxx"
    sex = "male"
    age = 20
    d = {"name": name, "sex": sex, "age": age}
    return render(request, "show.html", d)
