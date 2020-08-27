from django.shortcuts import render

# Create your views here.
from .forms import UserForm

def projfin(request,area,latitude,longitude):
     useage = 14612.445542070016+area*1.96406582 + latitude*(-557.54615103) +longitude*183.09409243
     return int(useage)

def index(request):
    submitbutton= request.POST.get("submit")
    noofbedrooms=0
    noofbathrooms=0
    furnishing=''
    tenants=''
    area=0
    latitude=0
    longitude=0
    if request.method=='POST':
        form= UserForm(request.POST)
        if form.is_valid():
            noofbedrooms= form.cleaned_data.get("noofbedrooms")
            noofbathrooms= form.cleaned_data.get("noofbathrooms")
            furnishing= form.cleaned_data.get("furnishing")
            tenants=form.cleaned_data.get("tenants")
            area=form.cleaned_data.get("area")
            latitude=form.cleaned_data.get("latitude")
            longitude=form.cleaned_data.get("longitude")
            #price=projfin(request,area,latitude,longitude)
            #price=14612.445542070016+form.cleaned_data["area"]*1.96406582 +form.cleaned_data["latitude"]*(-557.54615103) +form.cleaned_data["longitude"]*183.09409243
    else:
        form=UserForm()
    price=0
    price=14612.445542070016+area*1.96406582 + latitude*(-557.54615103) +longitude*183.09409243
    cost=int(price)
    context= {'form': form, 'noofbedrooms': noofbedrooms, 'noofbathrooms':noofbathrooms,'submitbutton': submitbutton, 'furnishing':furnishing,'tenants':tenants,'area':area,'latitude':latitude,'longitude':longitude,'cost':cost}

    return render(request, 'app/index.html', context)
