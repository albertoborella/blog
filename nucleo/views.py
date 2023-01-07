from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post,Categoria
from .forms import PostForm


class PostListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'nucleo/home.html'

    def get_queryset(self):
        return Post.objects.filter(publicado=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'nucleo/detail.html'


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'nucleo/categoria.html'

    def get_queryset(self):
        categoria_id = self.request.GET['cat']
        if categoria_id:
            return Post.objects.filter(categoria=categoria_id, publicado=True)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(CategoriaListView, self).get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.get(id=self.request.GET['cat'])
        return context


class AutorListView(ListView):
    model = User
    template_name = 'nucleo/autor.html'

    def get_queryset(self, **kwargs):
        autor_id = self.request.GET['aut']
        if autor_id:
            return Post.objects.filter(autor=autor_id, publicado=True)
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AutorListView, self).get_context_data(**kwargs)
        context['autor'] = User.objects.get(id=self.request.GET['aut'])
        return context

def dates(request, month_id, year_id):
    posts = Post.objects.filter(publicado=True, created__month=month_id, created__year=year_id)

    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Setiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }
    return render(request, 'nucleo/dates.html', { 'posts':posts, 'month':meses[month_id], 'year':year_id })

class PostCreateView(CreateView):
    model = Post 
    form_class = PostForm

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) + '?ok'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')


class AboutPageView(TemplateView):

    template_name = "nucleo/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




