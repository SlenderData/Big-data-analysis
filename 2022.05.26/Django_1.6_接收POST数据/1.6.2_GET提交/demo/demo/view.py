from django.http import HttpResponse


def respForm(request):
    response = HttpResponse()
    try:
        name = request.POST.get("name")
        sex = request.POST.get("sex", "男")
        response.write("name=" + name + "<br>")
        response.write("sex=" + sex + "<br>")
    except Exception as e:
        response.write(e)
    return response


def showForm(request):
    s = '''
        <html>
            <body>
                <h3>Hello 静态网页</h3>
                <form method="get" action="resp">
                    <input type="text" name="name" value="测试" />
                    <input type="submit" value="提交" />
                </form>
            </body>
        </html>
    '''
    return HttpResponse(s)
