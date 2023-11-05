from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    authUser = models.OneToOneField(User, on_delete = models.CASCADE)
    authRate = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return f'{self.authUser}'

    def update_rating(self):
        postsRate = self.post_set.aggregate(postsRating=Sum('rate'))
        pRating = 0
        pRating += postsRate.get('postsRating')

        commentsRate = self.authUser.comment_set.aggregate(commentsRating=Sum('rate'))
        cRating = 0
        cRating += commentsRate.get('commentsRating')

        postsComentsRate = self.post_set.all().values('rate')
        pcRating = 0
        for i in postsComentsRate:
            pcRating + i['rate']
        
        self.authRate = pRating*3 + cRating + pcRating
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'


class Post(models.Model):
    
    cat_choise = [
    ('Article', 'Article'),
    ('News', 'News'),
    ]

    authors =  models.ForeignKey(Author, on_delete = models.CASCADE)
    postType = models.CharField(max_length=8, 
                            choices = cat_choise, 
                            default = 'Article')
    
    postCategory = models.ManyToManyField(Category, through = 'PostCategory')
    createTime = models.DateTimeField(auto_now_add = True)
    postHead = models.CharField(max_length = 255)
    postBody = models.TextField()
    rate = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return f'{self.postHead}'

    def like(self):
        self.rate += 1
        self.save()
    
    def dislike(self):
        self.rate -= 1
        self.save()

    def preview(self):
        return f"{self.postBody[:123]} ..."
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    postTh = models.ForeignKey(Post, on_delete = models.CASCADE)
    categoryTh = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete = models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete = models.CASCADE)
    commentText = models.TextField()
    createTime = models.DateTimeField(auto_now_add = True)
    rate = models.IntegerField(default = 0)

    def like(self):
        self.rate += 1
        self.save()
    
    def dislike(self):
        self.rate -= 1
        self.save()
