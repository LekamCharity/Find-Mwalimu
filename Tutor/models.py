from django.db import models

# Create your models here.

class Experience(models.Model):
    experience_level = models.CharField(max_length=60)

    def __str__(self):
        return self.experience_level

class Language(models.Model):
    language_name = models.CharField(max_length=60)

    def __str__(self):
        return self.language_name

class Tutor(models.Model):
    tutor_name = models.CharField(max_length=60)
    tutor_email = models.CharField(max_length=60)
    tutor_bio = models.TextField()
    languages = models.ManyToManyField(Language)
    programming_experience = models.ForeignKey(Experience, null=True,  on_delete=models.CASCADE)
    tutor_image = models.ImageField(upload_to = 'profpics/', null=True)
    tutor_location = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.tutor_name

    def save_tutor(self):
        self.save()

    def delete_tutor(self):
        self.delete()

    @classmethod
    def display_tutor(cls):
        tutors=cls.objects.all()
        return tutors

    @classmethod
    def find_tutor_location(cls, search_term):
        tutors=cls.objects.filter(tutor_location__icontains=search_term)
        return tutors

    @classmethod
    def find_tutor_name(cls, search_term):
        tutors=cls.objects.filter(tutor_name__icontains=search_term)
        return tutors

    @classmethod
    def find_programming_experiencee(cls, search_term):
        tutors=cls.objects.filter(programming_experiencee__icontains=search_term)
        return tutors
