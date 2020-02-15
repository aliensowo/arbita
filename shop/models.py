from django.db import models

# Create your models here.


class bd_account_fb(models.Model):
    account_bm = models.URLField(name="bm_account")
    account_rec = models.URLField(name="rec_account")


class bd_photoshop_fb(models.Model):
    photoshop_ooo = models.URLField(name="photoshop_ooo")
    photoshop_ip = models.URLField(name="photoshop_ip")
    photoshop_oficce = models.URLField(name="photoshop_oficce")


class bd_other_fb(models.Model):
    other_proxy = models.URLField(name="other_proxy")
    other_bankcard = models.URLField(name="other_bankcard")


class bd_promocode(models.Model):
    promo_company1 = models.CharField(max_length=128, name="company1")