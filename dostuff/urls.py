from . import views
from django.urls import path


urlpatterns = [
path('api/events', views.events_list, name='events_list'),
path('api/addevent', views.user_add_event, name='user_add_event'),
path('api/deleteevent', views.user_delete_event, name='user_delete_event'),
path('api/register', views.create_user, name='create_user'),
path('api/edituser', views.edit_user, name='edit_user'),
path('api/deleteuser', views.delete_user, name='delete_user'),
path('api/dostuff-categories-need-added', views.populate_categories, name='populate_categories'),
path('api/login', views.log_user_in, name='login'),
path('api/logout', views.logout_view, name='logout'),
path('api/authentication-error', views.not_logged_in, name='not_logged_in'),
path('api/testing', views.testing, name='testing'),
  # path('api/event/', views.EventList.as_view(), name='event-list'),
  # path('api/event/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
]

## COMBINE URLS WITH LOCALHOST:8000 TO MAKE API CALLS!!!!!!!!!!!!