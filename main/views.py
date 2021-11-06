from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from accounts.forms import Profileform, UserForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, ProcessFormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from accounts.forms import Profileform, UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Campaign
# Create your views here.


def projects(request):
    campaigns = Campaign.objects.filter(is_complete=True)
    return render(request, "projects.html", {"campaigns": campaigns})


@login_required
def dashboard(request):
    campaigns = Campaign.objects.filter(owner=request.user)
    number_of_campaigns = len(campaigns)
    obj = get_object_or_404(Profile, user1=request.user)
    print(obj.facebook)
    firstname = request.user.first_name
    lastname = request.user.last_name
    email = request.user.email
    user = request.user
    return render(request, "dashboard.html", {'firstname': firstname, 'lastname': lastname, 'email': email, 'user': user, 'profile': obj, "number": number_of_campaigns})


@login_required
def editprofile(request):
    obj = get_object_or_404(Profile, user1=request.user)
    print(obj.__dict__)
    profile_form = Profileform(obj.__dict__)
    if request.method == "POST":
        profile_form = Profileform(request.POST, request.FILES, instance=obj)
        if profile_form.is_valid():
            obj.profileimg = profile_form.cleaned_data['profileimg']
            obj.bio = profile_form.cleaned_data['bio']
            obj.country = profile_form.cleaned_data['country']
            obj.website = profile_form.cleaned_data['website']
            obj.istagram = profile_form.cleaned_data['istagram']
            obj.facebook = profile_form.cleaned_data['facebook']
            obj.linkedin = profile_form.cleaned_data['linkedin']
            obj.twitter = profile_form.cleaned_data['twitter']
            obj.save()
            print(obj.bio)
        return redirect("editprofile")
    return render(request, "editprofile.html", {"form": profile_form, "profile": obj})


def home(request):
    return render(request, "home.html")


@login_required
def fundingprofile(request):
    return render(request, "fundingprofile.html")


@login_required
def campaigns(request):
    campaigns = Campaign.objects.filter(owner=request.user)
    return render(request, 'campaign.html', {"campaigns": campaigns})


@login_required
def createcampaign(request):
    return render(request, "campaign/createcampaign.html")


@login_required
def campaignview(request):
    return render(request, 'campaign/campaignview.html')


@login_required
def campaignsettings(request):
    firstname = request.user.first_name
    lastname = request.user.last_name
    email = request.user.email
    campID = 1
    if request.method == "POST":
        print(request.POST)
        campaign = Campaign.objects.create(
            owner=request.user,
            fullname=request.POST['fullname'],
            websiteURL=request.POST['weburl'],
            country=request.POST['country'],
            address=request.POST['address'],
            city=request.POST['city'],
            zipcode=request.POST['zipcode']
        )
        campID = campaign.id
        campaign.save()
        return redirect("camp", id=campaign.id)
    return render(request, "campaign/settings/basicinfo.html", {'email': email, 'firstname': firstname, 'lastname': lastname, 'campaign': campID})


@login_required
def camp(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    if request.method == "POST" and request.user == campaign.owner:
        campaign.campaignName = request.POST['campname']
        campaign.campaignTagline = request.POST['camptag']
        campaign.category = request.POST['category']
        campaign.startdate = request.POST['startdate']
        campaign.enddate = request.POST['enddate']
        campaign.save()
        return redirect("pitch", id=id)
    return render(request, "campaign/settings/camp.html", {"campaign": campaign})


@login_required
def pitch(request, id):
    campaign = Campaign.objects.get(id=id)
    if request.method == "POST" and request.user == campaign.owner:
        campaign.pitchCampaignName = request.POST['pitchCampName']
        campaign.pitchFile = request.FILES['profileimage']
        campaign.vidlink = request.POST['vidurl']
        campaign.campaignPitch = request.POST['campaignPitch']
        campaign.save()
        return redirect("funding", id=id)
    return render(request, "campaign/settings/pitch.html", {"campaign": campaign})


@login_required
def rewards(request, id):
    campaign = Campaign.objects.get(id=id)
    if request.method == "POST" and request.user == campaign.owner:
        campaign.price = request.POST['price']
        campaign.title = request.POST['title']
        campaign.rewardfile = request.FILES['file']
        campaign.shippingInfo = request.POST['shipinfo']
        campaign.rewarddetails = request.POST['rewarddetails']
        campaign.deliveryTime = request.POST['date']
        campaign.save()
        return redirect("faq", id=id)
    return render(request, "campaign/settings/rewards.html", {"campaign": campaign})


@login_required
def faq(request, id):
    campaign = Campaign.objects.get(id=id)
    if request.method == "POST" and request.user == campaign.owner:
        campaign.faqs = request.POST['faq']
        campaign.save()
        return redirect("campaigns")
    return render(request, "campaign/settings/FAQ.html", {"campaign": campaign})


@login_required
def funding(request, id):
    campaign = Campaign.objects.get(id=id)
    if request.method == "POST" and request.user == campaign.owner:
        campaign.campaignGoal = request.POST['goal']
        campaign.save()
        return redirect("rewards", id=id)
    return render(request, "campaign/settings/funding.html", {"campaign": campaign})

@login_required
def updateUser(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get("fullname")
        user.email = request.POST.get("email")
        user.save()
    return redirect("editprofile")

@login_required
def updateCampaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    if request.method == "POST":
        return redirect("campaigns")
    return render(request, "updateCampaign.html",{"campaign":campaign})

@login_required
def deleteCampaign(request,id):
    campaign = get_object_or_404(Campaign, id=id)
    campaign.delete()
    return redirect("campaigns")