from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request):
    return about_view(request)


def about_view(request):
    qs = PageVisits.objects.all()
    page_qs = PageVisits.objects.filter(path=request.path)
    try:
        percent = (page_qs.count() * 100) / qs.count()
    except:
        percent = 0
    mytitle = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": mytitle,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    PageVisits.objects.create(path=request.path)
    return render(request, html_template, my_context)