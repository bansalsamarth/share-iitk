from django.db import models

class FileData(models.Model):
	course_name = models.CharField(max_length = 50)	
	department_code = models.CharField(max_length = 5)
	course_code = models.CharField(max_length = 6)
	category = models.CharField(max_length = 10)
	year = models.IntegerField(blank = True, null = True)
	professor = models.CharField(max_length = 30, blank = True)
	description = models.TextField()
	approved = models.CharField(max_length = 1, default = 'P')
	file_url = models.CharField(max_length = 100)

	uploader_name = models.CharField(max_length = 40, blank = True)
	uploader_email = models.EmailField(blank = True)