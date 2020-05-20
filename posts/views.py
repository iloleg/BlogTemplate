from django.views.generic import ListView, DetailView,TemplateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    paginate_by = 8
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AboutView(TemplateView):
    template_name="about.html"

class CommunityView(TemplateView):
    template_name = "community.html"

class NewsLetterView(TemplateView):
    template_name = 'newsletter.html'