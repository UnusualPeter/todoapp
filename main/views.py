from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from main.models import Todo

# Create your views here.


def home(request):
    return render(request, 'main/index.html')


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST.get('content')

    Todo.objects.create(added_date=current_date, text=content)

    return render(request, 'main/index.html')
