from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Hide help text
        for field in self.fields.values():
            field.help_text = ""


class VisualizationOptionsForm(forms.Form):
    VISUALIZATION_TYPE_CHOICES = [
        ('streamgraph', 'Streamgraph'),
    ]

    VISUALIZATION_TARGET_CHOICES = [
        ('artist', 'Artist'),
        ('album', 'Album'),
        ('track', 'Track'),
        ('tag', 'Tag'),
    ]

    TIME_RANGE_CHOICES = [
        ('1month', 'Last Month'),
        ('3month', 'Last 3 Months'),
        ('6month', 'Last 6 Months'),
        ('12month', 'Last 12 Months'),
        ('alltime', 'All Time'),
    ]

    LIMIT_CHOICES = [
        (10, 'Top 10'),
        (20, 'Top 20'),
        (50, 'Top 50'),
    ]

    visualization_type = forms.ChoiceField(
        choices=VISUALIZATION_TYPE_CHOICES,
        initial='streamgraph'
    )

    visualization_target = forms.ChoiceField(
        choices=VISUALIZATION_TARGET_CHOICES,
        initial='artist'
    )

    time_range = forms.ChoiceField(
        choices=TIME_RANGE_CHOICES,
        initial='1month'
    )

    limit = forms.ChoiceField(
        choices=LIMIT_CHOICES,
        initial=20
    )
