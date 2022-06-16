from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_alive = models.BooleanField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%H: %M: %S')}"

    class Meta:
        # to for time
        ordering = ('-created_at',)
        # to turn the Test Models to Singular
        verbose_name_plural = 'Test Model'


class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name="text_content")
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_content.name} - {self.mileage}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = "ModelX"
