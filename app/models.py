from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=123, verbose_name='Название')
    parent_title = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        full_path = [self.title]
        k = self.parent_title
        while k is not None:
            full_path.append(k.title)
            k = k.parent_title
        return ' -> '.join(full_path[::-1])




