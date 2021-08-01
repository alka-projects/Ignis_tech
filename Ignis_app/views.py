from django.shortcuts import render
from Ignis_app.forms import eventForm
from Ignis_app.models import event
from django.shortcuts import redirect

# Create your views here.
def home(request):
    form=eventForm()
    event_list = event.objects.all().order_by('-id')
    if request.method=='POST':
        form= eventForm(request.POST,request.FILES)
        if form.is_valid(): 
            form.save()
    return render(request,'Ignis_app/home.html',{'form':form,'event_list':event_list})

def add_like(request,id):
    event_list=event.objects.all().filter(id=id).update(is_liked=True)
    return redirect('/')
    
def remove_like(request,id):
    event_list=event.objects.all().filter(id=id).update(is_liked=False)
    return redirect('/')
