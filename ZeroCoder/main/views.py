from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это домашняя страница моего первого проекта на Django</h1>")

def new(request):
    return HttpResponse("<h1>А здесь я буду публиковать самые горячие новости</h1>")

def data(request):
    return HttpResponse("<h1>Отсюда можно будет получить доступ к базам данных моего первого проекта на Django</h1>")

def test(request):
    return HttpResponse("<h1>Ну а это тестовая страничка моего первого проекта на Django</h1>")