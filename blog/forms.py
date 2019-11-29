from django import forms

class FindActivityForm(forms.Form):
    from_date = forms.DateField(label='from', widget=forms.SelectDateWidget)
    to_date = forms.DateField(label='to', widget=forms.SelectDateWidget)
