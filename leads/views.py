from django.shortcuts import render
from .models import Lead
from datetime import datetime
TODAY = datetime.today()

def lead_create_view(request):
    context={}
    leads_ref = Lead.objects.all()
    email_list = []
    phone_list = []
    if request.method == 'POST':
        if request.POST.get("DeleteLead"):
            Lead.objects.get(pk=request.POST['delete-id']).delete()
        else:
            if leads_ref:
                for info in leads_ref.values():
                    phone_number = info["phone_num"]
                    email = info["email"]
                    email_list.append(email)
                    phone_list.append(phone_number)
            if request.POST['email'] in email_list:
                print("Stop")
            else:
                obj = Lead.objects.create(firstname=request.POST['first_name'], lastname=request.POST['last_name'], phone_num=request.POST['phone_num'],
                                      email=request.POST['email'], birthday=TODAY)
    leads_ref = Lead.objects.all()
    if leads_ref:
        context["leads_ref"] = leads_ref
        context["created_on"] = TODAY
    else:
        context = {}
    return render(request, "leads/leads.html", context)

def add_lead_view(request):
    context={}
    leads_ref = Lead.objects.all()
    email_list = []
    phone_list = []
    if request.method == 'POST':
        context["post_success"] = False
        for info in leads_ref.values():
            phone_number = info["phone_num"]
            email = info["email"]
            email_list.append(email)
            phone_list.append(phone_number)
        if request.POST['email'] in email_list:
            context["email_found"] = True
        else:
            obj = Lead.objects.create(firstname=request.POST['first_name'], lastname=request.POST['last_name'], phone_num=request.POST['phone_num'],
                                        email=request.POST['email'], birthday=TODAY)
            context["post_success"] = True
    leads_ref = Lead.objects.all()
    if leads_ref:
        context["leads_ref"] = leads_ref
        context["created_on"] = TODAY
    else:
        context = {}
    return render(request, "leads/add_lead.html", context)
