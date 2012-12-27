"""Constants for the ``user_profile`` app."""
import pytz

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.common_timezones]

GENDER = {
    'male': 'male',
    'female': 'female',
    'other': 'other',
}

GENDER_CHOICES = (
    (GENDER['male'], GENDER['male']),
    (GENDER['female'], GENDER['female']),
    (GENDER['other'], GENDER['other']),
)
