from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from .models import *
from .forms import CreateProfileForm


class SelfProfile(DetailView):
    """Профиль пользователя"""
    template_name = 'profile.html'
    model = Profile


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'update_profile.html'
    fields = ('username', 'first_name', 'last_name', 'city', 'country', 'avatar')
    success_url = reverse_lazy('home')
    context_object_name = 'profile'


def register(request):
    if request.method == 'POST':
        user_form = CreateProfileForm(request.POST, request.FILES)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('../accounts/login')
    else:
        user_form = CreateProfileForm()
    return render(request, 'registration/create_profile.html', {'user_form': user_form})


class AddFriend(LoginRequiredMixin, CreateView):
    model = FriendList
    template_name = 'add_friend.html'
    fields = ['friends']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required
def add_friend_by_id(request, user_id):
    """Добавление пользователя в друзья"""
    if not FriendList.objects.filter(user=request.user, friends=Profile.objects.get(id=user_id)):
        user = Profile.objects.get(id=user_id)
        friend = FriendList(user=request.user)
        friend.save()
        friend.friends.add(user)
    return redirect('profile', user_id)


@login_required
def friend_list(request, user_id):
    """Список друзей"""
    friends = FriendList.objects.filter(user=user_id)
    return render(request, 'friends.html', {'friends': friends})


class SearchFriends(ListView):
    model = Profile
    template_name = 'search_users.html'
    context_object_name = 'users'

    def get_queryset(self):
        query = self.request.GET.get("q")
        users = Profile.objects.filter(
            Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))
        return users


class UserList(ListView):
    model = Profile
    template_name = 'user_list.html'
    context_object_name = 'profiles'
