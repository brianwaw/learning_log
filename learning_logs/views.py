from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib import messages
# Create your views here.


def index(request):
    """Home page view function"""
    entryform = EntryForm()
    topicform = TopicForm()

    if request.method == 'POST':
        if 'topicform-submit' in request.POST:
            topicform = TopicForm(request.POST)
            if topicform.is_valid():
                newtopic = topicform.save()
                messages.success(request, f"Successfully added {newtopic.text}")
                return redirect('learning_logs:index')

    context = {'entryform': entryform, 'topicform': topicform}

    return render(request, 'learning_logs/index.html', context)

