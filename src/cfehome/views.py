from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits

def home_page_view(request):
    queryset = PageVisits.objects.all()
    PageVisits.objects.create()
    return render(request, "home.html", { "page_title": "My Page", "queryset": queryset })