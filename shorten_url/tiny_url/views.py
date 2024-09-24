from django.shortcuts import render, HttpResponseRedirect
from .form import URLForm
from .models import ShortUrl
# Create your views here.


def url_shortner_view(request):
    """
    create user url shortner
    """
    if request.method == 'POST':
        long_url = request.POST.get('long_url', '')

        # Validate URL
        validate = URLForm(request.POST)
        if validate.is_valid():

            url_shortened = ShortUrl.objects.create(orig_url=long_url)
            url_shortened.save()
            short_url = request.build_absolute_uri(url_shortened.short_url)
        else:
            ...
        # Generate the full short URL
        return render(request, 'url_form.html', {'short_url': short_url})
    return render(request, 'url_form.html')


def get_shortened_url(request, short_code):
    """
    A get request to get user shortened url
    """
    if request.method == "POST":
        ...

    short_url = ShortUrl.objects.filter(short_url=short_code).first()
    if not short_url:
        return render(request, "404.html")

    return HttpResponseRedirect(short_url.orig_url)

def how_it_works(request):
    """
    return the how it's works template for shortnerpro
    """
    return render(request, "how_it_works.html")


def about_us(request):
    """
    page about us for user
    """
    return render(request, "about.html")
