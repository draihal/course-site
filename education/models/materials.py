# from django.db import models
#
# from .lesson import Lesson
#
#
# class Materials(models.Model):
#     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
#     # TODO polymorphic
#
#     class Meta:
#         verbose_name = 'Материал'
#         verbose_name_plural = 'Материалы'
#
#     # def __str__(self):
#     #     return self.name
