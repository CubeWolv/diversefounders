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
    updateUser,
    updateCampaign,
    deleteCampaign,
    campaignviewprivate,
    home,
    startups,
    startupsinvestorprofile,
    startupsstartupprofile,
    investors,
)

# Preload files


urlpatterns = [
    path('', home, name='home'), 
    path('dashboard/editprofile/',
         editprofile, name='editprofile'),
    path('dashboard/', dashboard, name='dashboard'),
    path('projects/', projects, name='projects'),
    path('dashboard/fundingprofile/', fundingprofile, name='fundingprofile'),
    path('dashboard/yourcampaigns/', campaigns, name='campaigns'),
    path('createcampaign/', createcampaign, name='createcampaign'),
    path('campaignview/', campaignview, name='campaignview'),
    path('createcampaign/campaignsettings/',
         campaignsettings, name="campaignsettings"),
    path('createcampaign/campaignsettings/campaign/<id>/', camp, name='camp'),
    path("createcampaign/campaignsettings/pitch/<id>/", pitch, name="pitch"),
    path('createcampaign/campaignsettings/funding/<id>/', funding, name='funding'),
    path('createcampaign/campaignsettings/rewards/<id>/', rewards, name='rewards'),
    path('createcampaign/campaignsettings/FAQ/<id>/', faq, name="faq"),
    path('updateUser/',updateUser,name="update-user"),
    path('updateCampaign/<id>/',updateCampaign, name="campign-update"),
    path('delete/<id>/',deleteCampaign, name="delete"),
    path('dashboard/yourcampaigns/<id>/',campaignviewprivate, name='campaignviewprivate'),
    path('startups/createinvestorprofile/',startupsinvestorprofile, name="startupsinvestorprofile"),
    path('startups/createstartupprofile/',startupsstartupprofile,name="startupsstartupprofile"),
    path('startups/',startups, name='startups'),
    path('startups/investors/',investors, name="investors"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
