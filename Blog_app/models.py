from django.db import models

# Create your models here.

class Blog(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False,default='slug')
    Main_Title = models.CharField(max_length=200)
    Sub_Title=models.CharField(max_length=200)
    Category=models.CharField(max_length=100)
    Heading=models.CharField(max_length=100)
    Paragraph1 = models.TextField()
    Paragraph2 = models.TextField()
    Highlight=models.CharField(max_length=200,default="Text")
    img=models.ImageField(upload_to='images/',null=True,blank=True)
    points = models.ManyToManyField('Points')

    def __str__(self):
        return self.slug
    
class Points(models.Model):
    point=models.CharField(max_length=500)
    
    def __str__(self):

        return self.point

