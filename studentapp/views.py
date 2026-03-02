from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
def Home(request):
    form = EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
    context={
        'form':form,
    }
    return render(request,'app1/index.html',context)

