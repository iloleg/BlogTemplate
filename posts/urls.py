from django.urls import path
from .views import PostListView, PostDetailView, AboutView, NewsLetterView, CommunityView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('newsletter/', NewsLetterView.as_view(), name='newsletter' ),
    path('community/', CommunityView.as_view(), name='community' )
]
