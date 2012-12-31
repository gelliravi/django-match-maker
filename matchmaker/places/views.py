"""Views of the ``places`` app."""
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView

from places.forms import PlaceCreateForm
from places.models import Place


class PlaceCreateView(CreateView):
    """Allows to create a new place."""
    form_class = PlaceCreateForm
    model = Place
    success_url = '/'


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
        if not self.request.POST.get('lat'):
            return None
        return Place.objects.get_nearby(
            5, self.request.POST.get('lat'), self.request.POST.get('lng'),)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
