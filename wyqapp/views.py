from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

import json
from django.http import JsonResponse
from django import views
from wyqapp.models import ages
from utlis.error_code import RET
from utlis.wyqtest2 import aa
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from utlis import  error_code

try:
# Create your views here.
    conn=get_redis_connection('default')
except Exception as e:
    print(e)

def grades(request):

    return render(request,'grades.html')

def login(request):
    if request.method == 'POST':

        # （1）默认数据请求
        # name = request.POST.get('username')
        # psd = request.POST.get('password')
        #
        # # （2）JSON数据请求
        # request_data = request.body.decode('utf-8')
        # request_dict = json.loads(request_data)
        # name = request_dict.get('username')
        # psd = request_dict.get('password')
        #
        # if name == "yang" and psd == '123':
        #     data={'sta':1,'name':'wyq','list':[1,2,3,4,5,6,7,8]}
        # else:
        #     data={'sta':1,'name':'wyq','list':[1,2,3,4,5,6,7,8]}
            # data=json.dumps(data)
            # print(data)
            # print(type(data))

        # return HttpResponse(data,content_type='application/json')
        from  utlis.HandleJson  import HandleJson
        redata={}
        jstr=request.POST.get("jstr",None)
        key=request.POST.get("key",None)
        value=request.POST.get("key1",None)
        if  len(value)==0:
            value=' '
        redata["jstr"]=jstr
        redata["key"]=key
        redata["value"]=value
        print(redata["value"])
        try:
            hj = HandleJson(json.loads(jstr))
            res2 = hj.find_key_path(key)
            res3 = hj.find_value_path(value)
            # print(res3)
            # print(redata)
            redata['res2'] = res2
            redata['res3'] = res3
            print(res3)

            # redata={"jstr":jstr,"res2key":res2,'res2value':res3}
            return render(request, 'formit.html', {"redata": redata})
        except Exception as e:
            redata["error"] = "查找出现异常,请自行检查数据"
            return render(request, 'formit.html', {"redata":redata})

    else :
        return render(request,'formit.html')

def loginq(request):
    print(request.POST)
    print(request.body)
    if request.method == 'POST':
        # （1）默认数据请求
        # name = request.POST.get('username')
        # psd = request.POST.get('password')

        # （2）JSON数据请求
        request_data = request.body.decode('utf-8')
        print(request_data)
        request_dict = json.loads(request_data)
        name = request_dict.get('username')
        psd = request_dict.get('password')
        if name=='wyq' and psd=='123':
            re=HttpResponse('设置cookies生效')
            re.set_cookie('wyq',name,max_age=60)
            return re
        else:
            # from wyqapp.task_sm.sm.task import wyq_im
            #
            # wyq_im.delay()
            return  HttpResponse('不设置cokkises')

    else :

        return render(request,'loginq.html')

def checklogin(fun):
    def inner(request,*args,**kwargs):
        tt = request.COOKIES.get('wyq')
        if tt:
            return HttpResponse('ok')
        else:
            return HttpResponse('不ok')

        return fun(request,*args,**kwargs)
    return inner




# @checklogin
def index(request):

    return render(request, 'zhengAdmin-master/index.html')
def cutr(request):

    # return render(request, 'zhengAdmin-master/crud_url.html')
    # return render(request, 'zhengAdmin-master/crud_url.html')
    return render(request, 'zhengAdmin-master/crud_server.html')

class login1(views.View):
    def get(self,re):
        # return  HttpResponse('ok1')
        list=[{'name1':'1'},{'name2':'2'},{'name3':'3'}]
        data={'data1':list}
        return  JsonResponse(data)
    def post(self,re):
        return HttpResponse('ok post')


def set_session(re):
    re.session['name']='wyqtest'
    return HttpResponse('设置session')

def get_session(re):
    t=re.session['name']
    if t=='wyqtest':
        return HttpResponse('11111')
    else:
        return HttpResponse('22222')


def getname(request):
    from utlis.retustr import restr
    if request.method == 'POST':
        data={'error':error_code.RET.OK,'error_msg':'成功','ages_info':restr.Rtr}
        return JsonResponse(data)
    else:
        return render(request, 'ref.html')
def setname(request):
    from utlis.retustr import restr
    if request.method == 'POST':
        try:
            request_data = request.body.decode('utf-8')
            request_dict = json.loads(request_data)
            note=request_dict.get('rdata',None)
            restr.Rtr=note
            data={'error':error_code.RET.OK,'error_msg':'成功'}
            return JsonResponse(data)
        except Exception as e:
            data = {'error': error_code.RET.SERVERERR, 'error_msg': '内部错误'}

    # else:
    #     return render(request, 'ref.html')
