from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('GAMES', 'GAMES'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'GAMES':
            games_parser = parser.parser()
            for i in games_parser:
                models.PGParser.objects.create(**i)