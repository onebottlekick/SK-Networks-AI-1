# Generated by Django 5.0.6 on 2024-06-14 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccountLoginType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "loginType",
                    models.CharField(choices=[("KAKAO", "Kakao")], max_length=10),
                ),
            ],
            options={
                "db_table": "account_login_type",
            },
        ),
        migrations.CreateModel(
            name="AccountRoleType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("roleType", models.CharField(max_length=64)),
            ],
            options={
                "db_table": "account_role_type",
            },
        ),
        migrations.CreateModel(
            name="Account",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "loginType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.accountlogintype",
                    ),
                ),
                (
                    "roleType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.accountroletype",
                    ),
                ),
            ],
            options={
                "db_table": "account",
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nickname", models.CharField(max_length=64, unique=True)),
                ("email", models.CharField(max_length=64, unique=True)),
                (
                    "account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.account",
                    ),
                ),
            ],
            options={
                "db_table": "profile",
            },
        ),


    ]
