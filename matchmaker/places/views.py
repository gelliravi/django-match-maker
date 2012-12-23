"""Views of the ``places`` app."""
from django.views.generic import CreateView

from places.forms import CreatePlaceForm
from places.models import Place


class CreatePlaceView(CreateView):
    form_class = CreatePlaceForm
    model = Place
    success_url = '/'
