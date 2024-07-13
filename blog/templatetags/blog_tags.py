import markdown
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe

from blog.models import Post
from blog.utils import HTMLTextExtractor

register = template.Library()

# Tags

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


# Filters 

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter(name='htmltext')
def html_text_extract(s):
    parser = HTMLTextExtractor()
    parser.feed(s)
    return parser.get_text()