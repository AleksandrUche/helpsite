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
            '40', '63', '100', '160', '200', '250'
        ],
        initial=''
    )

    def clean_type_fl(self):
        type_fl = self.cleaned_data['type_fl']
        if type_fl not in ['01', '02', '11']:
            raise ValidationError(_(f'Нет значения %(value)s'),
                                  params={'value': type_fl}
                                  )
        return type_fl

    # def clean_surface_fl(self):
    #     surface = self.cleaned_data['surface']
    #     if surface not in ['B', 'C', 'D', 'E', 'F']:
    #         raise ValidationError(_(f'Нет значения %(value)s'),
    #                               params={'value': surface}
    #                               )
    #     return surface


# def clean_dn_passage(self):
#     dn_passage = self.cleaned_data['dn_passage']
#
# def clean_dn_passage(self):
#     pn = self.cleaned_data['pn']


class Atk261813Form(forms.Form):
    dn_passage = forms.CharField(label='Dy', max_length=6)
    pn = forms.CharField(label='Py', max_length=6)
    execution = forms.CharField(label='Исполнение', max_length=6)
