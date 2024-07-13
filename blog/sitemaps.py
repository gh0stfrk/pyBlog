from django.contrib import sitemaps

from blog.models import Post


class PostSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.updated