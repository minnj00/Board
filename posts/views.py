

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,

    }
    return render(request, 'index.html', context)

def detail(request, id):
    post =Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)
def new(request):
    return render(request, 'new.html')

def create(request):
    title=request.POST.get('title')
    # new.html 에서 input 을 가져오기 위한 코드 
    content=request.POST.get('content')

    # post = Post()
    # post.title = title
    # post.content = content
    # post.save 

    # 인스턴스화를 함과 동시에 집어넣음
    post= Post(title=title, content= content)
    post.save()

    return redirect('posts:detail', id=post.id)

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('posts:index')

def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post':post,
    }
    return render(request, 'edit.html', context )

def update(request, id):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect('posts:detail', id=post.id)