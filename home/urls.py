
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from home import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('home.urls'))
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('orderMeals', views.orderMeals, name='orderMeals'),
   path('buyGrocerries', views.buyGrocerries, name='buyGrocerries'),
   path('orderMeals/search/', views.search, name='search'),
   path('buyGrocerries/<str:dynamic>', views.Details, name='Details'),
   path('orderMeals/<str:dynamic>', views.Details, name='Details'),
   re_path(r'^media/(?P<path>.*)$',serve, {'document_root':settings.MEDIA_ROOT}),
   
]

