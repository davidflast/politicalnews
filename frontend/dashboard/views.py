from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
	template_name = "simple.html"


class DashBoardView(TemplateView):
	template_name = "dashboard/dashboard.html"