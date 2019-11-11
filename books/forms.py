from django import forms

class BookSearchForm(forms.Form):
    book_name = forms.CharField(max_length=30,required=False)
    author_name = forms.CharField(max_length=30,required=False)
    isbn = forms.CharField(max_length=10,required=False)