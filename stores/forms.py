from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from .models import CartItems,Addresses
from django.core.cache import cache

class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='数量', min_value=1)
    # 更新データにidを付与(.HiddenInput()で隠しinput属性でデータを受け渡し)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ['quantity', 'id']
    
    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        id = cleaned_data.get('id')
        # models.pyのCartItemsから商品の在庫数を取得
        cart_item = get_object_or_404(CartItems, pk=id)
        if quantity > cart_item.product.stock:
            raise ValidationError(f'在庫数を超えています。{cart_item.product.stock}以下にしてください')
        

class AddressInputForm(forms.ModelForm):
    address = forms.CharField(label='住所', widget=forms.TextInput(attrs={'size': '80'}))

    class Meta:
        model = Addresses
        fields = ['zip_code', 'prefecture', 'address']
        labels = {
            'zip_code': '郵便番号',
            'prefecture': '都道府県',
        }
    
    # model = Addressesでuser(外部キー)が必要なため取得
    def save(self):
        address = super().save(commit=False)
        address.user = self.user
        try:
            address.validate_unique()
            address.save()
        except ValidationError as e:
            address = get_object_or_404(
                Addresses, user=self.user,
                prefecture=address.prefecture,
                zip_code=address.zip_code,
                address=address.address
            )
            pass

        cache.set(f'address_user_{self.user.id}',address)
        return address