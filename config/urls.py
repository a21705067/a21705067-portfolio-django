
from django.contrib import admin
from django.urls import path, include
from portfolio import views

app_name = "portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls'))
]
