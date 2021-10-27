from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    # api
    url('^api/subjects/$', views.SubjectList.as_view()), 
    url('^api/subjects/(?P<pk>[0-9]+)/$', views.SubjectDetail.as_view()), 
    url('^api/notes/$', views.NotesList.as_view()), 
    url('^api/notes/(?P<pk>[0-9]+)/$', views.NotesDetail.as_view()), 
    url('^api/profiles/$', views.ProfileList.as_view()), 
    url('^api/profiles/(?P<pk>[0-9]+)/$', views.ProfileDetail.as_view()), 
    url('^api/users/$', views.UserList.as_view()), 
    url('^api/users/create/$', views.UserCreate.as_view()), 
    url('^api/auth/login/$', views.loginUser.as_view()), 
    url('^api/auth/logout/$', views.logoutUser.as_view()), 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)