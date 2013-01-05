"""Views for the ``checkins`` app."""
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from checkins.forms import (
    CheckinCreateForm,
    CheckinMassCreateForm,
    CheckoutForm
)
from places.models import Place


class CheckinCreateViewMixin(object):
    """Common things for checkin create views."""
    success_url = '/places/'

    def dispatch(self, request, *args, **kwargs):
        try:
            self.place = Place.objects.get(pk=kwargs.get('place_pk'))
        except Place.DoesNotExist:
            raise Http404
        return super(CheckinCreateViewMixin, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(CheckinCreateViewMixin, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(CheckinCreateViewMixin, self).get_context_data(**kwargs)
        ctx.update({
            'place': self.place,
        })
        return ctx

    def get_form_kwargs(self):
        kwargs = super(CheckinCreateViewMixin, self).get_form_kwargs()
        kwargs.update({'place': self.place, })
        return kwargs


class CheckinCreateView(CheckinCreateViewMixin, FormView):
    """Allows a user to checkin at a place."""
    form_class = CheckinCreateForm
    template_name = 'checkins/checkin_form.html'

    def get_form_kwargs(self):
        kwargs = super(CheckinCreateView, self).get_form_kwargs()
        if self.request.user.is_authenticated():
            kwargs.update({'user': self.request.user, })
        return kwargs


class CheckinMassCreateView(CheckinCreateViewMixin, FormView):
    """Allows a user to checkin a number of anonymous users at a place."""
    form_class = CheckinMassCreateForm
    template_name = 'checkins/mass_checkin_form.html'

    def get_form_kwargs(self):
        kwargs = super(CheckinMassCreateView, self).get_form_kwargs()
        kwargs.update({
            'user_name_base': 'Player',
        })
        return kwargs


class CheckoutView(FormView):
    """Allows a user to checkout from the currently checked-in place."""
    form_class = CheckoutForm
    template_name = 'checkins/checkout_form.html'
    success_url = '/places/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(CheckoutView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CheckoutView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user,
        })
        return kwargs
