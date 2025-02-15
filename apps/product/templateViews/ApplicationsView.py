from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import ApplicationsForm
from ..models import ApplicationsModel
redirecTo = 'showApplications'


@login_required(login_url="login")
def addApplications(request):
    if request.POST:
        form = ApplicationsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = ApplicationsForm()
    return render(request, 'products/applications/create.html', {'form': form, 'active': 'applications'})



@login_required(login_url="login")
def showApplications(request):
    items = ApplicationsModel.objects.all().order_by('-id')
    return render(request, 'products/applications/show.html', {'items': items, 'active': 'applications'})



@login_required(login_url="login")
def editApplications(request, id):
    data = ApplicationsModel.objects.get(id=id)
    if request.POST:
        form = ApplicationsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = ApplicationsForm(instance=data)
    return render(request, 'products/applications/create.html', {'form': form, 'active': 'applications', 'activity': 'edit'})


@login_required(login_url="login")
def deleteApplications(request, id):
    try:
        data = ApplicationsModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)