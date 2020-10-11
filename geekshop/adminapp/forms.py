from django import forms


from mainapp.models import GameTypes, Game

from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser


class ShopUserAdminEditForm(ShopUserEditForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class GameTypeEditForm(forms.ModelForm):
    class Meta:
        model = GameTypes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class GameEditForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''





