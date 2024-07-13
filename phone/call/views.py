from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Contact
from django.shortcuts import get_object_or_404


# Create your views here.
def base(request):
    return render(request,'base.html')
def add(request):
    if request.method == 'POST':
     name=request.POST.get('name')
     email=request.POST.get('email')
     number=request.POST.get('number')
     alt=request.POST.get('alt')
     image=request.POST.get('image')
     if Contact.objects.filter(name=name,email=email).exists():
        messages.info(request,'contact already exists!!!!')
        print ("already have")
     else:
        new_user=Contact.objects.create(name=name,email=email,number=number,alt=alt,image=image)
        new_user.save()
        return redirect(view_details)
    return render(request,'add.html')

def view_details(request):
    details=Contact.objects.all()
    return render(request,'view.html',{'detail':details})

def individual(request,contact_id):
    contact=get_object_or_404(Contact, pk=contact_id)
    return render(request,'phone/individual.html',{'contact':contact})



def update(request,update_id):
   get_details=get_object_or_404(Contact,id=update_id)
   if request.method == 'POST':
      new_user=request.POST.get('new_user')
      get_details.details=new_user
      get_details.save()
      return redirect(base)
   else:
      context={
         'get_details':get_details
      }
      return render(request,'update.html',context)
  

def delete(request,delete_id):
   delete_user=get_object_or_404(Contact,id=delete_id)
   delete_user.delete()
   return redirect('/')

 














































