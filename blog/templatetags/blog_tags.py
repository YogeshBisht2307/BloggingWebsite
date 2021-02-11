from django import template
from blog.models import BlogCategory,Comment,Blog,Web_detail, SEO_Configuration
register = template.Library()


@register.simple_tag
def SEO():
    configuration= SEO_Configuration.objects.all().first()
    return configuration

@register.simple_tag
def web_detail():
    detail = Web_detail.objects.all().first()
    return detail

@register.simple_tag
def category():
    categories = BlogCategory.objects.all()
    return categories
    
@register.simple_tag
def comment_replies(comment):
    replies = Comment.objects.filter(parent = comment)
    return replies


@register.simple_tag
def total_no_of_comment(blog):
    total = Comment.objects.filter(blog=blog)
    length = len(total)
    return length

@register.simple_tag
def feature_post():
    blogs = Blog.objects.all()
    comment_dict = {}
    for blog in blogs:
        no_of_comment = Comment.objects.filter(blog = blog).count()
        comment_dict[blog.permalink] = no_of_comment
    comment = dict(sorted(comment_dict.items(),reverse=True, key=lambda item: item[1]))
    query_set =set()
    for slug in dict(list(comment.items())[0: 5]):
        blog = Blog.objects.get(permalink = slug)
        query_set.add(blog)
    return query_set
