from django.contrib import admin
from django.urls import  path
from tiny_url import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.url_shortner_view, name="short_url"),
    path("how-it-works", views.how_it_works, name="how_it_works"),
    path("about-us", views.about_us, name="about_us"),
    path("<str:short_code>/", views.get_shortened_url, name="get_short_url"),
]
