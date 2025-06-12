from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0001_initial'),  # Replace '000X_previous_migration' with the actual dependency
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True),
        ),
    ]
