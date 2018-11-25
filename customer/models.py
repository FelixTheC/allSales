from django.db import models


class Producttype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    generation = models.TextField(blank=True, null=True)
    typ = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    hatantenne = models.NullBooleanField()
    hatbatterie = models.NullBooleanField()
    hatbeacon = models.NullBooleanField()
    hatdropoff = models.NullBooleanField()
    hatgehaeuse = models.NullBooleanField()
    hatgurt = models.NullBooleanField()
    hatradiokommunikation = models.NullBooleanField()
    hatlongrangekommunikation = models.NullBooleanField()
    hatexternesensoren = models.NullBooleanField()
    hatcottonspacer = models.NullBooleanField()
    batterien_id = models.IntegerField(blank=True, null=True)
    gurtdicken_id = models.IntegerField(blank=True, null=True)
    gehaeuse_id = models.IntegerField(blank=True, null=True)
    elektronikkonfigurationseinstellungen_id = models.IntegerField(blank=True, null=True)
    gurtfarben_id = models.IntegerField(blank=True, null=True)
    gurtbreiten_id = models.IntegerField(blank=True, null=True)
    gurtformen_id = models.IntegerField(blank=True, null=True)
    gurtkanten_id = models.IntegerField(blank=True, null=True)
    gurtverbinder_id = models.IntegerField(blank=True, null=True)
    antennen_id = models.IntegerField(blank=True, null=True)
    comtypes_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'ProductType'


# class Shortrangecomtype(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     obsolete = models.NullBooleanField()
#
#     class Meta:
#         managed = False
#         db_table = 'ShortRangeComType'
#
#
# class Configfile(models.Model):
#     id = models.IntegerField(primary_key=True)
#     addedtimestamp = models.DateTimeField(blank=True, null=True)
#     filetext = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ConfigFile'
#
#
# class Customerproject(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     projectid = models.TextField(blank=True, null=True)
#     customerrefno = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'CustomerProject'

# Create your models here.
class Vasdevice(models.Model):
    id = models.IntegerField(primary_key=True)
    serialno = models.BigIntegerField(unique=True, blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    beltlabel = models.NullBooleanField()
    beltlabeltext = models.TextField(blank=True, null=True)
    comid = models.TextField(blank=True, null=True)
    deviceweight = models.FloatField(blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    longrangeiccid = models.TextField(blank=True, null=True)
    longrangeimei = models.TextField(blank=True, null=True)
    longrangeimsi = models.TextField(blank=True, null=True)
    longrangepin = models.TextField(blank=True, null=True)
    longrangepin2 = models.TextField(blank=True, null=True)
    longrangepuk = models.TextField(blank=True, null=True)
    longrangepuk2 = models.TextField(blank=True, null=True)
    longrangeservicestarted = models.DateTimeField(blank=True, null=True)
    longrangesubscription = models.IntegerField(blank=True, null=True)
    longrangeregistered = models.NullBooleanField()
    longrangeregistertime = models.DateTimeField(blank=True, null=True)
    longrangeunregistertime = models.DateTimeField(blank=True, null=True)
    shortrangefrequencytx = models.TextField(blank=True, null=True)
    shortrangefrequencyrx = models.TextField(blank=True, null=True)
    hasbeacon = models.NullBooleanField()
    beaconfrequency = models.TextField(blank=True, null=True)
    hasdropoff = models.NullBooleanField()
    dropoffradiocontrolled = models.NullBooleanField()
    dropofftimercontrolled = models.NullBooleanField()
    dropofftimercontrolledabsolute = models.NullBooleanField()
    dropofftimercontrolledrelative = models.NullBooleanField()
    dropofftimercontrollvalue = models.TextField(blank=True, null=True)
    dropoffinternal = models.NullBooleanField()
    dropoffexternal = models.NullBooleanField()
    comment = models.TextField(blank=True, null=True)
    shippingdate = models.DateTimeField(blank=True, null=True)
    protectivebelt = models.NullBooleanField()
    dropoffcode = models.TextField(blank=True, null=True)
    batteryname = models.TextField(blank=True, null=True)
    batteryscrewthread = models.IntegerField(blank=True, null=True)
    beltpunchingplus = models.IntegerField(blank=True, null=True)
    beltpunchingplusspace = models.TextField(blank=True, null=True)
    beltpunchingminus = models.IntegerField(blank=True, null=True)
    beltpunchingminusspace = models.TextField(blank=True, null=True)
    beltlength = models.TextField(blank=True, null=True)
    customer = models.TextField(blank=True, null=True)
    customeremailaddress = models.TextField(blank=True, null=True)
    customeradditionalinformation = models.TextField(blank=True, null=True)
    customercontact = models.TextField(blank=True, null=True)
    customercountry = models.TextField(blank=True, null=True)
    customerorganization = models.TextField(blank=True, null=True)
    customerphone = models.TextField(blank=True, null=True)
    customerrefno = models.TextField(blank=True, null=True)
    longrangesubscriptioncustomeremailaddress = models.TextField(blank=True, null=True)
    longrangesubscriptioncustomer = models.TextField(blank=True, null=True)
    longrangepayment = models.TextField(blank=True, null=True)
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING, blank=True, null=True)
    # longrangecomprovider = models.ForeignKey('Comprovider', models.DO_NOTHING, blank=True, null=True)
    # longrangecomtype = models.ForeignKey('Comtype', models.DO_NOTHING, blank=True, null=True)
    # pcbtype = models.ForeignKey('Pcbtype', models.DO_NOTHING, blank=True, null=True)
    # shortrangecomtype = models.ForeignKey(Shortrangecomtype, models.DO_NOTHING, blank=True, null=True)
    # animalspecies = models.ForeignKey('Animalspecies', models.DO_NOTHING, blank=True, null=True)
    # configfile = models.ForeignKey(Configfile, models.DO_NOTHING, blank=True, null=True)
    # beltcolor = models.ForeignKey('Beltcolors', models.DO_NOTHING, blank=True, null=True)
    # beltedge = models.ForeignKey('Beltedges', models.DO_NOTHING, blank=True, null=True)
    # beltfastener = models.ForeignKey('Beltfastener', models.DO_NOTHING, blank=True, null=True)
    # beltshape = models.ForeignKey('Beltshapes', models.DO_NOTHING, blank=True, null=True)
    # beltthickness = models.ForeignKey('Beltthickness', models.DO_NOTHING, blank=True, null=True)
    # beltwidth = models.ForeignKey('Beltwidths', models.DO_NOTHING, blank=True, null=True)
    # customerproject = models.ForeignKey(Customerproject, models.DO_NOTHING, blank=True, null=True)
    # antenna = models.ForeignKey('Antennas', models.DO_NOTHING, blank=True, null=True)
    locked = models.NullBooleanField()
    cottonspacer = models.IntegerField(blank=True, null=True)

    def get_full_name(self):
        return self.serialno

    def __str__(self):
        return str(self.serialno) + ", "

    class Meta:
        managed = False
        db_table = 'VasDevice'
        ordering =['serialno']


