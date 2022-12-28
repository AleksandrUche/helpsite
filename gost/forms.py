from django import forms


class Gost33259Form(forms.Form):
    type = forms.CharField(label='Тип 1, 2, 11...', max_length=6)
    surface = forms.CharField(label='Поверхность F, E...', max_length=6)
    dn_passage = forms.CharField(label='DN', max_length=6)
    pn = forms.CharField(label='PN', max_length=6)


class Atk261813Form(forms.Form):
    dn_passage = forms.CharField(label='Dy', max_length=6)
    pn = forms.CharField(label='Py', max_length=6)
    execution = forms.CharField(label='Исполнение', max_length=6)
