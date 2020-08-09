from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3
from django.forms import ModelForm

from webapp.models import RaffleParticipant


class RaffleForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = RaffleParticipant
        fields = ['participant_name', 'participant_email']
