from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import NewsAndEventsForm
from ..models import NewsAndEventsModel
redirecTo = 'showNewsEvents'


@login_required(login_url="login")
def addNewsEvents(request):
    if request.POST:
        form = NewsAndEventsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()

            return redirect(redirecTo)
    else:
        form = NewsAndEventsForm()
    return render(request, 'lube/news_events/create.html', {'form': form, 'active': 'news_events'})



@login_required(login_url="login")
def showNewsEvents(request):
    items = NewsAndEventsModel.objects.all().order_by('-id')
    return render(request, 'lube/news_events/show.html', {'items': items, 'active': 'news_events'})



@login_required(login_url="login")
def editNewsEvents(request, id):
    data = NewsAndEventsModel.objects.get(id=id)
    if request.POST:
        form = NewsAndEventsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            
            data.save()
            return redirect(redirecTo)

    else:
        form = NewsAndEventsForm(instance=data)
    return render(request, 'lube/news_events/create.html', {'form': form, 'active': 'news_events', 'activity': 'edit'})


@login_required(login_url="login")
def deleteNewsEvents(request, id):
    try:
        data = NewsAndEventsModel.objects.get(id=id)
        data.delete()
    except:
        pass
    return redirect(redirecTo)