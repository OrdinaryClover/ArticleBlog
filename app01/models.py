from django.db import models
# Create your models here.
##RichTextField  底层是TextField  只是修改了前端的样式，能够将输入的内容以HTML的格式进行重新排版
from ckeditor.fields import RichTextField
###支持文件上传
from ckeditor_uploader.fields import RichTextUploadingField



GENDER_STATUS = (
    (0,"女"),
    (1,"男"),
)

class Author(models.Model):
    name = models.CharField(max_length=32,verbose_name="作者姓名")
    # gender = models.CharField(choices=GENDER_STATUS,max_length=32,verbose_name="性别")
    gender1 = models.IntegerField(choices=GENDER_STATUS,verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    email = models.EmailField(verbose_name="邮箱")

    def __str__(self):
        return self.name
    class Meta:
        db_table = "author"
        verbose_name_plural = "作者名单"

class Type(models.Model):
    name = models.CharField(max_length=32,verbose_name="类型名字")
    description = models.TextField(verbose_name="描述")

    def __str__(self):
        return self.name
    class Meta:
        db_table = "type"
        verbose_name_plural = "类型"

class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name="标题")
    date = models.DateField(auto_now=True,verbose_name="创建时间")
    # content = models.TextField(verbose_name="内容")
    # description = models.TextField(verbose_name="文章描述")
    # content = RichTextField(verbose_name="内容")
    content = RichTextUploadingField(verbose_name="内容")
    description = RichTextField(verbose_name="描述")

    ##由upload_to决定了图片上传的路径  static/images/
    picture = models.ImageField(upload_to="images",verbose_name="图片")
    recommend = models.IntegerField(verbose_name="图文推荐")  #1：推荐 0：不推荐
    click = models.IntegerField(verbose_name="点击率")
    author = models.ForeignKey(to=Author,to_field="id",on_delete=models.CASCADE)
    type = models.ManyToManyField(to=Type)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "article"
        verbose_name_plural = "文章合集"

class User(models.Model):
    username = models.CharField(max_length=32,verbose_name="用户名")
    password = models.CharField(max_length=32,verbose_name="密码")
    create_time = models.DateTimeField(auto_now=True,verbose_name="创建时间")
    class Meta:
        db_table = "user"