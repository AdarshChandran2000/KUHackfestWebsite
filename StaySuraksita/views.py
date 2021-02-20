# Create your views here.
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy

# from .models import table_name
# from django.contrib.auth import authenticate, login, logout
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.decorators import login_required

# CODE FOR Paginator, authenticate, login, logout WRITTEN IN COMPUTER

def index(request):
   return render(request, "StaySuraksita/index.html")

