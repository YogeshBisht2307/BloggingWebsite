from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from blog.models import Blog,BlogCategory,BlogSubCategory,Tag,Comment,Contact


def pagination(request,blogs,page_number):
    paginator = Paginator(blogs, page_number) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    return blog_obj


class  IndexView(View):
    def get(self,request):
        blogs = Blog.objects.all()
        blog_obj = pagination(request,blogs,4)

        recent_post = Blog.objects.all().order_by("-date")
        context = {
            'blogs':blog_obj,
            'recent_post':recent_post,
        }
        return render(request, template_name="blog/index.html",context = context)

class BlogView(View):
    def get(self,request,category_slug):
        category = BlogCategory.objects.get(slug = category_slug)
        blogs = Blog.objects.filter(category = category)
        sub_category = BlogSubCategory.objects.filter(category = category)
        # calling pagination function
        blog_obj = pagination(request,blogs,6)
        context = {
            'blogs':blog_obj,
            'sub_category':sub_category,
            'category':category,
        }
        return render(request, template_name="blog/blog.html", context = context)

class SubCatBlogView(View):
    def get(self,request,category_slug,subCategory_slug):
        category = BlogCategory.objects.get(slug = category_slug)
        sub_cat = BlogSubCategory.objects.get(slug = subCategory_slug)
        blogs = Blog.objects.filter(category = category, sub_category= sub_cat)
        sub_category = BlogSubCategory.objects.filter(category = category)
        # calling pagination function
        blog_obj = pagination(request,blogs,6)
        context = {
            'blogs':blogs,
            'sub_category':sub_category,
            'category':sub_cat,
            
        }
        return render(request, template_name="blog/blog.html", context=context)



class BlogDetailView(View):
    def get(self, request,blog_slug):
        blog = Blog.objects.get(permalink = blog_slug)
        tags = Tag.objects.filter(blog = blog)
        blog_sub_category = blog.sub_category
        related_blogs = Blog.objects.filter(sub_category = blog_sub_category).exclude(permalink = blog_slug)
        # code for blog comment 
        comment = Comment.objects.filter(blog = blog,parent=None)
        context = {
            'blog':blog,
            'tags':tags,
            'related_blogs':related_blogs,
            'comments':comment,
        }

        return render(request, template_name="blog/blogDetail.html",context = context)
    
    def post(self,request,blog_slug):
        blog = Blog.objects.get(permalink = blog_slug)
        tags = Tag.objects.filter(blog = blog)
        blog_sub_category = blog.sub_category
        related_blogs = Blog.objects.filter(sub_category = blog_sub_category).exclude(permalink = blog_slug)
        # code for blog comment 
        

        query = request.POST
        parent_sno = query.get('parent_sno')
        name=query.get('name')
        email = query.get('email')
        comment = query.get('comment')
        # validation for comment form 
        flag = False
        if name == "":
            messages.warning(request,"Name is required")
        elif len(name) < 4 :
            messages.warning(request,"Enter a valid name")
        elif email == "":
            messages.warning(request,"Email is required")
        elif len(email)<8:
            messages.warning(request,"Enter a valid Email")
        elif comment == "":
            messages.warning(request,"Comment is required")
        else:
            flag =True
        if flag is True:
            post_comment = Comment()
            post_comment.name=name
            post_comment.email = email
            post_comment.blog_comment = comment
            post_comment.blog = blog
            if parent_sno == "":
                post_comment.save()
            else:
                parent = Comment.objects.get(id=parent_sno)
                post_comment.parent = parent
                post_comment.save()
            messages.success(request,"You have successfull comment !")
            blog_comment = Comment.objects.filter(blog = blog,parent=None)
            context = {
                'blog':blog,
                'tags':tags,
                'related_blogs':related_blogs,
                'comments':blog_comment,
                'name':name,
            }
            return render(request, template_name = "blog/blogDetail.html", context = context)
        else:
            blog_comment = Comment.objects.filter(blog = blog,parent=None)
            context = {
                'blog':blog,
                'tags':tags,
                'related_blogs':related_blogs,
                'comments':blog_comment,
                'name':name,
            }
            return render(request, template_name="blog/blogDetail.html",context=context)

class SearchBlogView(View):
    def get(self,request):
        search = request.GET.get('search')
        category = BlogCategory.objects.all()
        if len(search) >50:
            allblogs = Blog.objects.none()
        else:
            allblogsTitle = Blog.objects.filter(title__icontains = search)  
            allblogsContent = Blog.objects.filter(content__icontains = search)
            allblogs = allblogsTitle.union(allblogsContent)

        context = {
            'blogs':allblogs,
            'search_query':search,
            'categories':category,
        }
        return render(request, 'blog/search.html',context = context)
    


class ContactView(View):
    def get(self,request):
        return render(request, template_name="blog/contact.html")
    def post(self,request):
        query = request.POST
        name=query.get('name')
        email = query.get('email')
        subject = query.get('subject')
        message = query.get('message')
        # validation for comment form 
        flag = False
        if name == "":
            messages.warning(request,"Name is required !")
        elif len(name) < 4 :
            messages.warning(request,"Enter a valid name !")
        elif email == "":
            messages.warning(request,"Email is required !")
        elif len(email)<8:
            messages.warning(request,"Enter a valid Email !")
        elif subject == "":
            messages.warning(request,"Subject is required !")
        elif message == "":
            messages.warning(request, "Message is required !")
        else:
            flag =True
        
        if flag:
            contact = Contact()
            contact.name=name
            contact.email = email
            contact.message = message
            contact.subject = subject
            contact.save()
            messages.success(request, "Your Query has successfully recive, we will look on it Soon")
            return render(request,template_name="blog/contact.html", context={'name':name})
        else:
            return render(request,template_name="blog/contact.html", context={'name':name})