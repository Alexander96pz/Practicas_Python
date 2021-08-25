from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import ArticleForms
from .models import Article
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
# Create your views here.
class ArticleCreateView(CreateView):
    template_name='articles/article_create.html'
    form_class=ArticleForms
    query_set=Article.objects.all()
    def formvalid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
    # return render(request,self.template_name,context)
class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()
class ArticleDetailView(DetailView):
    # model = Article
    template_name='articles/article_details.html'
    # obligatorio get_object
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
# class ArticleDeleteView:
class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)
    def get_success_url(self):
        return reverse('articles:article-list')

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForms

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)