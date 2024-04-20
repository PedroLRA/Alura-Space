from django.urls import path
from apps.galery.views import \
    index, filter, image, new_image, edit_image, delete_image

urlpatterns = [
    path('', index, name = 'index'),
    path('filter/<str:category>', filter, name = 'filter'),
    path('image/<int:photoId>', image, name = 'image'),
    path('new-image', new_image, name = 'new_image'),
    path('edit-image/<int:photoId>', edit_image, name = 'edit_image'),
    path('delete-image/<int:photoId>', delete_image, name = 'delete_image'),
]
