from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def help(request):
    my_dict = {'insert_me': 'Hey I am from views.py to help you'}
    return render(request, 'help_app/help.html', context = my_dict)
