from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import WatcherCountRedirect

urlpatterns = [

                  path('stories/<slug:slug>/<int:pk>/', views.story, name='story'),
                  path('stories/<slug:slug>/<int:pk>/watch/', WatcherCountRedirect.as_view(), name='watch'),
                  path('', views.home, name='home'),
                  path('registration/register/', views.register, name='register'),
                  path('registration/registration-complete/', views.register_complete, name='registration_complete'),
                  path('all-paragraphs/', views.all_paragraphs, name='all_paragraphs'),
                  path('start-a-story/', views.start_a_story, name='start_story'),
                  path('registration/edit/', views.edit_profile, name='edit_profile')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
