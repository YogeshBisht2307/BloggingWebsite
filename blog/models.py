from django.db import models


class Author(models.Model):
    name = models.CharField(max_length = 50)
    designation = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    image = models.ImageField(upload_to="upload/",default="")

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.CharField(max_length = 100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class BlogSubCategory(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length = 100)
    permalink = models.CharField(max_length = 200)
    content = models.TextField()
    description = models.CharField(max_length = 300)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author ,on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory , on_delete=models.CASCADE)
    sub_category = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "upload/")


    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length= 100)
    permalink = models.CharField(max_length = 100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Comment(models.Model):
    name=models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    blog_comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "upload/", null=True)

    def __str__(self):
        return self.blog_comment[0:15] + "..." + "by" + self.name


class Contact(models.Model):
    name=models.CharField(max_length=30)
    email= models.EmailField(max_length=100)
    subject = models.CharField(max_length= 50)
    message = models.TextField()

    def __str__(self):
        return self.email

class Web_detail(models.Model):
    website_name = models.CharField(max_length=100)
    hero_image = models.ImageField(upload_to = "upload/")
    category_image = models.ImageField(upload_to = "upload/")
    sub_category_image = models.ImageField(upload_to = "upload/")
    comment_image = models.ImageField(upload_to = "upload/")
    facebook_link =models.CharField(max_length=200)
    instagram_link =models.CharField(max_length=200)
    twitter_link =models.CharField(max_length=200)
    telegram_link =models.CharField(max_length=200)

    def __str__(self):
        return self.website_name

class SEO_Configuration(models.Model):
    tagline = models.CharField(max_length= 200)
    description = models.TextField()
    logo = models.ImageField(upload_to = "upload/")
    keyword = models.CharField("Seprate each keywrod with comma (,) ",max_length=1000)
    web_author= models.CharField(max_length=50)
    CHOICES = (
        ("noindex , nofollow","noindex , nofollow"),
        ("index, follow", "index, follow"),
    )
    robot_tag = models.CharField( 
        max_length = 20, 
        choices = CHOICES, 
        default = "noindex , nofollow"
        )
    google_bot = models.CharField( 
        max_length = 20, 
        choices = CHOICES, 
        default = "noindex , nofollow"
        )
 