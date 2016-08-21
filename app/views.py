from django.shortcuts import render, get_object_or_404
from app import models


def sites(request):
    context = {
        "sites": models.Site.objects.all()
    }
    return render(request, 'assignment/sites.html', context=context)


def site_page(request, id=None):
    site = get_object_or_404(models.Site, pk=id)
    context = {
        "site": site,
        "entries": site.dataentry_set.all().order_by("date"),
    }
    return render(request, 'assignment/site_page.html', context=context)


def summary_sums(request):
    return render(request, 'assignment/summary.html')


def summary_averages(request):
    return render(request, 'assignment/summary.html')
