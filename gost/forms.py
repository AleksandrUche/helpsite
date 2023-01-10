from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Gost33259Form(forms.Form):
    type_fl = forms.CharField(
        label='Тип фланца',
        max_length=6,
        help_text=['01', '02', '11'],
        initial='',
    )
    surface = forms.CharField(
        label='Уплотнительная поверхность',
        max_length=6,
        help_text=['B', 'C', 'D', 'E', 'F'],
        initial=''
    )
    dn_passage = forms.CharField(
        label='DN',
        max_length=6,
        help_text=[
            '10', '15', '20', '25', '32', '40', '50', '65', '80', '100', '125',
            '150', '200', '250', '300', '350', '400', '450', '500', '600', '700',
            '800', '900', '1000', '1200', '1400', '1600', '1800', '2000', '2200',
            '2400', '2600', '2800', '3000', '3200', '3400', '3600', '4000'
        ],
        initial=''
    )
    pn = forms.CharField(
        label='PN',
        max_length=6,
        help_text=[
            '1', '2,5', '6', '10', '16', '25',
            '40', '63', '100', '160', '200'
        ],
        initial=''
    )

    def clean(self):
        cleaned_data = super().clean()
        type_fl = cleaned_data.get('type_fl')
        surface = cleaned_data.get('surface')
        dn_passage = cleaned_data.get('dn_passage')
        pn = cleaned_data.get('pn')

        if type_fl and surface and dn_passage and pn:
            if type_fl not in self.fields['type_fl'].help_text:
                self.add_error('type_fl', f'Нет значения "{type_fl}"')
            if surface not in self.fields['surface'].help_text:
                self.add_error('surface', f'Нет значения "{surface}"')
            if dn_passage not in self.fields['dn_passage'].help_text:
                self.add_error('dn_passage', f'Нет значения "{dn_passage}"')
            if pn not in self.fields['pn'].help_text:
                self.add_error('pn', f'Нет значения "{pn}"')


class Atk261813Form(forms.Form):
    dn_passage = forms.CharField(label='Dy', max_length=6)
    pn = forms.CharField(label='Py', max_length=6)
    execution = forms.CharField(label='Исполнение', max_length=6)
