
from django.contrib import admin
from django.urls import path, include
from user.views import UserViewset
from socialBook.views import UploadViewset, CommentViewset, LikeViewSet


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',UserViewset.as_view({'post':'create','get':'view_all'})),
    path('user/<uuid:pk>/',UserViewset.as_view({'get':'view_by_id','put':'partial_update'})), 
    path('user/login/',UserViewset.as_view({'post':'login'})),

    path('upload/',UploadViewset.as_view({'post':'create','get':'view_all'})),
    path('upload/<uuid:pk>/',UploadViewset.as_view({'get':'view_by_id','put':'partial_update'})),

    path('comment/',CommentViewset.as_view({'post':'create', 'get':'view_all'})),
    path('comment/<uuid:pk>', CommentViewset.as_view({'get':'view_user_comment','put':'partial_update'})),

    path('like/',LikeViewSet.as_view({'post':'like_post'})),
    path('like/<uuid:pk>/',LikeViewSet.as_view({'get':'like_post_by_user'})),
    path('like/highest-like',LikeViewSet.as_view({'get':'highest_like'})),
]


 