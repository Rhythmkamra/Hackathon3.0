from django.db import models

class Student_cultural(models.Model):
    YEAR_CHOICES = (
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    )

    EVENT_TYPE_CHOICES = (
        ('national', 'National'),
        ('state', 'State'),
        ('district', 'District'),
    )

    POSITION_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('none', 'None'),
    )

    EVENT_TYPE_DEFAULT = 'cultural'
    EVENT_NAME_DEFAULT = 'Cultural Event'
    EVENT_DESC_DEFAULT = 'This is a cultural event.'

    name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)
    rollno = models.CharField(max_length=20, default='')
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)
    event_description = models.TextField(default=EVENT_DESC_DEFAULT)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)  # New field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Student_sports(models.Model):
    YEAR_CHOICES = (
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    )

    EVENT_TYPE_CHOICES = (
        ('national', 'National'),
        ('state', 'State'),
        ('district', 'District'),
    )

    POSITION_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('none', 'None'),
    )

    EVENT_TYPE_DEFAULT = 'sports'
    EVENT_NAME_DEFAULT = 'Sports Event'
    EVENT_DESC_DEFAULT = 'This is a sports event.'

    name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)
    rollno = models.CharField(max_length=20, default='')
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)
    event_description = models.TextField(default=EVENT_DESC_DEFAULT)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)  # New field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Student_technical(models.Model):
    YEAR_CHOICES = (
        (1, 'First Year'),
        (2, 'Second Year'),
        (3, 'Third Year'),
        (4, 'Fourth Year'),
    )

    EVENT_TYPE_CHOICES = (
        ('national', 'National'),
        ('state', 'State'),
        ('district', 'District'),
    )

    POSITION_CHOICES = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
        ('none', 'None'),
    )

    EVENT_TYPE_DEFAULT = 'technical'
    EVENT_NAME_DEFAULT = 'Technical Event'
    EVENT_DESC_DEFAULT = 'This is a technical event.'

    name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)
    rollno = models.CharField(max_length=20, default='')
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)
    event_description = models.TextField(default=EVENT_DESC_DEFAULT)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)  # New field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
