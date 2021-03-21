from django import forms


class ImportForm(forms.Form):
    import_url = forms.URLField(label="Or ypu can paste url to Google API")
