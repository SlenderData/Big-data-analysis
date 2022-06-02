from django.shortcuts import render


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def getName(self):
        return "my name is " + self.name


def index(request):
    user = Person("xxx", 19, "male")
    return render(request, "show.html", locals())
