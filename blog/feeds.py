import markdown

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from blog.models import Post

class LatestPostsFeed(Feed):
    title = "Py Bl0g"
    link = reverse_lazy("blog:post_list")
    description = 'New posts from Py Bl0g'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        # safe_markdown = mark_safe()
        # print(safe_markdown)
        return truncatewords(mark_safe(markdown.markdown(item.body)), 10)
    
    def item_pubdate(self, item):
        return item.publish