from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return HttpResponse("Simple Calculator")


def suma(request, num1, num2):
    return HttpResponse(num1 + num2)


def resta(request, num1, num2):
    return HttpResponse(num1 - num2)


def multiplicacion(request, num1, num2):
    return HttpResponse(num1 * num2)


def division(request, num1, num2):
    return HttpResponse(num1 / num2)

