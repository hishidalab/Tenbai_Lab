from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, loginID, password=None):
        if not loginID:
            raise ValueError('Users must have an loginID address')

        user = self.model(
            loginID=self.normalize_email(loginID),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, loginID, password):
        user = self.create_user(
            loginID,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, loginID, password):
        user = self.create_user(
            loginID,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    class Meta:
        db_table = 'userScertification'

    name = models.CharField(max_length=500)
    loginID = models.CharField(max_length=20, unique=True)
    createDate = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    # towns = ListCharField(
    #     models.CharField(max_length=10),size=6, max_length=(6 * 11))

    USERNAME_FIELD = 'loginID'
    objects = UserManager()

    def __str__(self):
        return self.loginID

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class ImageUpload(models.Model):
    class Meta:
        db_table = 'goods'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    mainimg = models.ImageField(upload_to="images")  # こちらの通り
    img1 = models.ImageField(upload_to="images", default='/images/no_image_square.jpg')
    img2 = models.ImageField(upload_to="images", default='/images/no_image_square.jpg')
    img3 = models.ImageField(upload_to="images", default='/images/no_image_square.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

# class Thread(models.Model):
#     goodsid = models.ForeignKey(ImageUpload, on_delete=models.CASCADE)
#     content  = models.TextField(blank=False, null=False)
#     user     = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_datetime = models.DateTimeField(auto_now_add=True)
#     updated_datetime = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.title

class Comment(models.Model):
    comment = models.TextField(blank=False, null=False)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    thread  = models.ForeignKey(ImageUpload, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.comment