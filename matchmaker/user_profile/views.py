"""Views for the ``user_profile`` app."""
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DetailView

from user_profile.forms import UsernameUpdateForm, UserProfileUpdateForm
from user_profile.models import UserProfile


class UserProfileViewMixin(object):
    def _security_checks(self, request, *args, **kwargs):
        return

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        try:
            self.user_profile = request.user.get_profile()
        except UserProfile.DoesNotExist:
            self.user_profile = UserProfile.objects.create(user=request.user)
        security_result = self._security_checks(request, *args, **kwargs)
        if isinstance(security_result, HttpResponseRedirect):
            return security_result
        return super(UserProfileViewMixin, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(UserProfileViewMixin, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UserProfileViewMixin, self).get_form_kwargs()
        kwargs.update({
            'instance': self.user_profile,
        })
        return kwargs


class UserProfileUpdateView(UserProfileViewMixin, FormView):
    form_class = UserProfileUpdateForm
    template_name = 'user_profile/user_profile_form.html'
    success_url = '/profile/'


class UsernameUpdateView(UserProfileViewMixin, FormView):
    form_class = UsernameUpdateForm
    template_name = 'user_profile/username_form.html'
    success_url = '/profile/'

    def _security_checks(self, request, *args, **kwargs):
        super(UsernameUpdateView, self)._security_checks(
            request, *args, **kwargs)
        if self.user_profile.username:
            return redirect(reverse('user_profile_update'))


class PublicProfileView(DetailView):
    model = UserProfile
    slug_field = 'username'
    slug_url_kwarg = 'username'
