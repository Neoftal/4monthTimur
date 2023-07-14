from django.shortcuts import HttpResponse
from datetime import datetime





# Create your posts here.
def hellow_view(request):
    if request.method == 'GET':
        return HttpResponse('"Hello! Its my project"')


def goodbyw_view(request):
    if request.method == 'GET':
        return HttpResponse('"Goodby user!"')

def data_view(request):
    if request.method == 'GET':
        now_date=datetime.now()
        return HttpResponse(f"{now_date}")
