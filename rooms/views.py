from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
#from django.http import HttpResponse, Http404
from .models import Room, Topic, Post

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})
# Create your views here.

def room_topics(request, pk):
    #try:
    #    room = Room.objects.get(pk=pk)
    #except Room.DoesNotExist:
    #    raise Http404
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'topics.html', {'room' : room})

def new_topic(request, pk):
    room = get_object_or_404(Room, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.room = room
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('room_topics', pk=room.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'room' : room, 'form' : form})
