from django.shortcuts import render


def dummy_view(request):
    return render(request, "assignment/dummy.html")
