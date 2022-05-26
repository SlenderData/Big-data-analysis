from django.http import HttpResponse


def respForm(request):
    response = HttpResponse()
    if request.method == "POST":
        name = request.POST.get("name")
        sex = request.POST.get("sex", "男")
    else:
        name = request.GET.get("name")
        sex = request.GET.get("sex", "男")
    response.write("method=" + request.method + "<br>")
    response.write("name=" + name + "<br>")
    response.write("sex=" + sex + "<br>")
    return response


def showForm(request):
    s = '''
        <html>
            <body>
                <h3>Hello 静态网页</h3>
                <form method="get" action="/resp">
                    <input type="text" name="name" value="GET" />
                    <input type="submit" value="GET提交" />
                </form>
                <form method="post" action="/resp">
                    <input type="text" name="name" value="POST" />
                    <input type="submit" value="POST提交" />
                </form>
            </body>
        </html>
    '''
    return HttpResponse(s)
