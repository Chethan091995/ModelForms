from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from myapp.models import Topic,Webpage,AccessDetails

def create_topic(request):
    topic=request.POST.get("topic")
    t=Topic.objects.get_or_create(Topic_name=topic)
    if t[1]==True:
        t[0].save()
        return HttpResponse("<h1>Topic added succesfully</h1>")
    else:
        return HttpResponse("<h1> Topic Exists Please try again</h1>")
    return render(request,"create_topic.html")

def create_web(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        name=request.POST.get("name")
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(Topic_name=topic)[0]
        w=Webpage .objects.get_or_create(Topic=t,name=name,url=url)
        w.save()
        return HttpResponse("<h1>Webpage added successfully</h1>")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})

def display_topic(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",context={'topics':topics})

def display_webpage(request):
    webpages=Webpage.objects.all()
    return render(request,"display_webpage.html",context={'webpages':webpages})

def disp_img(request,id):
    profile=ProfilePic.objects.filter(id=id)
    return render(request,"disp_image.html",{'profile':profile})
from myapp.forms import *
def topic_modelform(request):
    if request.method=="POST":
        form=TopicForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'mdoelform.html',{'form':form})
    form=TopicForm()
    return render(request,'modelform.html',{'form':form})
def webform(request):
    if request.method=="POST":
        form=WebpageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'mdoelform.html',{'form':form})
    form=WebpageForm()
    return render(request,'modelform.html',{'form':form})