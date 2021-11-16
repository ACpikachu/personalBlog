
import markdown
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from comment.models import Comment
from .form import ArticlePostForm
from .models import ArticlePost


# Create your views here.


def article_list(request):
    '''
    支持分页的文章列表
    '''
    search = request.GET.get('search')
    order = request.GET.get('order')
    # 搜索逻辑
    if search:
        if order == 'total_views':
            # 用 Q对象 进行联合搜索
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        search = ''
        if order == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
        else:
            article_list = ArticlePost.objects.all()

    # 每页显示 3 篇文章
    paginator = Paginator(article_list, 3)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    # 需要吧order和search一起传过去
    context = {'articles': articles, 'order':order, "search":search}
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    '''文章内容界面，使用markdown进行渲染'''
    md = markdown.Markdown(
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    ) 
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)
    # 浏览量+1
    article.total_views += 1
    article.save(update_fields=['total_views'])
    #使用markdown转换
    article.body = md.convert(article.body)
    #取出评论,filter可以取出多个符合条件的对象，get方法只能取回一个
    comments = Comment.objects.filter(article=id)
    # # 需要传递给模板的对象
    context = { 'article': article, 'toc': md.toc, 'comments': comments }
    # context = { 'article': article, 'toc': md.toc}
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)


def article_create(request):
    '''
    创建文章

        创建时间自动填充，会判断用户的登录状态    
    '''
    # 判断用户是否提交数据
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # 指定数据库中 id=1 的用户为作者
            # 如果你进行过删除数据表的操作，可能会找不到id=1的用户
            # 此时请重新创建用户，并传入此用户的id
            new_article.author = User.objects.get(id=1)
            # 将新文章保存到数据库中
            new_article.save()
            # 完成后返回到文章列表
            return redirect("article:article_list")
        # 如果数据不合法，返回错误信息
        else:

            return HttpResponse("表单内容有误，请重新填写。")
        # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文
        context = {'article_post_form': article_post_form}
        # 返回模板
        return render(request, 'article/create.html', context)


# 不安全的删除方法！
def article_delete(request, id):
    '''不安全的删除方法'''
    # 获取要删除文章的id
    article = ArticlePost.objects.get(id=id)
    # 调用原生delete函数
    article.delete()
    return redirect("article:article_list")


# 安全的删除方法
def article_safe_delete(request, id):
    '''
    安全的删除方法

        将请求限定为POST
    '''
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅仅允许POST请求")


# 更新文章
def article_update(request, id):
    """
    更新文章的视图函数
    通过POST方法提交表单，更新title、body字段
    GET方法进入初始表单页面
    id： 文章的 id
    """
    article = ArticlePost.objects.get(id=id)
    if request.user != article.author:
        return HttpResponse("抱歉，你无权修改这篇文章。")
    
    # 获取需要修改的具体文章对象

    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect("article:article_detail", id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = {'article': article, 'article_post_form': article_post_form}
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)
