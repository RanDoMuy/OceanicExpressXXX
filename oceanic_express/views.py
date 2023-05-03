from django.shortcuts import render
from .models import user, package
# Create your views here.
def home(requests):
    #signup
    if requests.method== "POST":
    
        if 'fullname' in requests.POST:
            fullname= requests.POST['fullname']
            email= requests.POST['email']
            number= requests.POST['number']
            password= requests.POST['password']

            newuser= user(
                Fullname= fullname,
                Email= email, 
                Number= number,
                Password= password)
            newuser.save()

        elif 'tracking_id' in requests.POST:
            tracking_id= requests.POST['tracking_id']
            packageinfo= package.objects.get(Tracking_Id= tracking_id)
            return render(requests, "p_info.html", {"packageinfo": packageinfo})
        
    return render(requests, "index.html", {})
