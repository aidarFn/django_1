from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from . import models


def books_detail_view(request, id):
    if request.method == "GET":
        emp_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name='books/books_detail.html',
            context={
                'emp_id': emp_id,
            }
        )


def books_list(request):
    if request.method == 'GET':
        queryset = models.Books.objects.filter().order_by('-id')
        return render(
            request,
            template_name='books/books_list.html',
            context={
                'emp': queryset
            }
        )


def name_view(request):
    if request.method == 'GET':
        return HttpResponse('Айдар Догтурбеков, 18 лет')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Играть в игры')


def times_view(request):
    if request.method == 'GET':
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f'Текущее время: {current_time}')


def random_view(request):
    if request.method == 'GET':
        numbers = random.randint(1, 100)
        return HttpResponse(f"Число: {numbers}")



