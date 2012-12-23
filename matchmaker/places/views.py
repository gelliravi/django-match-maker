"""Views of the ``places`` app."""
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView

from places.forms import CreatePlaceForm
from places.models import Place


class CreatePlaceView(CreateView):
    """Allows to create a new place."""
    form_class = CreatePlaceForm
    model = Place
    success_url = '/'


class PlaceListView(TemplateView):
    """Gets the user's geolocation and pulls nearby places via AJAX."""
    template_name = 'places/place_list.html'
    ajax_template_name = 'places/partials/place_list.html'

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super(PlaceListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PlaceListView, self).get_context_data(**kwargs)
        if self.request.POST.get('lat'):
            pnt = Point(
                float(self.request.POST.get('lng')),
                float(self.request.POST.get('lat')),)
            places = Place.objects.filter(
                point__distance_lte=(pnt, D(km=2))).distance(pnt).order_by(
                    'distance')
            ctx.update({
                'places': places,
            })
        return ctx

    def get_template_names(self):
        if self.request.is_ajax():
            return [self.ajax_template_name, ]
        return [self.template_name, ]

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
