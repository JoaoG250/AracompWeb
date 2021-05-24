from django import forms

from enigmas.models import VencedorEnigmas


class RespostaEnigmaForm(forms.Form):
    resposta = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'enigma-input'}))

    def save(self, commit=True):
        enigma = super(EnigmaVencedorForm, self).save(commit=False)
        return enigma


class EnigmaVencedorForm(forms.ModelForm):

    class Meta:
        model = VencedorEnigmas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EnigmaVencedorForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'enigma-input'})
        self.fields['email'].widget.attrs.update({'class': 'enigma-input'})
