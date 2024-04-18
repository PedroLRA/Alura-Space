from django.urls import path
from apps.galery.views import \
    index, image, new_image, edit_image, delete_image

urlpatterns = [
    path('', index, name = 'index'),
    path('image/<int:photoId>', image, name = 'image'),
    path('new-image', new_image, name = 'new_image'),
    path('edit-image', edit_image, name = 'edit_image'),
    path('delete-image', delete_image, name = 'delete_image'),
]
