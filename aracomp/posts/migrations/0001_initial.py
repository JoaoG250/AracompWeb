# Generated by Django 3.2.2 on 2021-05-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('P', 'Palestras'), ('H', 'Hackathon'), ('M', 'Minicursos')], max_length=1, verbose_name='Tipo de Postagem')),
                ('title', models.CharField(max_length=120, verbose_name='Título')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('content', models.TextField(max_length=1500, verbose_name='Conteúdo')),
                ('image', models.CharField(max_length=200, verbose_name='Path da imagem em static')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
        ),
    ]
