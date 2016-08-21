from django.shortcuts import render, get_object_or_404
from django.db.models.aggregates import Avg
from app import models


def sites(request):
    """
    The "home" page, with the list of sites.
    """
    context = {
        "sites": models.Site.objects.all()
    }
    return render(request, 'assignment/sites.html', context=context)


def site_page(request, id=None):
    """
    Individual site pages.
    """
    site = get_object_or_404(models.Site, pk=id)
    context = {
        "site": site,
        "entries": site.dataentry_set.all().order_by("date"),
    }
    return render(request, 'assignment/site_page.html', context=context)


def summary_sums(request):
    """
    Summary table with the sums of A and B values for each site.

    This view does the aggregation (join and sum operations) in python, which is
    generally less safe and efficient than a db-level query like in the other
    summary function.

    This view calculates sums in python, which is fine if for some reason
    it cannot be done in the database, and the dataset is small. For something
    bigger, numerical calculations could take advantage of something like NumPy
    or an ad hoc C library. Furthermore, all data entries will be read in
    memory, which could be a problem on a large dataset.

    On a more intricate or critical query, the query should be pulled in a utility
    function so it can be easily unit-tested.

    We check in test.py that we only query the database twice.
    """

    sites = models.Site.objects.all()
    entries = models.DataEntry.objects.all()

    rows = []

    for site in sites:
        entry_set = [e for e in entries if e.site_id == site.id]
        rows.append({
            'site': site.name,
            'a_value': sum(entry.a_value for entry in entry_set),
            'b_value': sum(entry.b_value for entry in entry_set),
        })

    context = {"rows": rows}
    return render(request, 'assignment/summary.html', context=context)


def summary_averages(request):
    """
    Summary table with the average values of A and B for each site.

    This view aggregates the data at the database level. A print(qs).query in the
    interactive shell shows that the query simplifies to an efficient
    JOIN.
    """

    rows = [{
        'site': site.name,
        'a_value': site.a_vals_avg,
        'b_value': site.b_vals_avg,
    } for site in models.Site.objects.all().annotate(
            a_vals_avg=Avg('dataentry__a_value'),
            b_vals_avg=Avg('dataentry__b_value'))]

    context = {"rows": rows}
    return render(request, 'assignment/summary.html', context=context)
