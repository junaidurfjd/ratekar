from django.db import models
from django.conf import settings 
from django.core.validators import MaxValueValidator, MinValueValidator
from social.models import Friendship


class Reputation(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'myRatings')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendsRatings')
	reputation = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(10)])

class Review(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'myReviews')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendsReviews')
	review = models.CharField(max_length = 200)
	liked = models.BooleanField(default = False)

	created_on = models.DateField(auto_now_add = True)
	updated_on = models.DateField(auto_now = True)

class Trait(models.Model):
	title  = models.CharField(max_length = 15)
	description  = models.CharField(max_length = 100)

class TraityQuestion(models.Model):
	trait = models.ForeignKey(Trait)
	text = models.CharField(max_length = 100)
	min_cat = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(4)])

class Feedback(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'myFeedbacks')
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'friendsFeedbacks')
	question = models.ForeignKey(TraityQuestion)
	rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])




