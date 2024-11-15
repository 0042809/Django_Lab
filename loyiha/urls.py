
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('account/', include('django.contrib.auth.urls')),
    path ('account/', include('account.urls')),
        path('',include('news.urls'))
]