from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import AboutForm, ContactDetailForm, HomeModelForm, CompanyModelForm, AgricultureLubricantsForm
from ..models import AboutModel, ContactDetailModel, GetInTouchModel, QueryModel, HomeModel, CompanyModel, AgricultureLubricantsModel
redirecTo = 'showAbout'


# For Home page Content
def getHomeContent():
    if home_details:= HomeModel.objects.all():
        data = HomeModel.objects.all().order_by("-id")[:1][0]
    else:
        data = None

    return data


@login_required(login_url="login")
def homeContentData(request):
    data = getHomeContent()
    if request.POST:
        form = HomeModelForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form = HomeModelForm(instance=data)
    return render(request, 'lube/home_content/show.html', {'form': form, 'active': 'home_content'})



# For Company details setting
def getCompanyDetails():
    if home_details:= CompanyModel.objects.all():
        data = CompanyModel.objects.all().order_by("-id")[:1][0]
    else:
        data = None

    return data


@login_required(login_url="login")
def companyDetailsData(request):
    data = getCompanyDetails()
    if request.POST:
        form = CompanyModelForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form = CompanyModelForm(instance=data)
    return render(request, 'lube/company_details/show.html', {'form': form, 'active': 'company_details'})




# for about us details
def getAbout():
    if about_details:= AboutModel.objects.all():
        data = AboutModel.objects.all().order_by("-id")[:1][0]
    else:
        data = None

    return data

@login_required(login_url="login")
def aboutData(request):
    data = getAbout()
    if request.POST:
        form = AboutForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form = AboutForm(instance=data)

    return render(request, 'lube/about_us/show.html', {'form': form, 'active': 'about'})



# for agriculture lubricants
def getAgricultureLubricants():
    if details:= AgricultureLubricantsModel.objects.all():
        data = AgricultureLubricantsModel.objects.all().order_by("-id")[:1][0]
    else:
        data = None

    return data


@login_required(login_url="login")
def agricultureLubricantsData(request):
    data = getAgricultureLubricants()
    if request.POST:
        form = AgricultureLubricantsForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form = AgricultureLubricantsForm(instance=data)

    return render(request, 'lube/agriculture_lubricants/show.html', {'form': form, 'active': 'agriculture_lubricants'})



# For contact details
def getContactDetails():
    if contact_details:= ContactDetailModel.objects.all():
        data = ContactDetailModel.objects.all().order_by("-id")[:1][0]
    else:
        data = None

    return data

@login_required(login_url="login")
def contactDetails(request):
    data = getContactDetails()
    if request.POST:
        form = ContactDetailForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
    else:
        form = ContactDetailForm(instance=data)

    return render(request, 'lube/contact_details/show.html', {'form': form, 'active': 'contact_details'})



# For Get In Touch
@login_required(login_url="login")
def showGetInTouch(request):
    data = GetInTouchModel.objects.all().order_by('-id')
    return render(request, 'lube/getintouch/show.html', {'items': data, 'active': 'getintouch'})

@login_required(login_url="login")
def markRead(request, id):
    data = GetInTouchModel.objects.get(id=id)
    data.is_read = True
    data.save()
    return redirect('showGetInTouch')


# For Query
@login_required(login_url="login")
def showQuery(request):
    data = QueryModel.objects.all().order_by('-id')
    return render(request, 'lube/query/show.html', {'items': data, 'active': 'query'})

@login_required(login_url="login")
def markReadQuery(request, id):
    data = QueryModel.objects.get(id=id)
    data.is_read = True
    data.save()
    return redirect("showQuery")