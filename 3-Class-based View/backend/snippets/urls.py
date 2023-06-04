# # 1), 3), 5)  views.py  //////////////////////////////////
# from django.urls import path
# from .views import SnippetList

# urlpatterns = [
#     path('list/', SnippetList.as_view()),
#     path('create/', SnippetList.as_view()),
# ]


# # 2), 4), 6) views.py  //////////////////////////////////
from django.urls import path
from .views import SnippetList, SnippetDetail

urlpatterns = [
    path('list/', SnippetList.as_view()),
    path('create/', SnippetList.as_view()),
    path('<int:pk>/detail/', SnippetDetail.as_view()),
    path('<int:pk>/update/', SnippetDetail.as_view()),
    path('<int:pk>/delete/', SnippetDetail.as_view()),
]