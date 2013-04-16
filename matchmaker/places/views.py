"""Views of the ``places`` app."""
from django.conf import settings
from django.contrib.gis.utils import GeoIP
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, DetailView, ListView

from places.forms import PlaceCreateForm
from places.models import Place


def get_geoip_position(request):
    """Returns the user's position as a (lat, lng) tuple based on his IP."""
    result = (None, None)
    g = GeoIP()
    ip = (request.META.get('HTTP_X_FORWARDED_FOR')
          or request.META.get('REMOTE_ADDR'))
    result = g.lon_lat(ip)
    if result is None:
        ip = settings.SERVER_IP
        result = g.lon_lat(ip)
        if result is None:
            return None
    return (result[1], result[0])


class PlaceCreateView(CreateView):
    """Allows to create a new place."""
    form_class = PlaceCreateForm
    model = Place
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(PlaceCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user, })
        return kwargs

    def get_success_url(self):
        return self.object.get_absolute_url()


class PlaceDetailView(DetailView):
    """Allows to see details about a place."""
    model = Place


class PlaceListView(ListView):
    """Gets the user's geolocation and pulls nearby places via AJAX."""
    context_object_name = 'places'
    template_name = 'places/place_list.html'
    ajax_template_name = 'places/partials/place_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super(PlaceListView, self).dispatch(request, *args, **kwargs)

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.ajax_template_name, ]
        return [self.template_name, ]

    def get_queryset(self):
        if not self.request.GET.get('lat'):
            lat_lng = get_geoip_position(self.request)
            if not lat_lng:
                return None
        lat = self.request.GET.get('lat') or lat_lng[0]
        lng = self.request.GET.get('lng') or lat_lng[1]
        return Place.objects.get_nearby(5, lat, lng,)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
