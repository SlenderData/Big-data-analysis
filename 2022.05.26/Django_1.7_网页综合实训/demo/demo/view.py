from django.http import HttpResponse


def show(request):
    html = '''
        <form name="frm" id="frm" action="" method="post">
            <table>
                <tr>
                    <th>用户:</th>
                    <td><input type="text" name="user" id="user"></td>
                </tr>
                <tr>
                    <th>性别:</th>
                    <td>
                        <input type="radio" name="sex" value="男" checked>男
                        <input type="radio" name="sex" value="女">女
                    </td>
                </tr>
                <tr>
                    <th>年龄:</th>
                    <td><input type="text" name="age"></td>
                </tr>
                <tr>
                    <th>班级:</th>
                    <td>
                        <select name="dept">
                            <option value="18 软件">18 软件</option>
                            <option value="19 软件">19 软件</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <th>课程:</th>
                    <td>
                        <input type="checkbox" name="python" value="python">Python
                        <input type="checkbox" name="java" value="java">Java
                    </td>
                </tr>
                <tr>
                    <th>Email:</th>
                    <td><input type="text" name="email" id="email"></td>
                </tr>
            </table>
            <input type="submit" value="提交"">
        </form>
    '''
    msg = ""
    if request.method == "POST":
        user = request.POST.get("user", "")
        sex = request.POST.get("sex", "")
        age = request.POST.get("age", "")
        dept = request.POST.get("dept", "")
        python = request.POST.get("python", "")
        java = request.POST.get("java", "")
        email = request.POST.get("email", "")
        msg = user + "," + "," + sex + "," + age + "," + dept + "," + python + "," + java + "," + email
    html = html + "<div>" + msg + "</div>"
    return HttpResponse(html)
