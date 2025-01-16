from django.shortcuts import render
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

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

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created successfully for {user.username}!")
            login(request, user)
            return redirect('index')  # Redirect to the homepage or another page
    else:
        form = UserCreationForm()
    return render(request, 'blog_app/register.html', {'form': form})

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')  # Redirect to the homepage or another page
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('index')
