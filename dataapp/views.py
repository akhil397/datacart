from django.shortcuts import render, get_object_or_404, redirect
from .models import CodeModels
from .forms import CodeForm

# Show list of code entries
def details(request):
    code_models = CodeModels.objects.all()
    return render(request, 'detail.html', {'code_models': code_models})

# Show a single item
def about(request, pk):
    code_detail = get_object_or_404(CodeModels, id=pk)
    return render(request, 'about.html', {'code_detail': code_detail})

# Add new data
def adddata(request):
    if request.method == 'POST':
        codeformsave = CodeForm(request.POST)
        if codeformsave.is_valid():
            codeformsave.save()
            return redirect('details')  # Redirect after saving
    else:
        codeformsave = CodeForm()
    
    return render(request, 'add_data.html', {'codeform': codeformsave})

# Update an entry
def update_code_model(request, pk):
    code_model = get_object_or_404(CodeModels, id=pk)
    
    if request.method == 'POST':
        form = CodeForm(request.POST, request.FILES, instance=code_model)
        if form.is_valid():
            form.save()
            return redirect('about', pk=code_model.pk)  # Redirect to about page
    else:
        form = CodeForm(instance=code_model)
    
    return render(request, 'update.html', {'form': form})

# Delete an entry
def delete_data(request, pk):
    code = get_object_or_404(CodeModels, id=pk)
    code.delete()
    return redirect('details')

# Search function
def search_btn(request):
    searched = ""
    posts = []
    
    if request.method == 'POST':
        searched = request.POST.get('searched', '')  # Avoid KeyError
        posts = CodeModels.objects.filter(language__icontains=searched)
    
    return render(request, 'search.html', {'searched': searched, 'posts': posts})