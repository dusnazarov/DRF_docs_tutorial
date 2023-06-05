# 1) //////////////////////////////////
# from django.urls import path
# from .views import snippet_list

# urlpatterns = [
#     path('list/', snippet_list),
#     path('create/', snippet_list),
# ]


# # 2) # //////////////////////////////////
# from django.urls import path
# from .views import snippet_list, snippet_detail

# urlpatterns = [
#     path('list/', snippet_list),
#     path('create/', snippet_list),
#     path('<int:pk>/detail/', snippet_detail),
#     path('<int:pk>/update/', snippet_detail),
#     path('<int:pk>/delete/', snippet_detail),
# ]


# # 3), 4) //////////////////////////////////
from django.urls import path
from .views import snippet_list_detail

urlpatterns = [
    path('list/', snippet_list_detail),
    path('create/', snippet_list_detail),
    path('<int:pk>/detail/', snippet_list_detail),
    path('<int:pk>/update/', snippet_list_detail),
    path('<int:pk>/delete/', snippet_list_detail),
]