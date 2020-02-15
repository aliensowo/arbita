from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index_site, name="index_site"),
    path("fb-account", views.site1_1, name="site1_1"),
    path("offers", views.site1_6, name="site1_6"),
    path("rekl", views.site1_7, name="site1_7"),
    path("promo", views.site1_8, name="site1_8"),
    path("rab-svyazki", views.site1_9, name="site1_9"),
    path("soft-creo", views.site1_10, name="site1_10"),
    path("anti-dect", views.site1_11, name="site1_11"),
    path("soft-clear", views.site1_12, name="site1_12"),
    path("private-pp", views.site1_13, name="site1_13"),
    path("agency", views.site1_15, name="site1_15"),
    path("consultacia", views.site1_16, name="site1_16"),
]