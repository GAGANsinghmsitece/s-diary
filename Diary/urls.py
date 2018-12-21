from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Diary import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/saporainc./GAGAN/admin/saporainc.', admin.site.urls),
    path('',include('CreateDiary.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

