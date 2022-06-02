from django.shortcuts import render


class Person:
    def __init__(self, n, s, a):
        self.name = n
        self.sex = s
        self.age = a


def show(request):
    items = []
    items.append(Person("aaa", "m", 20))
    items.append(Person("bbb", "f", 18))
    d = {"items": items}
    return render(request, "show.html", d)
