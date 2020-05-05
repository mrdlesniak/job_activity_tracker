from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Date, Application, Activity

# Create your views here.
def index(request):
    all_dates = Date.objects.order_by("date")
    all_applications = Application.objects.order_by("company_name")
    all_activities = Activity.objects.all()
    
    context = {
        "all_dates": all_dates,
        "all_applications": all_applications,
        "all_activities": all_activities
    }

    return render(request, 'unemployapp/index.html', context)