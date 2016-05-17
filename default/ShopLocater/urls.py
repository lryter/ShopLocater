from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^login/$',  views.Login), 
    url(r'^logout/$',  views.Logout), 
    url(r'^home/$',  views.Home), 
    url(r'^blog/$',  views.Blog), 
    url(r'^(?P<id>\d+)/$',  views.Detail,  name='Detail'), 
    
]

urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
