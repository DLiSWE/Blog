from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
#set publish date variable in class to timezone now when called
    def publish(self):
        self.published_date = timezone.now()
        self.save()
#display only approved comments
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

#go to post_detail page to find primary key of post just created
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

#allows to display a string representation
    def __str__(self):
        return self.title

#Comment model should be directly related to a post object.
class Comment(models.Model):
    post = models.ForeignKey('BlogApp.post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

#    
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text

