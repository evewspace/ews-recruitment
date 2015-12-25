# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voteactionlog',
            name='voter',
            field=models.ForeignKey(related_name='ro_votes_for', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interview',
            name='application',
            field=models.ForeignKey(related_name='interviews', to='Recruitment.Application'),
        ),
        migrations.AddField(
            model_name='interview',
            name='interviewer',
            field=models.ForeignKey(related_name='interviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appvote',
            name='application',
            field=models.ForeignKey(related_name='votes', to='Recruitment.Application'),
        ),
        migrations.AddField(
            model_name='appvote',
            name='vote',
            field=models.ForeignKey(related_name='appvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apptype',
            name='accept_group',
            field=models.ForeignKey(related_name='applications', to='auth.Group', null=True),
        ),
        migrations.AddField(
            model_name='apptype',
            name='use_standings',
            field=models.ForeignKey(related_name='applications', to='core.Corporation', null=True),
        ),
        migrations.AddField(
            model_name='appstage',
            name='app_type',
            field=models.ForeignKey(related_name='stages', to='Recruitment.AppType'),
        ),
        migrations.AddField(
            model_name='appresponse',
            name='application',
            field=models.ForeignKey(related_name='responses', to='Recruitment.Application'),
        ),
        migrations.AddField(
            model_name='appresponse',
            name='question',
            field=models.ForeignKey(related_name='responses', to='Recruitment.AppQuestion'),
        ),
        migrations.AddField(
            model_name='appquestionchoice',
            name='question',
            field=models.ForeignKey(related_name='choices', to='Recruitment.AppQuestion'),
        ),
        migrations.AddField(
            model_name='appquestion',
            name='app_stage',
            field=models.ForeignKey(related_name='questions', to='Recruitment.AppStage'),
        ),
        migrations.AddField(
            model_name='appquestion',
            name='app_type',
            field=models.ForeignKey(related_name='questions', to='Recruitment.AppType'),
        ),
        migrations.AddField(
            model_name='application',
            name='app_type',
            field=models.ForeignKey(related_name='applications', to='Recruitment.AppType'),
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(related_name='applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='closed_by',
            field=models.ForeignKey(related_name='applications_closed', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='appcomment',
            name='application',
            field=models.ForeignKey(related_name='ro_comments', to='Recruitment.Application'),
        ),
        migrations.AddField(
            model_name='appcomment',
            name='author',
            field=models.ForeignKey(related_name='ro_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='actionentry',
            name='action',
            field=models.ForeignKey(to='Recruitment.Action'),
        ),
        migrations.AddField(
            model_name='actionentry',
            name='application',
            field=models.ForeignKey(to='Recruitment.Application'),
        ),
        migrations.AlterUniqueTogether(
            name='voteactionlog',
            unique_together=set([('action_entry', 'voter')]),
        ),
        migrations.AddField(
            model_name='countersignaction',
            name='approver1',
            field=models.ForeignKey(related_name='counter_approve1', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='countersignaction',
            name='approver2',
            field=models.ForeignKey(related_name='counter_approve2', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='approvalaction',
            name='approver',
            field=models.ForeignKey(related_name='ro_approvals', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='actionentry',
            unique_together=set([('action', 'application')]),
        ),
    ]