# @csrf_exempt
def loginadd(request):
        if request.method == "GET":
            return render(request, 'loginadd.html')
        elif request.method == "POST":
            print(request.POST)
            user = request.POST.get('user')
            pwd = request.POST.get('pwd')
            if user == 'root' and pwd == "123456":
                # 生成随机字符串
                # 写到用户浏览器cookie
                # 保存在服务端session中
                # 在随机字符串对应的字典中设置相关内容
                # request.session['username'] = user
                # request.session['islogin'] = True
                if request.POST.get('rmb', None) == '1':
                    # 认为设置超时时间
                    # request.session.set_expiry(10)
                    return redirect('/login/')
            else:
                return render(request, 'loginadd.html')


def logout(request):
    del request.session['username']
    request.session.clear()
    return redirect('/login/')

'''
def alsk(request):
    if request.method == 'GET':
        return render(request, 'formit.html')
    else:


        import requests,json
        debug= request.POST.get('debug')
        print(debug)
        env= request.POST.get('env')
        datate= request.POST.get('jstr')
        try:
            data= json.loads(datate)
        except Exception as e:

            error = "入参出现异常,请自行检查数据 %s" % (e)
            reqdata = {'datate':datate, 'error': error}

            return render(request, 'formit.html',reqdata)
        api=env+data['api']

        head=data['head']
        if debug=='true':
            data['body']['debug']=1
        body=data['body']
        if head.get('version', None):
            version = head.get('version', None)
        else:
            version = head.get('Version', None)
        #   调用加密接口，请求加密
        url = "http://10.160.84.207:8206/husky/system/aes"
        clienttype = head['ClientType']
        inputreq = (json.dumps(body))
        data1 = {
            "type": "0",
            "version": version,
            "clienttype": clienttype,
            "key": "",
            "input": inputreq
        }
        re = requests.post(url, data={'req': json.dumps(data1)})
        redata = re.text.strip()
        data2 = {"req": redata}
        redata=requests.post(url=api,headers=head,data=data2)
        debugInfo = redata.json().get('debugInfo',None)
        oldreq = redata.text
        if debugInfo:
            goods_par = debugInfo.split('misReqEnd')[0].split('misReq:')[1].split('misReq')[0]
            goods_req= debugInfo.split('misResp:')[1].split('misRespEnd')[0]
            goods={'商品库入参':goods_par,'商品库出参':goods_req}
            # del redata.json()['debugInfo']
            # nodebuginfo=redaa.json()
            # print(nodebuginfo)
            # print(goods_par)
            # print(goods_req)
            # print(redata.text)
            print(goods)
            reqdata = {'datate':datate,'goods_par':goods_par,'goods_req':goods_req, 'oldreq': oldreq}
            return render(request, 'formit.html', reqdata)

        else:
            reqdata={'datate':datate,'oldreq':oldreq}
            print(reqdata)
            return render(request, 'formit.html',reqdata)


        # return JsonResponse(reqdata)

'''

def alsk(request):
    import requests, json
    if request.method == 'GET':
        return render(request, 'test1.html')
    else:

        return JsonResponse(aa(request))

def wyqlogin(request):
    if request.method == 'GET':
        return render(request, 'zhengAdmin-master/login.html')
    else:

            request_data = request.body.decode('utf-8')
            request_dict = json.loads(request_data)
            # note=request_dict.get('rdata',None)
            data={'code':1,'error_msg':'成功'}
            return JsonResponse(data)

def  fenye(request):
    book_list = []
    '''
    数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    '''
    # for x in range(1, 100):  # 一共 25 本书
    #     book_list.append(x)

    book_list=[ x for x in range(1,100)]

    # 将数据按照规定每页显示 10 条, 进行分割
    paginator = Paginator(book_list, 10)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            books = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            books = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            books = paginator.page(paginator.num_pages)
    print(books.object_list)
    template_view = 'page.html'
    return render(request, template_view, {'book_list': books})


def wyqadduser(request):
    # request_data = request.body.decode('utf-8')
    # request_dict = json.loads(request_data)
    print(request.GET)

    page = request.GET.get('page')
    num = request.GET.get('rows')
    sortnum = request.GET.get('sort')
    sortOrdernum = request.GET.get('sortOrder')
    right_boundary = int(page) * int(num)
    print(right_boundary)

    #
    with open('static/resources/data/data2.json','r') as  f:
        p=json.loads(f.read())
    p['data']['totalCount']=len(p['data']['logs'])
    p['data']['logs']=p['data']['logs'][int(num)*(int(page)-1):right_boundary]
    print(p)
    print(p['data']['totalCount'])
    return JsonResponse(p)

def synconfig(request):
    return render(request, 'zhengAdmin-master/synconfig.html')

