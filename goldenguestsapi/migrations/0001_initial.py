# Generated by Django 4.1.7 on 2023-03-10 20:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GoldenGuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isTicketHolder', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3)])),
                ('number_of_tickets', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('date', models.DateField(blank=True, null=True)),
                ('goldenguest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goldenguestsapi.goldenguest')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goldenguestsapi.opponent')),
            ],
        ),
        migrations.CreateModel(
            name='OrgTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goldenguest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goldenguestsapi.goldenguest')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goldenguestsapi.ticket')),
            ],
        ),
    ]
