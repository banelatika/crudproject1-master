import re
from django.shortcuts import render, HttpResponseRedirect
from .forms import studentregistration
from .models import User


# this function add new item in databases and show all item
def add_show(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pm)
            reg.save()
            fm = studentregistration()
    else:
        fm = studentregistration()
    stud = User.objects.all()  # all data base collect on stud objects
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})

# this dunction update the data and edit the details


def update_data(request, id):
        if request.method == 'POST':
            pi = User.objects.get(pk=id)
            fm = studentregistration(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi = User.objects.get(pk=id)
            fm = studentregistration(instance=pi)
            
        return render(request, 'enroll/updatestudent.html', {'form':fm}   )


# this function will detele all details on databases
def delete_date(request, id):
    if request.method == "POST":
        # perticula one data they get on data base
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('tasksboard')
