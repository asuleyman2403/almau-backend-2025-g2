from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter cateogory name'
    }))


class ProductCreationForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter product name'
    }))
    quantity = forms.IntegerField(min_value=0, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter quantity'
    }))
    price = forms.IntegerField(min_value=1, max_value=1000000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter quantity'
    }))


class EditProductForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=200, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter product name'
    }))
    quantity = forms.IntegerField(min_value=0, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter quantity'
    }))
    price = forms.IntegerField(min_value=1, max_value=1000000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Enter quantity'
    }))
    category_id = forms.IntegerField(min_value=1, max_value=1000000, required=True, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'Select category'
    }))


