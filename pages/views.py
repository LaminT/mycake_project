from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, city_choices, title_choices

from listings.models import Listing
from bakers.models import Baker


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    context = {
        'listings': listings,
        'city_choices': city_choices,
        'price_choices': price_choices,
        'title_choices': title_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get alle bakers
    bakers = Baker.objects.order_by('-hire_date')

    # Get MVP
    mvp_bakers = Baker.objects.all().filter(is_mvp=True)

    context = {
        'bakers': bakers,
        'mvp_bakers': mvp_bakers
    }
    return render(request, 'pages/about.html', context)
