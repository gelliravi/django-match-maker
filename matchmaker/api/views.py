"""Views for the ``api`` app."""
import json

from django.views.generic import View
from django.http import HttpResponse

from user_profile.models import UserProfile


class UserCountAPIView(View):
    """API view that returns the number of user profiles."""
    def get(self, request, *args, **kwargs):
        count = UserProfile.objects.all().count()
        content = json.dumps(str(count))
        return HttpResponse(content, content_type='application/json')
