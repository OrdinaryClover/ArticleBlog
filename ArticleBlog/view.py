from django.shortcuts import HttpResponse,render_to_response,render
from django.template.loader import get_template
from app01.models import *
from django.core.paginator import Paginator
import hashlib


##登录装饰器
def loginValid(func):
    def inner(request,*args,**kwargs):
        ##校验用户的身份
        cookie_username = request.COOKIES.get("username")
        session_username = request.session.get("username")
        if cookie_username and session_username and cookie_username==session_username:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect("/login/")
    return inner









##密码加密
def setPassword(password):
    ##实例化对象
    md5 = hashlib.md5()
    ##对password进行加密
    md5.update(password.encode())
    result = md5.hexdigest()  ##得到一个16进制的加密结果
    return result


@loginValid
def index(request):
    ##返回数据
    ##1、返回六条文章数据  排序  按照时间逆序
    article = Article.objects.order_by("-date")[0:6]
    one = article[0]
    #############################
    # print(one)
    # print(one.author)
    # print(one.author.name)
    # print(one.type.first().name)
    # print(one.type.first())
    ##2、返回图文推荐文章内容  7条
    ##图文推荐
    recommend_article = Article.objects.filter(recommend=1).order_by("-date")[:7]
    ##3、点击排行12条数据
    cilck_article = Article.objects.order_by("date")[:12]
    return render_to_response("index.html",locals())

@loginValid
def about(request):
    templates_obj = get_template("about.html")
    result = templates_obj.render()
    return HttpResponse(result)

def listpic(request):
    templates_obj = get_template("listpic.html")
    result = templates_obj.render()
    return HttpResponse(result)

def newslistpic(request,page):
    #查询文章
    article = Article.objects.all().order_by("id")
    pagnitor_obj = Paginator(article,6)
    page_obj = pagnitor_obj.page(page)   #分页之后的结果

    ##获取当前的页码
    page_num = page_obj.number
    ##开始的页码
    start = page_num - 2
    if start <=2:
        start = 1
        end = start + 5
    ##结束的页码
    else:
        end = page_num + 3
        if end >= pagnitor_obj.num_pages:
            start = pagnitor_obj.num_pages -4
            end = pagnitor_obj.num_pages+1
    ##构建range
    # page_range = pagnitor_obj.page_range[start:end]
    page_range = range(start,end)


    return render_to_response("newslistpic.html",locals())


def articleinfo01(request):

    return render_to_response("articleinfo.html",locals())
##文章详情
def articleinfo(request,id):

    article = Article.objects.get(id = id)
    return render_to_response("articleinfo.html",locals())

def fy_test(request,page):
    print(page)
    ##查询文章
    article = Article.objects.all().order_by()
    print(article)
    paginator_obj = Paginator(article,6)   #每页想获取几条数据
    ## paginator_obj = Paginator(数据集，每页展示的条数)
    # print(paginator_obj)
    # print(paginator_obj.count) ##数据的总条数
    # print(paginator_obj.num_pages)  ##总页数


    page_obj = paginator_obj.page(page)    #你想获取第几页的数据
    # print(page_obj)  ##<Page 1 of 11>
    ##循环遍历，得到分页之后的数据
    for one in page_obj:
        print(one)
    # print(page_obj.has_next())  ##是否有下一页  返回布尔值
    # print(page_obj.has_previous())  ##是否有上一页 ，返回布尔值
    # print(page_obj.number)  ##返回当前所在的页码
    # print(page_obj.previous_page_number())  ##上一页的页码
    # print(page_obj.next_page_number())   ##下一页的页码
    # print(page_obj.has_other_pages())  ##是否有其他的页

    return  HttpResponse("fy_test")

def add_article(request):

    # for i in range(50):
    #     article = Article()
    #     article.title = "title_%s" % i
    #     article.content = "content_%s" % i
    #     article.description = "description_%s" % i
    #     article.author = Author.objects.get(id=1)
    #     article.save()
    #
    #     ##多对多关系中
    #     article.type.add(Type.objects.get(id=1))
    #     article.save()


    # Article.objects.filter(author_id__in=[1]).delete()



    return HttpResponse("add article")

###18、请求的部分
def request_demo(request):
    # print(dir(request))
    """
    ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding', '_get_full_path', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'headers', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']
    """
    # print(request.COOKIES)  #表示用户的身份
    # {'monitor_count': '619', 'csrftoken': 'YgHBlgHOFF2I6Ku4qMwmU5zxT0xECk3g6xxbkvZulkH8LKTVztOjMNrSfRrtHSAJ', '__guid': '96992031.4394207474015095000.1581514878044.2087', 'sessionid': 'ih3uwe7re7om231r1o7lnk4lf4btgffu'}
    # print(request.FILES)
    # name = request.GET.get("name")
    # age = request.GET.get("age")
    # print(name)
    # print(age)
    print(request.method)  #请求的方法
    print(request.scheme)  #请求的协议
    print(request.path)  #请求的路径
    print(request.META)  #请求的信息
    print(request.META.get("OS"))  #请求的系统
    # print(request.HTTP_REFERER)  #请求来源
    print(request.META.HTTP_HOST)  #请求的主机


    return HttpResponse("request_demo")

def get_test(request):
    data = request.GET
    print(data)
    name = request.GET.get("name")
    age = request.GET.get("age")

    return HttpResponse("{},{}".format(name,age))

def post_demo1(request):
    date = request.POST
    print(date)
    return HttpResponse("post_demo")

