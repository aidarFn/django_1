from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random


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



