# # 1) //////////////////////////////////
# from django.urls import path
# from .views import snippet_list

# urlpatterns = [
#     path('', snippet_list),
#     path('create/', snippet_list),
# ]


# # 2) //////////////////////////////////
from django.urls import path
from .views import snippet_list, snippet_detail

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_detail),
    path('<int:pk>/update/', snippet_detail),
    path('<int:pk>/delete/', snippet_detail),
]