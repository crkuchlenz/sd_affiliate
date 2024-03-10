from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    """
    Model representing an post event.

    Attributes:
        title (str): The title of the post.
        content (txt): The content written in the post.
        author (User): The user who created the post.
        date_posted (datetime): The timestamp when the post record was created.
        date_updated (datetime): The timestamp when the post record was last updated.

    Args:
        models (_type_): _description_
    """
    title = models.CharField(_("Title"), max_length=100)
    content = models.TextField(_("Content"))
    date_posted = models.DateField(_("Date Posted"), auto_now_add=True)
    date_updated = models.DateField(_("Date Updated"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    def info(self):
        return f"""Post:
    title: {self.title}
    content: {self.content}
    author: {self.author}
    date_posted: {self.date_posted}
    date_updated: {self.date_updated}
    """
    

    

    
