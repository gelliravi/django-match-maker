"""Views for the ``user_profile`` app."""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import FormView

from user_profile.forms import UserProfileUpdateForm
from user_profile.models import UserProfile


class UserProfileUpdateView(FormView):
    form_class = UserProfileUpdateForm
    template_name = 'user_profile/user_profile_form.html'
    success_url = '/profile/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user_profile = request.user.get_profile()
        return super(UserProfileUpdateView, self).dispatch(
            request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(UserProfileUpdateView, self).get_form_kwargs()
        kwargs.update({
            'instance': self.user_profile,
        })
        return kwargs
