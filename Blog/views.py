from django.shortcuts import render,redirect
from .models import Post, Comment
import uuid
from django.contrib.auth.decorators import login_required

def IDGen():
    Id = uuid.uuid1()
    if(Post.objects.filter(ID=Id).exists()):
        IDGen()
    else:
        return Id

def BlogHome(request):
    Result = Post.objects.all().order_by("-Date_created")
    Dict = {"Result":Result}
    return render(request, "BlogHome.html", Dict)

def BlogPost(request, id):
    if(request.method == "POST"):
        Data = request.POST
        Comment.objects.create(Blog_ID = Post.objects.get(ID=id), Content=Data["comment"], User_ID = request.user)
        return redirect("BlogPost", id=id)
    else:
        Obj = Post.objects.get(ID = id)
        Obj.views +=1 
        Obj.save()
        Comments = Comment.objects.filter(Blog_ID = Obj)
        Dict = {"Data":Obj, "Comments":Comments}
        return render(request, "BlogPost.html", Dict)

@login_required
def CreateBlog(request):
    if(request.method == "POST"):
        ID = IDGen()
        Data = request.POST
        Post.objects.create(ID = ID, Title = Data["title"], Content = Data["content"], user_id = request.user.id)
        return redirect("BlogHome")
    else:
        return render(request, "CreatePost.html")

def Like(request, ID):
    obj = Post.objects.get(ID=ID)
    obj.Likes += 1
    obj.save()
    return redirect("BlogPost", id=ID)
    
def YourPosts(request):
    obj = Post.objects.filter(user=request.user)
    Dict = {"Data": Post.objects.filter(user=request.user)}
    return render(request, "YourPosts.html", Dict)