from django.shortcuts import render, redirect
from .forms import UsersForm
from django.http import HttpResponse


def one(request):
    template = 'message/index.html'

    return render(request, template)


def home(request):
    return HttpResponse("Привет, я домашняя страница")


def dom(request):
    return HttpResponse("Привет, а я страница дом")


def data_users(request):
    error = ""
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'message/index.html')
        else:
            error = 'неверные данные'
    form = UsersForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'message/get_data_users.html', data)
