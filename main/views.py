from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from accounts.forms import Profileform, UserForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, ProcessFormView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from accounts.forms import Profileform,UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



def projects(request):
    return render(request,"projects.html")

@login_required
def dashboard(request):
    firstname = request.user.first_name
    lastname=request.user.last_name
    email=request.user.email
    return render(request, "dashboard.html",{'firstname': firstname,'lastname':lastname ,'email':email,})









 













class editprofile(LoginRequiredMixin, TemplateView):
    user_form = UserForm 
    profile_form = Profileform
    template_name = "Profiles/editprofile.html"

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None
        
       
        user_form = UserForm(post_data, instance=request.user)
        profile_form =Profileform(post_data, file_data, instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
























def home(request):
    return render(request, "home.html")



@login_required
def fundingprofile(request):
    return render(request , "profiles/fundingprofile.html")

@login_required
def campaigns(request):
    return render(request, 'profiles/campaign.html')

@login_required  
def createcampaign(request):
    return render(request, "campaign/createcampaign.html")

@login_required
def campaignview(request):
    return render(request, 'campaign/campaignview.html')

@login_required
def campaignsettings(request):
    firstname = request.user.first_name
    lastname=request.user.last_name
    email=request.user.email
    return render(request, "campaign/settings/basicinfo.html" ,{'email':email ,'firstname':firstname ,'lastname':lastname})

@login_required
def camp(request):
    return render(request, "campaign/settings/camp.html")

@login_required
def pitch(request):
    return render(request, "campaign/settings/pitch.html")

@login_required
def rewards(request):
    return render(request, "campaign/settings/content.html")
    
@login_required
def faq(request):
    return render(request, "campaign/settings/FAQ.html")

@login_required
def funding(request):
    return render(request, "campaign/settings/funding.html")