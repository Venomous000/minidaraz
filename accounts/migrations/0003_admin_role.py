# Generated by Django 5.2.3 on 2025-06-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_user_address_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="admin",
            name="role",
            field=models.CharField(
                choices=[
                    ("superadmin", "Super Admin"),
                    ("manager", "Manager"),
                    ("staff", "Staff"),
                ],
                default="staff",
                max_length=20,
            ),
        ),
    ]
