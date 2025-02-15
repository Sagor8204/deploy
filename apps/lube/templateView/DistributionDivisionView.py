from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import DistributionDivisionForm
from ..models import DistributionDivisionModel
redirecTo = 'showDivision'


@login_required(login_url="login")
def addDivision(request):
    if request.POST:
        form = DistributionDivisionForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = DistributionDivisionForm()
    return render(request, 'lube/division/create.html', {'form': form, 'active': 'division'})



@login_required(login_url="login")
def showDivision(request):
    items = DistributionDivisionModel.objects.all().order_by('-id')
    return render(request, 'lube/division/show.html', {'items': items, 'active': 'division'})



@login_required(login_url="login")
def editDivision(request, id):
    data = DistributionDivisionModel.objects.get(id=id)
    if request.POST:
        form = DistributionDivisionForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = DistributionDivisionForm(instance=data)
    return render(request, 'lube/division/create.html', {'form': form, 'active': 'division', 'activity': 'edit'})


@login_required(login_url="login")
def deleteDivision(request, id):
    try:
        data = DistributionDivisionModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)