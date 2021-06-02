from django.test import TestCase
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 just에 오신것을 환영합니다.")