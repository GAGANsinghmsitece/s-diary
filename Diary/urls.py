from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Diary import settings

urlpatterns = [
    path('admin/saporainc./GAGAN/admin/saporainc.', admin.site.urls),
    path('',include('CreateDiary.urls')),
]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

