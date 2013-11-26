__author__ = 'mpetyx'

from django.shortcuts import render_to_response

def home(request):
    """ Home Page """
    return render_to_response('index.html')