from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
from .models import Choice
def index(request):
    page = "User Management"
    User = ["Trần Hữu Phú","Đức Duy","Huy Hoàng","Huy Hoàng"]
    ns = ["01-09-1998","01-13-1990","01-07-1997","09-09-1995"]
    address = ["Huế" ,"Quảng Trị","Ha Nội","Đà Lạt"]
    context = {"page" : page ,"User":User,"ns":ns,"address" : address}
    return render(request ,"polls/index.html" , context)

def listQuestion(request):
    questions = Question.objects.all();
    choice = Choice.objects.all();
    context = {"listquestion": questions ,"choice":choice}
    return render(request ,"polls/questionsPage.html" , context)
