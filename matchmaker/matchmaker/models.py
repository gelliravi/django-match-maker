"""
Signal handlers and custom models and managers for the ``matchmaker`` app.

"""
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from checkins.models import Checkin
from places.models import Place, PlaceManager
from subscribe.models import Subscription


class CustomPlaceManager(PlaceManager):
    """
    PlaceManager with some extra methods needed by the matchmaker project.

    """
    def get_active(self):
        return self.get_query_set()


class CustomCheckin(Checkin):
    """
    Custom Checkin model with extra methods needed by the matchmaker project.

    """
    class Meta:
        proxy = True

    def get_name(self):
        """
        Returns the name of the user or nickname of an anonymous user.

        """
        if self.user:
            return self.user.get_profile().display_name
        return self.user_name


class CustomPlace(Place):
    """
    Custom Place model with extra methods needed by the matchmaker project.

    """
    class Meta:
        proxy = True

    objects = CustomPlaceManager()

    def get_checkins(self):
        return CustomCheckin.objects.filter(place=self, expired=False)


def send_mail(subject, message, from_email, recipient_list, bcc_recipient_list,
              priority="medium", fail_silently=False, auth_user=None,
              auth_password=None):
    from django.utils.encoding import force_unicode
    from mailer import PRIORITY_MAPPING
    from mailer.models import make_message

    priority = PRIORITY_MAPPING[priority]

    subject = force_unicode(subject)
    message = force_unicode(message)

    make_message(subject=subject,
                 body=message,
                 from_email=from_email,
                 to=recipient_list,
                 bcc=bcc_recipient_list,
                 priority=priority).save()
    return 1


@receiver(post_save, sender=Checkin)
def send_checkin_notifications(sender, **kwargs):
    instance = kwargs.get('instance')
    checkins = Checkin.objects.filter(place=instance.place, expired=False)

    if checkins.count() == 1:
        recipients = []

        # Get subscribers of the player who checked in
        ctype = ContentType.objects.get_for_model(instance.user.get_profile())
        subscriptions = Subscription.objects.filter(
            content_type=ctype, object_id=instance.pk)
        for subscription in subscriptions:
            recipients.append(subscription.user.email)

        # Get subscribers of the place
        ctype = ContentType.objects.get_for_model(instance.place)
        subscriptions = Subscription.objects.filter(
            content_type=ctype, object_id=instance.place.pk)
        for subscription in subscriptions:
            recipients.append(subscription.user.email)

        if recipients:
            context = {'place': instance.place, }
            subject = render_to_string(
                'matchmaker/email/checkin_notification_subject.txt', context)
            subject = ''.join(subject.splitlines())
            message = render_to_string(
                'matchmaker/email/checkin_notification_body_plain.txt',
                context)

            send_mail(
                subject=subject,
                message=message,
                from_email=settings.FROM_EMAIL,
                recipient_list=[],
                bcc_recipient_list=recipients,
            )
