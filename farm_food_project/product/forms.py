import os
from os.path import join

from django import forms
from django.conf import settings

from farm_food_project.product.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('producer_profile',)


class EditProductForm(ProductForm):
    def save(self, commit=True):
        db_product = Product.objects.get(pk=self.instance.id)
        if commit:
            os.remove(join(settings.MEDIA_ROOT, str(db_product.product_image)))
        return super().save(commit)

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_type': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                }
            )
        }