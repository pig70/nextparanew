from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                  path('stories/<slug:slug>/<int:pk>/', views.story, name='story'),
                  path('', views.home, name='home'),
                  path('registration/register/', views.register, name='register'),
                  path('registration/registration-complete/', views.register_complete, name='registration_complete'),
                  path('all-paragraphs/', views.all_paragraphs, name='all_paragraphs'),
                  path('start-a-story/', views.start_a_story, name='start_story'),
                  path('registration/edit/', views.edit_profile, name='edit_profile'),
                  re_path(r'^stories/<slug:slug>/<int:pk>/like/', views.like_story, name='like_story')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
