from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from .forms import EmailPostForm, CommentForm, SearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Comment
from django.db.models import Count
from taggit.models import Tag
from django.views.generic import ListView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, HttpResponse

# Create your views here.


def post_list(request, tag_slug=None):    # this method us for paginator now us class based-view
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    paginator = Paginator(post_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)

    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
        'tag': tag,

    }
    return render(request, 'post/list_post.html', context)


# post detail and post comments
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year,
                             publish__month=month,  publish__day=day)
    # comment post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    # post tags retreve
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(
        tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count(
        'tags')).order_by('-same_tags', '-publish')[:4]

    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'new_comment': new_comment,
        'similar_posts': similar_posts,
    }

    return render(request, 'post/post_detail.html', context)


#end of post detail and post comments


# class based views fo list post
class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'post/list_post.html'


# method sending email post
def post_shar(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommended to read "\
                f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'karimbiologie@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'post': post,
        'form': form,
        'sent': sent
    }
    return render(request, 'post/share.html', context)
# end method post share


# #search views with search victor and search query
# def post_search(request):
#     form = SearchForm()
#     query = None
#     resulta = []
#     if 'query' in request.GET :
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             search_victor = SearchVector('title', weight ='A')+\
#                             SearchVector('body', weight = 'B')
#             search_query  = SearchQuery(query)
#             resulta = Post.objects.annotate( search =search_victor,\
#                                             rank = SearchRank(search_victor,search_query))\
#                                             .filter(rank__gte=0.3).order_by('-rank')
#
#     context = {
#     'form':form,
#     'query':query,
#     'resulta':resulta,
#     }
#     return render(request,'blog/post/search.html', context)

#search views
def post_search(request):
    form = SearchForm()
    query = None
    resulta = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_victor = SearchVector('title', weight='A') +\
                SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            resulta = Post.objects.annotate(similarity=TrigramSimilarity('title', query))\
                .filter(similarity__gte=0.1).order_by('-similarity')

    context = {
        'form': form,
        'query': query,
        'resulta': resulta,
    }
    return render(request, 'post/search.html', context)
