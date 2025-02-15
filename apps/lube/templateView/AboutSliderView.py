from django.shortcuts import render, redirect
from ..forms import AboutSliderForm
from django.contrib.auth.decorators import login_required
from ..models import AboutSliderModel
redirecTo = 'showAboutSlider'

@login_required(login_url="login")
def addAboutSlider(request):
    if request.POST:
        form = AboutSliderForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = AboutSliderForm()
    return render(request, 'lube/about_slider/create.html', {'form': form, 'active': 'about_slider'})


@login_required(login_url="login")
def showAboutSlider(request):
    items = AboutSliderModel.objects.all().order_by('-id')
    return render(request, 'lube/about_slider/show.html', {'items': items, 'active': 'about_slider'})

@login_required(login_url="login")
def editAboutSlider(request, id):
    data = AboutSliderModel.objects.get(id=id)
    if request.POST:
        form = AboutSliderForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = AboutSliderForm(instance=data)
    return render(request, 'lube/about_slider/create.html', {'form': form, 'active': 'about_slider', 'activity': 'edit'})

@login_required(login_url="login")
def deleteAboutSlider(request, id):
    try:
        data = AboutSliderModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)