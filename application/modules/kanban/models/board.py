from django.conf import settings
from django.db import models


class Board(models.Model):
    # 所有者
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ボード名
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} of {}'.format(self.pk, self.name, self.owner)

    @classmethod
    def get_list_by_owner(cls, owner):
        return list(cls.objects.filter(owner=owner).order_by('updated_at'))