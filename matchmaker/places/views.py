"""Views of the ``places`` app."""
from django.views.generic import CreateView

from places.models import Place


class CreatePlaceView(CreateView):
    model = Place
