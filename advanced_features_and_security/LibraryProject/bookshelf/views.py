from django.shortcuts import render

# Create your views here.


from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .forms import ExampleForm
from .models import MyModel
from .models import Book

# View to edit MyModel (only accessible to users with `can_edit` permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_model_view(request, pk):
    # Code to handle editing
    instance = MyModel.objects.get(pk=pk)
    if request.method == 'POST':
        # Save changes logic
        pass
    return render(request, 'edit_model.html', {'instance': instance})

# View to create MyModel (only accessible to users with `can_create` permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_model_view(request):
    # Code to handle creation
    if request.method == 'POST':
        # Save new instance logic
        pass
    return render(request, 'create_model.html')

# View to delete MyModel (only accessible to users with `can_delete` permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_model_view(request, pk):
    # Deletion logic
    instance = MyModel.objects.get(pk=pk)
    instance.delete()
    return redirect('model_list')


#Add permission_required to book_list Vie
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})



def search_books(request):
    books = []
    form = ExampleForm(request.GET or None)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})
