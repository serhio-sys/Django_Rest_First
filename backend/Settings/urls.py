from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework import routers
from Core.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = routers.DefaultRouter().urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path("Contacts/",UserContactsViewSets.as_view({'get':'list','post':'createcontact'})),
    path("Contacts/<pk>/",UserContactsViewSets.as_view({'get':'retrieve','put':'update','patch':'partial_update'})),
    path("Contacts-images/",UserContactsViewSets.as_view({'get':'images'})),
    path("Contacts/<str:pk>/user/",UserContactsViewSets.as_view({'get':'user'})),
    #path("Contacts/",ContactAPIView.as_view()),
    #path("Contact/<pk>/",ModernDetailAPIUpdate.as_view()),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/t-auth/', include('djoser.urls')),          # djoser
    re_path(r'^t-auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
