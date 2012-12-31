"""Views of the ``matchmaker`` project."""
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from places.models import Place
from places.views import PlaceListView


class HomeView(TemplateView):
    template_name = 'matchmaker/home.html'


class CustomPlaceListView(PlaceListView):
    """
    PlaceListView with extra functionality needed by the matchmaker project.

    """
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.filter = getattr(request, request.method).get('filter', 'nearby')
        if not self.filter:
            self.filter = 'nearby'
        return super(CustomPlaceListView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PlaceListView, self).get_context_data(**kwargs)
        ctx.update({'filter': self.filter, })
        return ctx

    def get_queryset(self):
        if not self.request.POST.get('lat'):
            return None

        lat = self.request.POST.get('lat')
        lng = self.request.POST.get('lng')
        if self.filter == 'nearby':
            return Place.objects.get_nearby(5, lat, lng).order_by('distance')
        if self.filter == 'active':
            return Place.objects.get_active()
        if self.filter == 'all':
            return Place.objects.get_distance(lat, lng).order_by('distance')
