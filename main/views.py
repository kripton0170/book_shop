from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView, View
from .models import BooksModel
from .forms import CreateBookForm
from django.urls import reverse

# class HomeView(TemplateView):
#     template_name = "main/index.html"

class HomeView(ListView):
    # model = BooksModel
    # queryset = BooksModel.objects.all().filter(price='95000')
    template_name = "main/index.html"
    
    def get_queryset(self):
        q = self.request.GET.get('q') 
        if q:
            qs = BooksModel.objects.all().filter(name=q)
        else:
            qs = BooksModel.objects.all()
        return qs
    
    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get("q")
        if q:
            context['q'] = q
        return context

class CreateBookView(CreateView):
    model = BooksModel
    success_url = '/'
    template_name = 'main/form.html'
    # fields = ['name', 'price']
    form_class = CreateBookForm
    
class UpdateBookView(UpdateView):
    model = BooksModel
    template_name = "main/update.html"
    fields = ["name", "price"]
    # success_url = '/'
    
    def get_success_url(self):
        return reverse('create')
    
class DetailBookView(DetailView):
    model = BooksModel
    template_name = "main/detail.html"
    
    
    
class DeleteBookView(DeleteView):
    model = BooksModel
    template_name = "main/delete.html"
    # success_url = "/"
    
    def get_success_url(self):
        return reverse('home')
    
class MainView(View):
    
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q') 
        if q:
            qs = BooksModel.objects.all().filter(name__icontains=q)
        else:
            qs = BooksModel.objects.all()
        return render(self.request, 'main/index.html', context={
            'object_list': qs,
            'form': CreateBookForm
        })
        
    def post(self, request, *args, **kwargs):
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
        else:
            return redirect('home')
        
    