def get_demo(request):
    # data = request.GET
    # print(data)
    # search = request.GET.get("search")
    # print(search)


    #### 需求：通过输入文章的标题，返回包含输入内容的文章标题
    ##接受请求  处理请求   返回响应
    search = request.GET.get("search")
    ##查询数据库  得到文章的标题
    if search:
        article = Article.objects.filter(title__contains=search).values("title")
    ##返回结果

    return render_to_response("getdemo.html",locals())

def post_demo(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username)
    print(password)

    return render(request,"post_demo.html")
from app01 import forms
###注册的模型
def register(request):
    ##处理了get请求，返回了注册页面
    ##接受到用户注册的请求  ，post
    ##将用户的数据  保存到数据库中
    userform = forms.UserForm()
    if request.method == "POST":
        # data = request.POST
        # print(data)
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        data = forms.UserForm(request.POST)
        if data.is_valid():
            ##进行迁移，成功之后返回True 失败返回Flase
            ##获取到检验成功的数据
            username = data.cleaned_data.get("username")
            password = data.cleaned_data.get("password")
            ##判断用户名是否存在
            flag = User.objects.filter(username=username)
            if flag:
                #存在不注册
                message = "用户已经存在,请重新输入"
            else:
            ##不存在注册
            ##保存数据到数据库
                message = "注册成功"
                User.objects.create(username=username,password=setPassword(password))

        else:
            ##校验失败
            message = data.errors

        # ##判断用户名是否存在
        # flag = User.objects.filter(username=username)
        # if flag:
        #     message = "用户已经存在,请重新输入"
        # else:
        # ##保存数据到数据库
        #     message = "注册成功"
        #     User.objects.create(username=username,password=setPassword(password))

    return render(request,"register.html",locals())

def ajax_demo(request):
    return render_to_response("ajaxdemo.html")



from django.http import JsonResponse
##返回ajax注册的页面
def ajax_register(request):
    ##写处理业务的代码
    return render(request,"ajax_register.html")

##练习json请求
def ajax_get_req(request):
    """
    处理ajax的get请求
        获取到ajax的值，进行查询数据库，判断用户是否村早
    :param request:
        username 用户的账号
    :return:
        返回是否存在的结果
    """

    username = request.GET.get("username")
    print(username)
    result = {"code":10000,"msg":""}
    if username:
        flag = User.objects.filter(username=username).exists()
        if flag:
            result = {"code":10001,"msg":"账号已经存在，换一个试试"}
        else:
            result = {"code":10000,"msg":"账号不存在，可以使用"}
    else:
        result = {"code":10002,"msg":"账号不能为空"}
    return JsonResponse(result)

def ajax_post_req(request):

    """
    完成注册的需求
    :param request:
        username
        password
    :return:
        Json对象  成功或者失败
    """

    username = request.POST.get("username")
    password = request.POST.get("password")
    if username and password:
        try:
            User.objects.create(username=username, password=password)
            result = {"code": 10000, "msg": "注册成功"}
        except:
            result = {"code":10002,"msg":"注册失败"}
    else:
        result = {"code": 10001, "msg": "请求参数为空"}

    return JsonResponse(result)

# ##处理ajax get请求
# def ajax_get_req(request):
#     """
#     处理ajax的get请求
#         获取到ajax的值，进行查询数据库，判断用户是否村早
#     :param request:
#         username 用户的账号
#     :return:
#         返回是否存在的结果
#     """
#
#     username = request.GET.get("username")
#     print(username)
#     if username:
#         flag = User.objects.filter(username=username).exists()
#         if flag:
#             message = "账号存在"
#         else:
#             message = "账号不存在"
#     else:
#         message = "账号不能为空"
#     return HttpResponse(message)

##下发cookie
def set_cookie(request):
    response = HttpResponse("设置cookie")
    response.set_cookie("username","zhangsan",max_age=60)
    response.set_cookie("age",19)
    return response
def get_cookie(request):
    data = request.COOKIES
    username = request.COOKIES.get("username")
    age = request.COOKIES.get("age")
    print(username)
    print(age)
    return HttpResponse("获取cookie")
def delete_cookie(request):
    ##删除cookies
    response = HttpResponse("删除cookie")
    response.delete_cookie("age")
    response.delete_cookie("username")
    return response

def set_session(request):
    ##设置session
    request.session["username"] = "zhangsan"

    return HttpResponse("设置session")

def get_session(request):
    username = request.session.get("username")
    return HttpResponse(username)

def delete_session(request):
    username = request.session.get("username")
    print(username)

    del request.session["username"]
    return HttpResponse("删除session")



from django.http import HttpResponseRedirect
def login(request):
    ##判断登录
    if request.method == "POST":
        ##获取值
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            # flag = User.objects.filter(username=username, password=setPassword(password)).exists()
            user = User.objects.filter(username=username,password=setPassword(password)).first()
            if user:
                # True
                # return HttpResponse("登录成功")
                # response = HttpResponse("登录成功")
                ##参数：要跳转的路径
                response = HttpResponseRedirect('/index/')
                ##下发occkie和session
                response.set_cookie("username",user.username)
                response.set_cookie("user_id",user.id)
                request.session["username"] = user.username
                return response
            else:
                return HttpResponse("账号密码不正确")
        else:
            ##参数为空
            return HttpResponse("请输入账号密码")
    return render(request,"login.html")

def logout(request):
    ##删除cookie 和session
    ##重新定向到登录页
    response = HttpResponseRedirect("/login")
    response.delete_cookie("username")
    del request.session["username"]

    return response