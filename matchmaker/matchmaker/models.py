"""Signal handlers for the ``matchmaker`` app."""
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_libs.utils_email import send_email

from checkins.models import Checkin
from subscriptions.models import Subscription


@receiver(post_save, sender=Checkin)
def send_checkin_notifications(sender, **kwargs):
    instance = kwargs.get('instance')
    checkins = Checkin.objects.filter(place=instance.place, expired=False)

    if checkins.count() == 1:
        recipients = []
        ctype = ContentType.objects.get_for_model(instance.place)
        subscriptions = Subscription.objects.filter(content_type=ctype)
        for subscription in subscriptions:
            recipients.append(subscription.user.email)

        if recipients:
            send_email(
                request={},
                extra_context={'place': instance.place, },
                subject_template=(
                    'matchmaker/email/checkin_notification_subject.txt'),
                body_template_plain=(
                    'matchmaker/email/checkin_notification_body_plain.txt'),
                body_template=(
                    'matchmaker/email/checkin_notification_body.html'),
                from_email=settings.FROM_EMAIL,
                recipients=recipients,
            )
