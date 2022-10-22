from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    # return HttpResponse("안녕하세요. pyboard에 오신 것을 환영합니다.")
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pyboard/question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'pyboard/question_detail.html', context)