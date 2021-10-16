from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


class CaseModel(models.Model):
    CHOICES = (
        ('пшеница', 'пшеница'), ('семечка', 'семечка'), ('майонез', 'майонез'), ('овес', 'овес'), ('жмых', 'жмых'),
        ('кусочек сыра', 'кусочек сыра')
    )
    ROLES = (('КФХ', 'КФХ'), ('АГЕНТ', 'АГЕНТ'))

    role = models.CharField(max_length=20, choices=ROLES)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    farmerName = models.CharField(max_length=150)
    companyName = models.CharField(max_length=150)
    phone = models.CharField(max_length=40)
    address = models.CharField(max_length=250, blank=True, null=True)
    tegName = MultiSelectField(choices=CHOICES)
    mail = models.EmailField(null=True, blank=True)
    date_open = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey('StatusModel', on_delete=models.CASCADE, null=True)

    def as_json(self):
        return dict(
            id=self.id, farmerName=self.farmerName, companyName=self.companyName,
            phone=self.phone, address=self.address, tegName=self.tegName, mail=self.mail, date_open=self.date_open,
        )


class CommentModel(models.Model):
    case = models.ForeignKey(CaseModel, on_delete=models.CASCADE, null=True, related_name="comments")
    date_created = models.DateTimeField(auto_now_add=True)
    text_comment = models.TextField(max_length=300)

    def as_json(self):
        return dict(
            date_created=self.date_created, text_comment=self.text_comment
        )


class StatusModel(models.Model):
    status = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    is_active = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        description = str(self.status)
        return description

    def as_json(self):
        return dict(
            status=self.status, is_active=self.is_active
        )
