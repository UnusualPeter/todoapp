from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from main.models import Todo

# Create your views here.


def home(request):
    todo_items = Todo.objects.order_by('added_date').all()

    return render(request, 'main/index.html', {'todo_items': todo_items})


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST.get('content')

    Todo.objects.create(added_date=current_date, text=content)

    return HttpResponseRedirect(reverse('main:home'))


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()

    return HttpResponseRedirect(reverse('main:home'))
