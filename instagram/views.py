from django.shortcuts import render,redirect
from .models import  Post,Likes,Profile
from django.utils import timezone
from .forms import ProfileUpdateForm,CommentForm,PostForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url = '/accounts/login/')
def post(request):
    posts = Post.objects.all().filter(created_date__lte = timezone.now()).order_by('-created_date')


    return render(request, 'insta/post.html', {'posts':posts})

def profile(request):
    user = Profile.objects.get_or_create(user=request.user)
    user = request.user
 
    posts = Post.objects.filter(author=request.user).order_by('-created_date')

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance = request.user.profile)

        if p_form.is_valid():
            p_form.save()
            # messages.success(request,f'your account has been updated')

            return redirect('profile')


    else:
        p_form = ProfileUpdateForm(instance = request.user.profile)



    return render(request, 'insta/profile.html', {'p_form':p_form,"posts" : posts,'user' : user})     

def like(request,post_id):
    user = request.user
    post = Post.objects.get(id = post_id)
    current_likes = post.likes
    liked = Likes.objects.filter(user = user,post = post).count()
    if not liked:
        Likes.objects.create(user = user,post = post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user = user,post = post).delete()  
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return redirect('post')    

def new_comment(request,pk):
    post = Post.objects.get(pk = pk)

    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.post = post
            obj.save()
        return redirect('post')
    else:
        form = CommentForm()

    return render(request, 'insta/comment.html', {'post':post,"form": form})    

def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        # We pass in the request.FILES argument because we are going to be uploading an Image file and we want to process that in our form.
        if form.is_valid():
            post = form.save(commit = False)
            post.author = current_user
            post.save()
        return redirect('post')
    else:
        form = PostForm()
    return render(request, 'insta/create_post.html', {"form": form})        
