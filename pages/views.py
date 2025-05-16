from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Page

# LISTADO
class PageListView(ListView):
    model = Page
    template_name = 'pages/pages_list.html'
    context_object_name = 'pages'

# DETALLE
class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page_detail.html'

# CREACIÓN
class CreatePageView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('pages_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# EDICIÓN
class UpdatePageView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    template_name = 'pages/page_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('pages_list')

    def test_func(self):
        page = self.get_object()
        return self.request.user == page.author

# BORRADO
class DeletePageView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = 'pages/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')

    def test_func(self):
        page = self.get_object()
        return self.request.user == page.author

# ABOUT
def about_view(request):
    return render(request, 'pages/about.html')