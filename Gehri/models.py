# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
	question_text = models.CharField(max_length=499)
	pub_date = models.DateTimeField('datetime')
	def __str__(self):
		return self.question_text
@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length = 243)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

