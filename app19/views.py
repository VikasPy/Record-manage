from django.shortcuts import render,redirect
from app19.models import mymodel

# Create your views here.
def home(request):
    if request.method =='POST':
        name=request.POST['nam']
        sction=request.POST['sction']
        rollno=request.POST['rollno']
        Email=request.POST['email']
        jon=request.POST['join']
        contact=request.POST['contct']
        mymodel.objects.create(Name=name,Sction=sction,Rollno=rollno, email=Email, join=jon, Conntct=contact)
        return redirect('home')
    else:
       ss= mymodel.objects.all()
       return render(request,'home.html',{'ss':ss})
    

def show(request):
        ss= mymodel.objects.all()
        return redirect('home')




def Update(request,id):
    data=mymodel.objects.get(id=id)
    
    if request.method == 'POST':
        name=request.POST['nam']
        sction=request.POST['sction']
        rollno=request.POST['rollno']
        Email=request.POST['email']
        jon=request.POST['join']
        contact=request.POST['contct']

        d1 = mymodel(id=id,Name=name, Sction=sction,Rollno=rollno, email=Email, join=jon, Conntct=contact)
        d1.save()
        return redirect('home')
    else:
        return render(request,'Home.html',{'n':data})


def delete(request,id):
    dd=mymodel.objects.get(id=id)
    dd.delete()
    return redirect('home')

