from django import forms


class Gost33259Form(forms.Form):
    type = forms.CharField(label='Тип 1, 2, 11...', max_length=6)
    surface = forms.CharField(label='Поверхность F, E...', max_length=6)
    dn_passage = forms.CharField(label='DN', max_length=6)
    pn = forms.CharField(label='PN', max_length=6)
