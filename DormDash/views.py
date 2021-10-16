from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return HttpResponse("Homepage unimplemented")

def signup(request):
    return HttpResponse("askfjhjkdfhsdjkfksdnfkjsdnfjk")