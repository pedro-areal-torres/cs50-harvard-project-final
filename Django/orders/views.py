import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum

from .models import Task, WorkOrder

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")
    
    return render(request,"menu.html") 

def index_Emp(request):
    return render(request,"menuEmp.html") 

#Login function
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'user: {username}')
        print(f'password: {password}')
        response = requests.post('http://localhost:8081/api/utilizadores/login', data={'username':username,'password':password})
        json_response = response.json()
        perm = json_response['permissoes']
        print(f"PERM {perm}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if perm == 1:
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "menuEmp.html")
        else:
            return render(request, "login.html", {"fail_message": "Invalid Credentials"})
    elif request.method == 'GET':
        return render(request, "login.html")

#Logout function that redirect you to the login page
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"sucess_message": "Logged Out"})

#Register Function
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        password = request.POST.get('password')
        permissoes = request.POST.get('permissoes')
        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        response = requests.post('http://localhost:8081/api/utilizadores/register', data={'nome':username,'password':password,'permissoes':permissoes})
        json_response = response.json()
        print(f'RESPOSTA: {json_response}')
        return render(request, "login.html", {"success_message": "New Account Created"})
    elif request.method == 'GET':
        return render(request, "register.html")

#Create a new task
def create_task_view(request):
    if request.method == 'POST':
        orderNum = request.POST.get('orderNum')
        nome = request.POST.get('name')
        descricao = request.POST.get('description')
        interveniente = request.POST.get('employer')
        response = requests.post('http://localhost:8081/api/tarefas', data={'orderNum':orderNum,'nome':nome,'descricao':descricao, 'interveniente':interveniente})
        json_response = response.json()
        print(f'RESPOSTA: {json_response}')
        return render(request, "menu.html", {"success_message": "New Task Created"})
    elif request.method == 'GET':
        return render(request, "create_task.html")

#Create Work Order
def create_order_view(request):
    if request.method == 'POST':
        orderNum = request.POST.get('orderNum')
        titulo = request.POST.get('title')
        descricao = request.POST.get('description')
        dataCriacao = request.POST.get('createDate')
        tipo = request.POST.get('tipo')
        custoEstimado = request.POST.get('cost')
        dataComeco = request.POST.get('startDate')
        dataPrevistaFim = request.POST.get('endDate')
        prioridadeOrdem = request.POST.get('prio')
        response = requests.post('http://localhost:8081/api/ordemTrabalho/chefeManutencao', data={'orderNum':orderNum,'titulo':titulo,'descricao':descricao, 'tipo':tipo, 'custoEstimado':custoEstimado, 'dataCriacao':dataCriacao, 'dataComeco':dataComeco, 'dataPrevistaFim':dataPrevistaFim, 'prioridadeOrdem':prioridadeOrdem})
        json_response = response.json()
        print(f'RESPOSTA: {json_response}')
        return render(request, "menu.html", {"success_message": "New Order Created"})
    elif request.method == 'GET':
        return render(request, "create_order.html")

#List all the task
def order_list_view(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")

    response = requests.get('http://localhost:8081/api/ordemTrabalho/chefeManutencao')
    json_response = response.json()
    print(f'RESPOSTA: {json_response}')
    orders = json_response['orders']
    ords = []
    for ordr in orders:
        orderNum = ordr['orderNum']
        titulo = ordr['titulo']
        tipo = ordr['tipo']
        custoEstimado = ordr['custoEstimado']
        ordr = WorkOrder.objects.create(orderNum=orderNum,title=titulo,typeOrder=tipo, cost=custoEstimado)
        ords.append(ordr)

    obj = {
        "ords" : ords
    }
    
    return render(request, "order_list.html", obj)

#List all the task
def task_list_view(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")

    response = requests.get('http://localhost:8081/api/tarefas')
    json_response = response.json()
    print(f'RESPOSTA: {json_response}')
    tarefas = json_response['tarefas']
    tasks = []
    for task in tarefas:
        orderNum = task['orderNum']
        name = task['nome']
        description = task['descricao']
        employer = task['interveniente']
        task = Task.objects.create(orderNum=orderNum,name=name,description=description, employer=employer)
        tasks.append(task)

    obj = {
        "tasks" : tasks
    }
    
    return render(request, "task_list.html", obj)

#List all the task
def task_emp_list_view(request):
    if not request.user.is_authenticated:
        return render(request,"login.html")

    response = requests.get('http://localhost:8081/api/tarefas')
    json_response = response.json()
    print(f'RESPOSTA: {json_response}')
    user = request.user.first_name
    tarefas = json_response['tarefas']
    tasks = []
    for task in tarefas:
        employer = task['interveniente']
        if (employer == user ):
            orderNum = task['orderNum']
            name = task['nome']
            description = task['descricao']
            task = Task.objects.create(orderNum=orderNum,name=name,description=description, employer=employer)
            tasks.append(task)

    obj = {
        "tasks" : tasks
    }
    
    return render(request, "task_list_emp.html", obj)


