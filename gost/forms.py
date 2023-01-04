from django import forms


class Gost33259Form(forms.Form):
    type = forms.CharField(label='Тип фланца', max_length=6, help_text=['1', '2', '11'])
    surface = forms.CharField(label='Уплотнительная поверхность', max_length=6, help_text=['B', 'C', 'D', 'E', 'F'])
    dn_passage = forms.CharField(label='DN',
                                 max_length=6,
                                 help_text=[
                                     '10', '15', '20', '25', '32', '40', '50', '65', '80', '100', '125',
                                     '150', '200', '250', '300', '350', '400', '450', '500', '600', '700',
                                     '800', '900', '1000', '1200', '1400', '1600', '1800', '2000', '2200',
                                     '2400', '2600', '2800', '3000', '3200', '3400', '3600', '4000'
                                 ]
                                 )
    pn = forms.CharField(label='PN',
                         max_length=6,
                         help_text=[
                             '1', '2,5', '6', '10', '16', '25',
                             '40', '63', '100', '160', '200', '250'
                         ]
                         )


class Atk261813Form(forms.Form):
    dn_passage = forms.CharField(label='Dy', max_length=6)
    pn = forms.CharField(label='Py', max_length=6)
    execution = forms.CharField(label='Исполнение', max_length=6)
