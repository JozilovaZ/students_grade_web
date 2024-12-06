from django.contrib.auth import login,logout
from django.shortcuts import render, redirect,get_object_or_404
from pyexpat.errors import messages

from .models import Student,Subject,Grade
from .forms import  AddFanlarForm,AddOquvchiForm,AddbahoForm
from .forms import SignupFOrm,LoginForm,UpdateGradeForm
from django.http import Http404



def home_page(request):
    students=Grade.objects.all()
    context={
        'students':students

    }

    return render(request,"home.html",context)


def oquvchi_page(request):
    students=Grade.objects.all()
    context={
        'students':students

    }

    return render(request,"oquvchi.html",context)


def fanlar_page(request):
    students=Grade.objects.all()
    context={
        'students':students

    }

    return render(request,"fan.html",context)


# fan qoshish
def add_fanqoshish(request):
    if request.method=='POST':
        forms=AddFanlarForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('fan_qosh')
    else:
        forms=AddFanlarForm()
    context={
            'forms':forms
    }
    return  render(request,"fan_qoshish.html",context)

# oquvchi  qo`shish
def add_oquvchiqosh(request):
    if request.method=='POST':
        forms=AddOquvchiForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('qoshish')
    else:
        forms=AddOquvchiForm()
    context={
            'forms':forms
    }
    return  render(request,"oquvchi_qosh.html",context)


def add_bahoq(request):
    if request.method=='POST':
        forms=AddbahoForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('b_q')
    else:
        forms=AddbahoForm()
    context={
         'forms':forms

    }
    return render(request,'baho_qoshish.html',context)


def signup_view(request):
    if request.method=='POST':
        form=SignupFOrm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=SignupFOrm()
    context={
        "form":form
    }
    return render(request,"signup.html",context)


def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return  redirect('bosh_sahifa')
    else:
        form=LoginForm()
    context={
        "form":form

    }
    return render(request,"login.html",context)






def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')



def grade_update_view(request,id):
    student=get_object_or_404(Student,id=id)
    grade = Grade.objects.filter(student=student).first()
    if not grade:
        raise Http404("Grade not found")

    if request.method=='POST':
        form=UpdateGradeForm(request.POST,instance=grade)
        if form.is_valid():
            form.save()
            return redirect('bosh_sahifa')
    else:
        form=UpdateGradeForm(instance=grade)
    context={
        "form":form
    }

    return render(request,"updata_grade.html",context)



def add_subject_view(request):
    if request.method=='POST':
        forms=AddFanlarForm(request.POST)
        if forms.is_valid():
            name=forms.cleaned_data['name']
            if Subject.object.filter(name__iexact=name).axitsts():
                messages.error(request,"Bu fan allaqachon mavjud")
            else:
                forms.save()
            messages.success(request,"Fan muvaffaqiyatli qo`shildi")
            return redirect('fan_add')

    else:
        forms=AddFanlarForm()
    context={
            'forms':forms
        }
    return render(request,"add_subject.html",context)




