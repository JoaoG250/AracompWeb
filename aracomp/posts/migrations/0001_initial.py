# Generated by Django 3.2.1 on 2021-05-04 23:55

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('P', 'Palestra'), ('H', 'Hackaton'), ('M', 'Minicurso')], max_length=1, verbose_name='Tipo de Postagem')),
                ('title', models.CharField(max_length=120, verbose_name='Título')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('content', models.TextField(max_length=1500, verbose_name='Conteúdo')),
                ('image', models.ImageField(default='default/post_image.png', upload_to=posts.models.post_image_path, verbose_name='Imagem da Postagem')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
        ),
    ]