# videoclub/views.py
from django.shortcuts import render

#vista normal
def home(request):
    return render(request, "videoclub/index.html")

 
