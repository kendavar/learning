from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import user
from AppTwo import forms

# Create your views here.

def index(request):
    my_dict ={"inside_me":"We are here to help you!"}
    return render(request, "AppTwo/help.html",context = my_dict )

def home(request):
    return render(request,"AppTwo/home.html",context={})

def users(request):
    form = forms.NewUser()
    if request.method == 'POST':
        form = forms.NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FROM INVALID")
    return render(request,'AppTwo/user.html',{'form':form})
    # users = user.objects.all()
    # details = {"user_details":users}
    # return render(request,"AppTwo/user.html",context=details)

def form_view(request):
    form = forms.ModelForm()
    return render(request,"AppTwo/forms_page.html",context={'form':form})
