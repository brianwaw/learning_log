from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm, TopicalEntry
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.


@login_required
def index(request):
    """Home page view function"""
    entryform = EntryForm()
    topicform = TopicForm()

    if request.method == 'POST':
        if 'topicform-submit' in request.POST:
            topicform = TopicForm(request.POST)
            if topicform.is_valid():
                newtopic = topicform.save(commit=False)  # Topic model instance that has not been saved yet.
                newtopic.owner = request.user  # Assign the owner field to the currently logged-in user.
                newtopic.save()  # Saving the model instance.
                messages.success(request, f"Successfully added {newtopic.text}")
                return redirect('learning_logs:all_topics')

        elif 'entryform-submit' in request.POST:
            entryform = EntryForm(request.POST)
            if entryform.is_valid():
                newentry = entryform.save()
                messages.success(request, f"Successfully added {newentry.text} on {newentry.topic}")
                return redirect('learning_logs:index')

    context = {'entryform': entryform, 'topicform': topicform}

    return render(request, 'learning_logs/index.html', context)


@login_required
def all_topics(request):
    """Display all available topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {
        'topics': topics
    }
    return render(request, 'learning_logs/all_topics.html', context)


@login_required
def topic(request, topic_name):
    """display entries of each topic"""
    topicc = get_object_or_404(Topic, text=topic_name)

    # A user only accesses topics belonging to them
    if topicc.owner != request.user:
        raise Http404

    all_entries = topicc.entries.order_by('-date_added')
    context = {
        'topicc': topicc,
        'all_entries': all_entries
    }
    return render(request, 'learning_logs/topic.html', context)


@login_required
def add_entry(request, topic_name):
    """add entry to specified topic"""
    entry_form = TopicalEntry()
    if request.method == 'POST':
        entry_form = TopicalEntry(request.POST)
        if entry_form.is_valid():
            topic = get_object_or_404(Topic, text=topic_name)  # instance for Topic model due to the foreign key aspect

            # User can only add entries to topics belonging to them
            if topic.owner != request.user:
                raise Http404

            entry = entry_form.save(commit=False)  # instance for Entry model.

            entry.topic = topic  # Assign the topic attribute into the Entry model.
            entry.save()
            return redirect('learning_logs:topic', topic_name=topic.text)

    context = {
        'topic_name': topic_name,
        'entry_form': entry_form,
    }
    return render(request, 'learning_logs/topical_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Editing Entries for specific topic"""
    entry = get_object_or_404(Entry, id=entry_id)
    topic_name = entry.topic
    topic_object = get_object_or_404(Topic, text=topic_name)

    # Allow editing entries for topic user owns
    if topic_object.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = TopicalEntry(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_name=topic_object.text)

    else:
        form = TopicalEntry(instance=entry)

    context = {
        'entry': entry,
        'topic_object': topic_object,
        'form': form,
    }
    return render(request, 'learning_logs/edit_entry.html', context)