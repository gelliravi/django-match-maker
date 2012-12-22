"""Views of the ``matchmaker`` project."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'matchmaker/home.html'
