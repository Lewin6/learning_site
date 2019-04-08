from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from learning_sites.models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.


def index(request):
    return render(request, 'learning_sites/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_sites/topics.html',context)

def topic(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    entries=topic.entry_set.order_by('-date_added')
    context={'topic':topic,"entries":entries}
    return render(request, 'learning_sites/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form=TopicForm()
    else:
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_sites:topics')) # Determine the URL based on the url mode

    context={'form':form}
    return render(request,'learning_sites/new_topic.html',context)

def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form=EntryForm();
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry= form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_sites:topic',args=[topic_id]))

    context={'topic':topic,'form':form}
    return render(request,'learning_sites/new_entry.html',context)

def edit_entry(request, entry_id):
    entry=Entry.objects.get(id=entry_id)
    topic=entry.topic

    if request.method !='POST':
        form = EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_sites:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_sites/edit_entry.html', context)
