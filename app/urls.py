from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    
    url('^api/subjects/$', views.CourseList.as_view()), # list of subjects
    url('^api/subjects/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()), # single subject
    url('^api/notes/$', views.NoteList.as_view()), # list of notes
    url('^api/notes/(?P<pk>[0-9]+)/$', views.NoteDetail.as_view()), # single note
    url('^api/profiles/$', views.ProfileList.as_view()), # list of profiles
    url('^api/profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()), # single profile
    url('^api/users/$', views.UserList.as_view()), # list of users
    url('^api/users/create/$', views.UserCreate.as_view()), # create user
    url('^api/auth/login/$', views.loginUser.as_view()), # login user
    url('^api/auth/logout/$', views.logoutUser.as_view()), # logout user
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)