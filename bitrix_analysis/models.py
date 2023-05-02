from django.db import models


class RuSitesAll(models.Model):
    class Meta:
        managed = False
        db_table = 'ru_sites_all'

    id = models.IntegerField(primary_key=True)
    domain = models.TextField(blank=True, null=True)
    domain = models.TextField()

    def __str__(self):
        return self.domain


class BitrixOnSites(models.Model):
    id = models.ForeignKey('RuSitesAll', models.DO_NOTHING, db_column='id', primary_key=True)
    domain = models.TextField()

    found_bitrix = models.BooleanField(default=False)
    had_redirect = models.BooleanField(default=False)
    status = models.IntegerField()
    error = models.TextField

    def __str__(self):
        return f'id:{self.domain} {self.found_bitrix}'

    class Meta:
        managed = False
        db_table = 'bitrix_on_sites'


