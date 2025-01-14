from django.shortcuts import render

from .models import Blog, Service

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

def create_service(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        # Create the Service object directly
        Service.objects.create(title=title, description=description, image=image)

        return redirect('all_services')  # Redirect to the service list after creation

    return render(request, 'blog_app/create_service.html')

def all_services(request):
    services = Service.objects.all()
    return render(request, 'blog_app/all_services.html', {'services': services})

def about(request):
    return render(request, 'blog_app/about.html')

def contact(request):
    return render(request, 'blog_app/contact.html')