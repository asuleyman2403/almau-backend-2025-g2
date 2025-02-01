from django import forms


class ProductCreationForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=200, required=True)
    quantity = forms.IntegerField(min_value=0, required=True)
    price = forms.IntegerField(min_value=1, max_value=1000000, required=True)




