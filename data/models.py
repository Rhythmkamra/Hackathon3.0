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
    
    EVENT_TYPE_DEFAULT = 'cultural'  # Default value for event_type
    EVENT_NAME_DEFAULT = 'Cultural Event'  # Default value for event_name
    EVENT_DESC_DEFAULT = 'This is a cultural event.'  # Default value for event_description

    name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)  # Added default value for name
    rollno = models.CharField(max_length=20, default='')  # Example default value for rollno (you can change it)
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)  # Added default value for event_name
    event_description = models.TextField(default=EVENT_DESC_DEFAULT)  # Added default value for event_description
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    is_active = models.BooleanField(default=True)  # Default field
    
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
    
    EVENT_TYPE_DEFAULT = 'cultural'  # Default value for event_type
    EVENT_NAME_DEFAULT = 'Sports Event'  # Default value for event_name
    EVENT_DESC_DEFAULT = 'This is a sports event.'  # Default value for event_description

    name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)  # Added default value for name
    rollno = models.CharField(max_length=20, default='')  # Example default value for rollno (you can change it)
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)  # Added default value for event_name
    event_description = models.TextField(default=EVENT_DESC_DEFAULT)  # Added default value for event_description
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    is_active = models.BooleanField(default=True)  # Default field
    
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
    
    EVENT_TYPE_DEFAULT = 'cultural'  # Default value for event_type
    EVENT_NAME_DEFAULT = 'Technical Event'  # Default value for event_name
    EVENT_DESC_DEFAULT = 'This is a technical event.'  # Default value for event_description

    name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)  # Added default value for name
    rollno = models.CharField(max_length=20, default='')  # Example default value for rollno (you can change it)
    year = models.IntegerField(choices=YEAR_CHOICES)
    event_name = models.CharField(max_length=100, default=EVENT_NAME_DEFAULT)  # Added default value for event_name
    event_description = models.TextField(default=EVENT_DESC_DEFAULT)  # Added default value for event_description
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default=EVENT_TYPE_DEFAULT)
    intercollege_mcq = models.BooleanField(default=False)
    intracollege_mcq = models.BooleanField(default=False)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    is_active = models.BooleanField(default=True)  # Default field
    
    def __str__(self):
        return self.name    
