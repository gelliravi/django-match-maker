"""Views for the ``checkins`` app."""
from django.views.generic import FormView
from django.http import Http404

from checkins.forms import CheckinCreateForm
from places.models import Place


class CheckinCreateView(FormView):
    """Allows a user to checkin at a place."""
    form_class = CheckinCreateForm
    template_name = 'checkins/checkin_form.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.place = Place.objects.get(pk=kwargs.get('place_pk'))
        except Place.DoesNotExist:
            raise Http404
        return super(CheckinCreateView, self).dispatch(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(CheckinCreateView, self).get_context_data(**kwargs)
        ctx.update({
            'place': self.place,
        })
        return ctx

    def get_form_kwargs(self):
        kwargs = super(CheckinCreateView, self).get_form_kwargs()
        if self.request.user:
            kwargs.update({'user': self.request.user, })
        kwargs.update({'place': self.place, })
        return kwargs
