from django.db import models

class ImageUpload(models.Model):
    class Meta:
        db_table = 'goods'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mainimg = models.ImageField(upload_to="images")  # こちらの通り
    img1 = models.ImageField(upload_to="images")
    img2 = models.ImageField(upload_to="images")
    img3 = models.ImageField(upload_to="images")
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.title

