from .models import Page
from .forms import PageForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args,
                                                        **kwargs)


class PagesListView(StaffRequiredMixin, ListView):
    model = Page


class PageDetailView(StaffRequiredMixin, DetailView):
    model = Page


class PageCreate(StaffRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    # 1 FORMA PARA REDIRECCIONAR
    # def get_success_url(self):
    #    return reverse('pages:pages')
    # 2 FORMA PARA REDIRECCIONAR (para perezosos-para mi)
    success_url = reverse_lazy('pages:pages')


class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
