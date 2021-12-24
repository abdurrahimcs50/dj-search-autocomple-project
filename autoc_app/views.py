from django.shortcuts import render, redirect
from . models import Client
from . forms import ClientForm
# Create your tests here.
def home(request):
    clients = Client.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ClientForm()
    
    return render(request,'index.html',{"clients":clients, "form": form})