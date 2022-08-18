
from django.views.generic import CreateView
from .models import File

from django.shortcuts import render


from .forms import FileForm
# Create your views here.


def form_view(request):
    if request.method =='POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            

        else:
            print("Not a bvlid form")

        
        print(request.POST)
        return render(request,'file_form.html',{'form':form})

    else:
        form = FileForm()
        return render(request,'file_form.html',{'form':form})
        
    
    
    