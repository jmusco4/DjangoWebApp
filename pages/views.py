from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from leads.models import Lead
# Create your views here.

def home_view(request, *args, **kwargs):
    print(request.user)
    count_leads = []
    lead_info = Lead.objects.all()
    for info in lead_info.values():
        count_leads.append(info["firstname"])
    number_of_leads = len(count_leads)
    date = datetime.today()
    date_time = date.strftime("%m-%d-%Y")
    return render(request,"home.html", {"today": date_time, "number_of_leads":number_of_leads})

def about_view(request, *args, **kwargs):
    my_context = {"my_text":"User Profile",
                  "my_number":"To Do List",
                  "my_list":["Topic 1 - Leasing", "Topic 2 - Analytics", "Topic 3 - Marketing", "Topic 4 - Leads"]}
    return render(request,"about.html", my_context)

