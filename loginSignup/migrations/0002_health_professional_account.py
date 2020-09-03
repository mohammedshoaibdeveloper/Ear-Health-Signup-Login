# Generated by Django 3.1.1 on 2020-09-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginSignup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Health_Professional_Account',
            fields=[
                ('Health_Professional_Account_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Full_Name', models.CharField(default='', max_length=100)),
                ('First_Name', models.CharField(default='', max_length=100)),
                ('Last_Name', models.CharField(default='', max_length=100)),
                ('Email', models.EmailField(default='', max_length=100)),
                ('Username', models.CharField(default='', max_length=100)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=100)),
                ('Date_of_Birth', models.DateField(blank=True, null=True)),
                ('Password', models.TextField(default=' ', max_length=3000)),
                ('Degree', models.CharField(default='', max_length=200)),
                ('Affiliation', models.CharField(default='', max_length=200)),
                ('Bio', models.TextField(default='')),
                ('Street_Address', models.CharField(default='', max_length=500)),
                ('City', models.CharField(default='', max_length=500)),
                ('State', models.CharField(default='', max_length=500)),
                ('Country', models.CharField(default='', max_length=500)),
                ('Location', models.CharField(default='', max_length=500)),
                ('Role', models.CharField(default='earhealthprofessional', max_length=100)),
                ('Health_Professional_Image', models.ImageField(default='dummy.jpg', upload_to='Health_Professional/')),
            ],
        ),
    ]
