from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls import url
# from django.urls import path
# from rest_framework_simplejwt import views as jwt_views


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    
    # path("ifsc", hello.views.ifsc, name="ifsc"),
    # path("bank_name_city", hello.views.bank_name_city, name="bank_name_city"),
    path("admin/", admin.site.urls),

    url(r'^api-token-auth/', obtain_jwt_token),
    
    
    path('bank_name_city', hello.views.bank_name_city_view.as_view(), name='bank_name_city_view'),
    path('ifsc', hello.views.ifsc_view.as_view(), name='ifsc_view'),
    
    
    
]
