from django import forms
from image_uploader_widget.widgets import ImageUploaderWidget


class ImageUploaderWidgetForm(forms.ModelForm):
    class Meta:
        widgets = {
            'photo_link': ImageUploaderWidget(),
        }
        fields = '__all__'
