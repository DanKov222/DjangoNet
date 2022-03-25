from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import *


class CreateLocalPost(LoginRequiredMixin, CreateView):
    """Создание публикации"""
    template_name = 'create_local_post.html'
    model = LocalPost
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UpdateLocalPost(UpdateView, LoginRequiredMixin):
    """Редактирование публикации"""
    template_name = 'update_local_post.html'
    model = LocalPost
    fields = ('title', 'text', 'image')
    context_object_name = 'post'


class DeleteLocalPost(DeleteView, LoginRequiredMixin):
    """Удаление публикации"""
    model = LocalPost
    template_name = 'delete_local_post.html'
    success_url = reverse_lazy('home')


class Home(ListView):
    """Представление домашней страницы"""
    template_name = 'home.html'
    model = LocalPost
    context_object_name = 'posts'
    paginate_by = 6


@login_required
def add_like(request, post_id):
    """Костыли!!! зато работает"""
    try:
        if Like.objects.get(post=LocalPost.objects.get(id=post_id), user=request.user):
            like = Like.objects.get(user=request.user, post=LocalPost.objects.get(id=post_id))
            like.delete()
            return redirect('local_detail', post_id)
    except ObjectDoesNotExist:
        like = Like.objects.create(user=request.user, post=LocalPost.objects.get(id=post_id))
        like.save()
        return redirect('local_detail', post_id)


class DetailLocalPost(DetailView):
    """Представление публикации"""
    model = LocalPost
    template_name = 'local_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['likes'] = Like.objects.filter(post=self.object.id).count()
        context['comments'] = Comments.objects.filter(post=self.object.id)
        return context


@login_required
def add_comment(request, post_id):
    """Костыльное добавление комментария"""
    user = request.user
    text = request.GET.get('text')
    post = LocalPost.objects.get(id=post_id)
    comment = Comments.objects.create(user=user, text=text, post=post)
    comment.save()
    return redirect('local_detail', post_id)
