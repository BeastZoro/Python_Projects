from django.shortcuts import render
from listing.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[0:]
    return render(request, 'pages/index.html', {'listings' : listings})

def about(request):
    #Retrieve all Realtors from DB
    realtors = Realtor.objects.order_by('-hire_date')
    pro_realtor = Realtor.objects.all().filter(is_mvp = True)

    context = {
        'realtors' : realtors,
        'pro_realtor' : pro_realtor
    }

    return render(request, 'pages/about.html', context)
