from django.db import models
from user.models import User, Organization


class Post(models.Model):
    text = models.TextField()
    date = models.DateField()
    number_of_likes = models.IntegerField(default=0)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="posts")

    def increase(self):
        self.number_of_likes += 1
        self.save()

    def decrease(self):
        self.number_of_likes -= 1
        self.save()


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    

class Comment(models.Model):
    text = models.TextField()
    date = models.DateField()
    number_of_likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    def increase(self):
        self.number_of_likes += 1
        self.save()

    def decrease(self):
        self.number_of_likes -= 1
        self.save()
    

class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="favourited_by")


class CommentAnswer(models.Model):
    text = models.TextField()
    date = models.DateField()
    number_of_likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_answers")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="answers")
    
    def increase(self):
        self.number_of_likes += 1
        self.save()

    def decrease(self):
        self.number_of_likes -= 1
        self.save()
    

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_comments")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")


class CommentAnswerLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_answer_like')
    comment_answer = models.ForeignKey(CommentAnswer, on_delete=models.CASCADE, related_name='comment_answer_like')
    

class PostImage(models.Model):
    image = models.ImageField(upload_to='post_image/')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_image')