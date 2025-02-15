from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import OurExpertsForm
from ..models import OurExpertsModel
redirecTo = 'showOurExperts'


@login_required(login_url="login")
def addOurExperts(request):
    if request.POST:
        form = OurExpertsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = OurExpertsForm()
    return render(request, 'lube/our_expert/create.html', {'form': form, 'active': 'our_experts'})


@login_required(login_url="login")
def showOurExperts(request):
    items = OurExpertsModel.objects.all().order_by('-id')
    return render(request, 'lube/our_expert/show.html', {'items': items, 'active': 'our_experts'})


@login_required(login_url="login")
def editOurExperts(request, id):
    data = OurExpertsModel.objects.get(id=id)
    if request.POST:
        form = OurExpertsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = OurExpertsForm(instance=data)
    return render(request, 'lube/our_expert/create.html', {'form': form, 'active': 'our_experts', 'activity': 'edit'})

@login_required(login_url="login")
def deleteOurExperts(request, id):
    try:
        data = OurExpertsModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)