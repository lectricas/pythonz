# Generated by Django 3.1.2 on 2020-10-31 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pythonz.apps.generics.models
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0054_auto_20200421_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(help_text='Предпочтительно имя и фамилия. Можно указать несколько, разделяя запятыми.<br><b>[u:<ид>:<имя>]</b> формирует ссылку на профиль пользователя pythonz. Например: [u:1:идле].', max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='historicalbook',
            name='author',
            field=models.CharField(help_text='Предпочтительно имя и фамилия. Можно указать несколько, разделяя запятыми.<br><b>[u:<ид>:<имя>]</b> формирует ссылку на профиль пользователя pythonz. Например: [u:1:идле].', max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='historicalvideo',
            name='author',
            field=models.CharField(help_text='Предпочтительно имя и фамилия. Можно указать несколько, разделяя запятыми.<br><b>[u:<ид>:<имя>]</b> формирует ссылку на профиль пользователя pythonz. Например: [u:1:идле].', max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='video',
            name='author',
            field=models.CharField(help_text='Предпочтительно имя и фамилия. Можно указать несколько, разделяя запятыми.<br><b>[u:<ид>:<имя>]</b> формирует ссылку на профиль пользователя pythonz. Например: [u:1:идле].', max_length=255, verbose_name='Автор'),
        ),
        migrations.CreateModel(
            name='HistoricalApp',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('author', models.CharField(help_text='Предпочтительно имя и фамилия. Можно указать несколько, разделяя запятыми.<br><b>[u:<ид>:<имя>]</b> формирует ссылку на профиль пользователя pythonz. Например: [u:1:идле].', max_length=255, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text_src', models.TextField(verbose_name='Исходный текст')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, db_index=True, max_length=200, null=True, verbose_name='Краткое имя для URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cover', models.TextField(blank=True, max_length=255, null=True, verbose_name='Обложка')),
                ('year', models.CharField(blank=True, max_length=10, null=True, verbose_name='Год')),
                ('time_created', models.DateTimeField(blank=True, editable=False, verbose_name='Дата создания')),
                ('time_published', models.DateTimeField(editable=False, null=True, verbose_name='Дата публикации')),
                ('time_modified', models.DateTimeField(editable=False, null=True, verbose_name='Дата редактирования')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Черновик'), (2, 'Опубликован'), (3, 'Удален'), (4, 'В архиве'), (5, 'К отложенной публикации')], default=1, verbose_name='Статус')),
                ('supporters_num', models.PositiveIntegerField(default=0, verbose_name='Поддержка')),
                ('repo', models.URLField(blank=True, db_index=True, help_text='URL, по которому доступен исходный код приложения.', null=True, verbose_name='Репозиторий')),
                ('downloads', models.JSONField(default=dict, verbose_name='Загрузки')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('last_editor', models.ForeignKey(blank=True, db_constraint=False, default=1, help_text='Пользователь, последним отредактировавший объект.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Редактор')),
                ('submitter', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Добавил')),
            ],
            options={
                'verbose_name': 'historical Приложение',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(help_text='Предпочтительно имя и фамилия. Можно указать несколько, разделяя запятыми.<br><b>[u:<ид>:<имя>]</b> формирует ссылку на профиль пользователя pythonz. Например: [u:1:идле].', max_length=255, verbose_name='Автор')),
                ('text', models.TextField(verbose_name='Текст')),
                ('text_src', models.TextField(verbose_name='Исходный текст')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Краткое имя для URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('cover', models.ImageField(blank=True, max_length=255, null=True, upload_to=pythonz.apps.generics.models.get_upload_to, verbose_name='Обложка')),
                ('year', models.CharField(blank=True, max_length=10, null=True, verbose_name='Год')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_published', models.DateTimeField(editable=False, null=True, verbose_name='Дата публикации')),
                ('time_modified', models.DateTimeField(editable=False, null=True, verbose_name='Дата редактирования')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Черновик'), (2, 'Опубликован'), (3, 'Удален'), (4, 'В архиве'), (5, 'К отложенной публикации')], default=1, verbose_name='Статус')),
                ('supporters_num', models.PositiveIntegerField(default=0, verbose_name='Поддержка')),
                ('repo', models.URLField(blank=True, help_text='URL, по которому доступен исходный код приложения.', null=True, unique=True, verbose_name='Репозиторий')),
                ('downloads', models.JSONField(default=dict, verbose_name='Загрузки')),
                ('authors', models.ManyToManyField(blank=True, related_name='apps', to='apps.Person', verbose_name='Авторы')),
                ('last_editor', models.ForeignKey(blank=True, default=1, help_text='Пользователь, последним отредактировавший объект.', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='app_editors', to=settings.AUTH_USER_MODEL, verbose_name='Редактор')),
                ('linked', models.ManyToManyField(blank=True, help_text='Выберите объекты, имеющие отношение к данному.', related_name='_app_linked_+', to='apps.App', verbose_name='Связанные объекты')),
                ('submitter', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='app_submitters', to=settings.AUTH_USER_MODEL, verbose_name='Добавил')),
            ],
            options={
                'verbose_name': 'Приложение',
                'verbose_name_plural': 'Приложения',
            },
        ),
    ]
