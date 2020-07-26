from django import template
from ..models import Post
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

# total post tag
register = template.Library()
@register.simple_tag
def total_post():
    return Post.objects.count()


# latest post
@register.inclusion_tag('blog/post/latest_posts.html')
def latest_posts(count = 5):
    latest_post= Post.objects.order_by('-publish')[:count]
    context={'latest_post' : latest_post,}
    return context


# latest comment
@register.inclusion_tag('blog/post/most_commented_posts.html')
def most_commented_posts(count=5):
    most_commented_post = Post.objects.annotate(total_comments = Count('comments')).order_by('-total_comments')[:count]
    context={'most_commented_post':most_commented_post ,}
    return context
# custom filter
@register.filter(name='markdown')
def markdown_forma(text):
    md = mark_safe(markdown.markdown(text))
    return md
