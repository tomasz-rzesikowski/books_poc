from django import forms


class ImportForm(forms.Form):
    import_url = forms.URLField()
