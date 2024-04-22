from django.contrib.auth.models import AbstractUser
from django.db import models

# Patients表
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    medical_history = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# GameSessions表
class GameSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    performance_metrics = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.patient.name} Session on {self.start_time.strftime('%Y-%m-%d')}"

# Games表
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

# ProgressTracking表
class ProgressTracking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    date = models.DateField()
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    physician_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Progress for {self.patient.name} on {self.date.strftime('%Y-%m-%d')}"

# Therapists表
class Therapist(AbstractUser):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    contact_info = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# PatientTherapistRelation表
class PatientTherapistRelation(models.Model):
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.therapist.name} - {self.patient.name}"

# 如果您有一个特定的索引需求，或者需要设置数据库特有的选项，可以在Meta子类中设置
# class GameSession(models.Model):
#     # ...
#     class Meta:
#         indexes = [
#             models.Index(fields=['patient_id'], name='idx_patient_id'),
#             models.Index(fields=['game_id'], name='idx_game_id'),
#         ]
