from django.shortcuts import render

from .models import Blog, Service
from .forms import ServiceForm

from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, "blog_app/index.html")

def blog_list(request):
    # Fetch all blogs to display
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog_app/blog_list.html', {'blogs': blogs})

def blog_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        comments = request.POST['comments']
        image = request.FILES['image']

        # Save the blog to the database
        Blog.objects.create(title=title, content=content, comments=comments, image=image)
        return redirect('blog_list')  # Redirect to the blog list after creation

    return render(request, 'blog_app/blog_create.html')

# View to create a new service
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_services')
    else:
        form = ServiceForm()
    return render(request, 'blog_app/create_service.html', {'form': form})

# View to display all services
def all_services(request):
    services = Service.objects.all()
    return render(request, 'blog_app/all_services.html', {'services': services})