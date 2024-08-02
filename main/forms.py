from django import forms

class EscolhaForm(forms.Form):
    PERGUNTAS = [
        ('opcao1', 'Nunca'),
        ('opcao2', 'Raramente'),
        ('opcao3', 'Às Vezes'),
        ('opcao4', 'Frequentemente'),
        ('opcao5', 'Sempre'),
    ]

    pergunta1 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 1')
    pergunta2 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 2')
    pergunta3 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 3')
    pergunta4 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 4')
    pergunta5 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 5')

class EscolhaForm2(forms.Form):
    PERGUNTAS = [
        ('opcao1', 'Nunca'),
        ('opcao2', 'Raramente'),
        ('opcao3', 'Às Vezes'),
        ('opcao4', 'Frequentemente'),
        ('opcao5', 'Sempre'),
    ]

    pergunta6 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 6')
    pergunta7 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 7')
    pergunta8 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 8')
    pergunta9 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 9')
    pergunta10 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 10')

class EscolhaForm3(forms.Form):
    PERGUNTAS = [
        ('opcao1', 'Nunca'),
        ('opcao2', 'Raramente'),
        ('opcao3', 'Às Vezes'),
        ('opcao4', 'Frequentemente'),
        ('opcao5', 'Sempre'),
    ]

    pergunta11 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 11')
    pergunta12 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 12')
    pergunta13 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 13')
    pergunta14 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 14')
    pergunta15 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 15')

class EscolhaForm4(forms.Form):
    PERGUNTAS = [
        ('opcao1', 'Nunca'),
        ('opcao2', 'Raramente'),
        ('opcao3', 'Às Vezes'),
        ('opcao4', 'Frequentemente'),
        ('opcao5', 'Sempre'),
    ]

    pergunta16 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 16')
    pergunta17 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 17')
    pergunta18 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 18')
    pergunta19 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 19')
    pergunta20 = forms.ChoiceField(choices=PERGUNTAS, widget=forms.RadioSelect, label='Pergunta 20')


