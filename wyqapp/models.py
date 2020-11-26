from django.db import models

# makemigrations
# migrate


class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = 'BaseTable'
# Create your models here.
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)



class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE, )

    class Meta:
        db_table = "students"
        ordering = ['id']

class ages(BaseTable):
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    isDelete = models.BooleanField(default=False)

    def ages_info(self):
        d={self.sname:self.sage}
        return d
    class Meta:
        db_table = "ages"
        ordering = ['id']