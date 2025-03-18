from django import forms
from .models import Post, Category


class AddPostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['title'].widget.attrs.update({"placeholder": '*Заголовок'})
            self.fields['content'].widget.attrs.update({"placeholder": '*Текст'})
            self.fields['excerpt'].widget.attrs.update({"placeholder": '*Краткое описание'})
            self.fields['category'].widget.attrs.update({"placeholder": '*сатегории'})
            self.fields['tags'].widget.attrs.update({"placeholder": 'теги'})
            self.fields['is_published'].widget.attrs.update({"placeholder": 'опобликовать'})
            self.fields['featured_image'].widget.attrs.update({"placeholder": 'Изображение'})
            
            self.fields[field].help_text = None
            self.fields[field].label = '' if field != 'category' else "theme"
            self.fields['is_published'].label = 'Published'

           
            

    class Meta:
        model = Post
        fields = ("title",
                  "content",
                  "excerpt",
                  "category",
                  "tags",
                  "is_published",
                  "featured_image")
        
       
