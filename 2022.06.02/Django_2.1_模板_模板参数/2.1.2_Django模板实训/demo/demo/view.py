from django.shortcuts import render


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        age = request.POST.get("age")
        if sex == "M":
            mchecked = "checked"
        else:
            fchecked = "checked"
    else:
        name = "xxx"
        sex = "M"
        age = 20
        mchecked = "checked"
    return render(request, "show.html", locals())
