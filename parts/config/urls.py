import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/',
         include('parts.app.accounts.urls')
         ),
    path('accounts/',
        include('django.contrib.auth.urls')
        ),
    path('__debug__', include(debug_toolbar.urls))

]

