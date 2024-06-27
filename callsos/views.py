from django.shortcuts import render
from .models import sos
from .forms import sosForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    return render(request,'index.html')


def sos_list(request):
    soss=sos.objects.all().order_by('-created_at')
    return render(request,'sos_list.html',{'soss':soss})



@login_required
def sos_create(request):
    if request.method=='POST':
        form=sosForm(request.POST,request.FILES)
        if form.is_valid():
            sos1=form.save(commit=False)
            sos1.user=request.user
            sos1.save()
            return redirect('sos_list')
    else:
        form=sosForm()
        return render(request,'sos_form.html',{'form':form})
    

@login_required
def sos_edit(request,sos_id):
    sos1=get_object_or_404(sos,pk=sos_id,user=request.user)
    if request.method == 'POST':
        form=sosForm(request.POST,request.FILES,instance=sos1)
        if form.is_valid():
            sos2=form.save(commit=False)
            sos2.user=request.user
            sos2.save()
            return redirect('sos_list')
    else:
        form=sosForm(instance=sos1)
    return render(request,'sos_form.html',{'form':form})

@login_required
def sos_delete(request,sos_id):
    sos3=get_object_or_404(sos,pk=sos_id,user=request.user)
    if request.method == 'POST':
        sos3.delete()
        return redirect('sos_list')
    return render(request,'sos_confirm_delete.html',{'sos3':sos3})

def register(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
         user=form.save(commit=False)   
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request,user)
         return redirect('sos_list')
    else:
        form=UserRegistrationForm()

    return render(request,'registration/register.html',{'form':form})