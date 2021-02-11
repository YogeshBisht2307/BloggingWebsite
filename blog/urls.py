from django.urls import path
from blog.views import IndexView, BlogView,BlogDetailView,SubCatBlogView,SearchBlogView, ContactView

urlpatterns = [
    path('',IndexView.as_view(), name="Home"),

    # path for showing all the blogs
    path('blogs/<str:category_slug>/<str:subCategory_slug>',SubCatBlogView.as_view(), name="SubCategory"),
    path('blogs/<str:category_slug>',BlogView.as_view(),name="blog"),
    
    # path for showing a paricualar blog
    path('blog/<str:blog_slug>',BlogDetailView.as_view(), name="BlogDetail"),
    path('search_blog/',SearchBlogView.as_view(), name="SearchBlog"),

    path('contact/',ContactView.as_view(), name="Contact"),
]
