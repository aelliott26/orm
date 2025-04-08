from django.db import models

# Create your models here.

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone_num = models.TextField()
    birthday = models.DateField()
    m_level = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PersonalTrainer(models.Model):
    trainer_id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    phone_num = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateField()
    payment_type = models.TextField()

    def __str__(self):
        return f"Payment ID {self.member.first_name}: ${self.amount}"


class CheckIn(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField()

    def __str__(self):
        return f"Check-In by {self.member.first_name} on {self.checkin_date}"


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    class_dt = models.DateTimeField()
    trainer = models.ForeignKey(PersonalTrainer, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Class ID {self.class_id}: {self.description}"


class SignUp(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    class_instance = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"Member {self.member.first_name} signed up for Class ID {self.class_instance.class_id}"
