from django.db import models

class Recipe(models.Model):
    recipe_title=models.CharField(max_length=50,null=True)
    recipe_desc=models.TextField()
    recipe_image=models.FileField(upload_to='testapp/',null=True,default=None)


