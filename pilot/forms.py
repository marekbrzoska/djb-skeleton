from django import forms


class Form(forms.Form):
    name = forms.CharField(max_length=30, help_text="laj")
    email = forms.EmailField(max_length=30, help_text="laj email dura lala")
    country = forms.ChoiceField(choices=[('', '---'), (1, 'one'), (2, 'two'), (3, '3333')], help_text="lajfjkdal ajd asdfkj")
    educated = forms.BooleanField()
