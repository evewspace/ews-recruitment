# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('required', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('action_type', models.IntegerField(default=1, choices=[(1, b'Approval'), (2, b'Countersign'), (3, b'Vote')])),
                ('visible', models.BooleanField(default=True)),
                ('required_votes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ActionEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AppComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('closetime', models.DateTimeField(null=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 12, 25, 19, 57, 18, 899715, tzinfo=utc))),
                ('submitted', models.DateTimeField(null=True)),
                ('disposition', models.IntegerField(null=True, choices=[(0, b'Duplicate'), (1, b'Accepted'), (2, b'Rejected'), (3, b'Deferred')])),
                ('status_text', models.TextField(null=True)),
            ],
            options={
                'permissions': (('can_recruit', 'Can view applications'), ('recruitment_admin', 'Can administer the RO tool.')),
            },
        ),
        migrations.CreateModel(
            name='AppQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=255)),
                ('question_type', models.IntegerField(choices=[(1, b'Text Field'), (2, b'Text Box'), (3, b'Radio'), (4, b'Checkbox')])),
                ('description', models.TextField(null=True, blank=True)),
                ('required', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=1)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='AppQuestionChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('response', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('order', models.IntegerField(default=1)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='AppType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('instructions', models.TextField(null=True, blank=True)),
                ('require_account', models.BooleanField(default=False)),
                ('disable_user_on_failure', models.BooleanField(default=False)),
                ('purge_api_on_failure', models.BooleanField(default=False)),
                ('required_votes', models.IntegerField(default=1)),
                ('accept_mail', models.TextField(null=True)),
                ('accept_subject', models.CharField(max_length=255, null=True)),
                ('reject_mail', models.TextField(null=True)),
                ('reject_subject', models.CharField(max_length=255, null=True)),
                ('defer_mail', models.TextField(null=True)),
                ('defer_subject', models.CharField(max_length=255, null=True)),
                ('visible', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AppVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disposition', models.IntegerField(choices=[(1, b'Accept'), (2, b'Reject'), (3, b'Defer')])),
                ('note', models.TextField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chatlog', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StandigsRequirement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entity', models.CharField(max_length=100)),
                ('standing', models.FloatField(null=True, blank=True)),
                ('entitytype', models.IntegerField(choices=[(0, b'Corporation'), (1, b'Faction')])),
            ],
        ),
        migrations.CreateModel(
            name='VoteActionLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.IntegerField(null=True, choices=[(0, b'Against'), (1, b'For')])),
                ('comment', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApprovalAction',
            fields=[
                ('action_entry', models.OneToOneField(parent_link=True, related_name='approval_info', primary_key=True, serialize=False, to='Recruitment.ActionEntry')),
                ('approval_comment', models.TextField(null=True, blank=True)),
                ('approval_time', models.DateTimeField(null=True)),
            ],
            bases=('Recruitment.actionentry',),
        ),
        migrations.CreateModel(
            name='CountersignAction',
            fields=[
                ('action_entry', models.OneToOneField(parent_link=True, related_name='countersign_info', primary_key=True, serialize=False, to='Recruitment.ActionEntry')),
                ('approver1_comment', models.TextField(null=True, blank=True)),
                ('approver1_time', models.DateTimeField(null=True)),
                ('approver2_comment', models.TextField(null=True, blank=True)),
                ('approver2_time', models.DateTimeField(null=True)),
            ],
            bases=('Recruitment.actionentry',),
        ),
        migrations.AddField(
            model_name='voteactionlog',
            name='action_entry',
            field=models.ForeignKey(related_name='vote_info', to='Recruitment.ActionEntry'),
        ),
    ]
