from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from .views import (
    dashboard,
    editprofile,
    projects,
    fundingprofile,
    campaigns,
    createcampaign,
    campaignview, 
    campaignsettings,
    camp,
    pitch,
    faq,
    funding,
    rewards, 
    home,
    editprofile,
)

# Preload files

 
urlpatterns = [
    path('',home, name='home'),
    path('dashboard/editprofile/', editprofile.as_view(), name='editprofile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('projects/',projects, name='projects'),
    path('dashboard/fundingprofile/',fundingprofile, name='fundingprofile'),
    path('dashboard/yourcampaigns/',campaigns, name='campaigns'),
    path('createcampaign/',createcampaign, name='createcampaign'),
    path('campaignview/', campaignview, name='campaignview'),
    path('createcampaign/campaignsettings/', campaignsettings , name="campaignsettings"),
    path('createcampaign/campaignsettings/campaign/',camp, name='camp'),
    path("createcampaign/campaignsettings/pitch",pitch, name="pitch"),
    path('createcampaign/campaignsettings/funding/',funding,name='funding'),
    path('createcampaign/campaignsettings/rewards/', rewards, name='rewards'),
    path('createcampaign/campaignsettings/FAQ/',faq, name="faq"),
]
  






if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)