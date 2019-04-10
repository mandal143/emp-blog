from django.db import models



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
class Employee(models.Model):
    emp_name = models.CharField(max_length=200)
    emp_age = models.IntegerField(default=1)
    emp_salary = models.IntegerField(default=1000)
    
    def __str__(self):
        return self.emp_name
        
        
class Event(models.Model):
    event_name = models.CharField(max_length=200,default="")
    no_of_people = models.IntegerField(default=1)
   
    start_date = models.DateField(u'Start Day of the event', help_text=u'Start Day of the event')
    end_date = models.DateField(u'End Day of the event', help_text=u' End First Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    def __str__(self):
        return str(self.event_name)
    
 


    
    
    