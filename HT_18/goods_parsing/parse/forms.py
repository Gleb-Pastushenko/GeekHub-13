from django import forms


class EnterIdsForm(forms.Form):
    id_list = forms.CharField(
        label="Enter products IDs, separated by coma"
    )
