# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Causasystem(models.Model):
    id = models.IntegerField(primary_key=True)
    deliveryoffsetinweeks = models.IntegerField(blank=True, null=True)
    minimummajorversion = models.IntegerField(blank=True, null=True)
    minimumminorversion = models.IntegerField(blank=True, null=True)
    minimumreleaseversion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CausaSystem'


class Communication(models.Model):
    dbid = models.IntegerField(primary_key=True)
    itemid = models.IntegerField(blank=True, null=True)
    comtype = models.ForeignKey('Comtype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Communication'


class Configfile(models.Model):
    id = models.IntegerField(primary_key=True)
    addedtimestamp = models.DateTimeField(blank=True, null=True)
    filetext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ConfigFile'


class Customergroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomerGroup'


class Customerproject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    projectid = models.TextField(blank=True, null=True)
    customerrefno = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CustomerProject'


class Deviceelectronic(models.Model):
    id = models.IntegerField(primary_key=True)
    serialnumber = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceElectronic'


class Deviceelectroniccfgproperty(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    required = models.NullBooleanField()
    defaultvalue = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    deviceelectronic = models.ForeignKey(Deviceelectronic, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DeviceElectronicCfgProperty'


class Deviceelectronicconfiguration(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'DeviceElectronicConfiguration'


class Dropoff(models.Model):
    id = models.IntegerField(primary_key=True)
    radiocontrolled = models.NullBooleanField()
    timercontrolled = models.NullBooleanField()
    timercontrolledabsolute = models.NullBooleanField()
    timercontrolledrelative = models.NullBooleanField()
    timercontrollvalue = models.CharField(max_length=255, blank=True, null=True)
    dropoffcode = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    internal = models.NullBooleanField()
    external = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'DropOff'


class Housing(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Housing'


class Longrangecommunication(models.Model):
    dbid = models.IntegerField(primary_key=True)
    comidstr = models.TextField(blank=True, null=True)
    registered = models.NullBooleanField()
    comment = models.TextField(blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    register_time = models.DateTimeField(blank=True, null=True)
    unregister_time = models.DateTimeField(blank=True, null=True)
    subscriptioncustomer_email_address = models.TextField(blank=True, null=True)
    customerrefno = models.TextField(blank=True, null=True)
    subscription = models.IntegerField(blank=True, null=True)
    iccid = models.TextField(blank=True, null=True)
    servicestarted = models.DateTimeField(blank=True, null=True)
    imsi = models.TextField(blank=True, null=True)
    pin = models.TextField(blank=True, null=True)
    pin2 = models.TextField(blank=True, null=True)
    puk = models.TextField(blank=True, null=True)
    puk2 = models.TextField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    subscriptioncustomer = models.TextField(blank=True, null=True)
    payment = models.TextField(blank=True, null=True)
    comtype = models.ForeignKey('Comtype', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(Customerproject, models.DO_NOTHING, blank=True, null=True)
    comprovider = models.ForeignKey('Comprovider', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LongRangeCommunication'


class Orderitem(models.Model):
    id = models.IntegerField(primary_key=True)
    eingang = models.NullBooleanField()
    warteaufinformationen = models.NullBooleanField()
    inproduktion = models.NullBooleanField()
    inproduktioninformationenfehlen = models.NullBooleanField()
    bereitauslieferung = models.NullBooleanField()
    ausgeliefert = models.NullBooleanField()
    gurtfertig = models.NullBooleanField()
    batteriefertig = models.NullBooleanField()
    gehaeusefertig = models.NullBooleanField()
    elektronikfertig = models.NullBooleanField()
    zusammenbaufertig = models.NullBooleanField()
    testfertig = models.NullBooleanField()
    konfigurationfertig = models.NullBooleanField()
    bereitauslieferungpapierefertig = models.NullBooleanField()
    anzahl = models.IntegerField(blank=True, null=True)
    beacon = models.NullBooleanField()
    cottonspacerlayer = models.IntegerField(blank=True, null=True)
    duedate = models.DateTimeField(blank=True, null=True)
    gurt = models.ForeignKey('Belt', models.DO_NOTHING, blank=True, null=True)
    batterie = models.ForeignKey('Batteries', models.DO_NOTHING, blank=True, null=True)
    tierart = models.ForeignKey('Animalspecies', models.DO_NOTHING, blank=True, null=True)
    gehaeuse = models.ForeignKey(Housing, models.DO_NOTHING, blank=True, null=True)
    typ = models.ForeignKey('Producttype', models.DO_NOTHING, blank=True, null=True)
    antenne = models.ForeignKey('Antennas', models.DO_NOTHING, blank=True, null=True)
    shippment = models.ForeignKey('Shippments', models.DO_NOTHING, blank=True, null=True)
    estimateddate = models.DateTimeField(blank=True, null=True)
    deviceids = models.TextField(blank=True, null=True)
    elektronik = models.ForeignKey(Deviceelectronic, models.DO_NOTHING, blank=True, null=True)
    shortrangecomtype = models.ForeignKey('Shortrangecomtype', models.DO_NOTHING, blank=True, null=True)
    longcomtype = models.ForeignKey('Comtype', models.DO_NOTHING, blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    beaconfrequencies = models.TextField(blank=True, null=True)
    labelplates = models.NullBooleanField()
    labelplatestext = models.TextField(blank=True, null=True)
    productionBatch = models.ForeignKey('Productionbatch', models.DO_NOTHING, blank=True, null=True)
    dropoff = models.ForeignKey(Dropoff, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrderItem'


class Possibleelectronicconfigurationproperty(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    defaultvalue = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    required = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'PossibleElectronicConfigurationProperty'


class Productelectronicconfigurationproperty(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    defaultvalue = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    required = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ProductElectronicConfigurationProperty'


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

    class Meta:
        managed = False
        db_table = 'ProductType'


class Shortrangecomtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'ShortRangeComType'


class Shortrangecommunication(models.Model):
    id = models.IntegerField(primary_key=True)
    frequencytx = models.TextField(blank=True, null=True)
    frequencyrx = models.TextField(blank=True, null=True)
    shortrangecomtype = models.ForeignKey(Shortrangecomtype, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ShortRangeCommunication'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    loginname = models.TextField(blank=True, null=True)
    initial = models.TextField(blank=True, null=True)
    prename = models.TextField(blank=True, null=True)
    surname = models.TextField(blank=True, null=True)
    productionrecordcounter = models.IntegerField(blank=True, null=True)
    employeid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


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
    longrangecomprovider = models.ForeignKey('Comprovider', models.DO_NOTHING, blank=True, null=True)
    longrangecomtype = models.ForeignKey('Comtype', models.DO_NOTHING, blank=True, null=True)
    pcbtype = models.ForeignKey('Pcbtype', models.DO_NOTHING, blank=True, null=True)
    shortrangecomtype = models.ForeignKey(Shortrangecomtype, models.DO_NOTHING, blank=True, null=True)
    animalspecies = models.ForeignKey('Animalspecies', models.DO_NOTHING, blank=True, null=True)
    configfile = models.ForeignKey(Configfile, models.DO_NOTHING, blank=True, null=True)
    beltcolor = models.ForeignKey('Beltcolors', models.DO_NOTHING, blank=True, null=True)
    beltedge = models.ForeignKey('Beltedges', models.DO_NOTHING, blank=True, null=True)
    beltfastener = models.ForeignKey('Beltfastener', models.DO_NOTHING, blank=True, null=True)
    beltshape = models.ForeignKey('Beltshapes', models.DO_NOTHING, blank=True, null=True)
    beltthickness = models.ForeignKey('Beltthickness', models.DO_NOTHING, blank=True, null=True)
    beltwidth = models.ForeignKey('Beltwidths', models.DO_NOTHING, blank=True, null=True)
    customerproject = models.ForeignKey(Customerproject, models.DO_NOTHING, blank=True, null=True)
    antenna = models.ForeignKey('Antennas', models.DO_NOTHING, blank=True, null=True)
    locked = models.NullBooleanField()
    cottonspacer = models.IntegerField(blank=True, null=True)
    firmware = models.TextField(blank=True, null=True)
    replaces = models.TextField(blank=True, null=True)
    replacedby = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VasDevice'


class Animalspecies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    ordering_id = models.IntegerField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'animalspecies'
        ordering = ['name', ]


class Antennas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antennas'


# class Antennatoproducttype(models.Model):
#     producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
#     antenna_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'antennatoproducttype'


class Batteries(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    hasdropoff = models.NullBooleanField()
    screwthread = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    ordering_id = models.IntegerField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'batteries'


class Batterytoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    battery_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'batterytoproducttype'


class Belt(models.Model):
    id = models.IntegerField(primary_key=True)
    lochung = models.TextField(blank=True, null=True)
    beschriftung = models.NullBooleanField()
    beschriftungtext = models.TextField(blank=True, null=True)
    farbe = models.ForeignKey('Beltcolors', models.DO_NOTHING, blank=True, null=True)
    form = models.ForeignKey('Beltshapes', models.DO_NOTHING, blank=True, null=True)
    dicke = models.ForeignKey('Beltthickness', models.DO_NOTHING, blank=True, null=True)
    breite = models.ForeignKey('Beltwidths', models.DO_NOTHING, blank=True, null=True)
    kante = models.ForeignKey('Beltedges', models.DO_NOTHING, blank=True, null=True)
    protectivebelt = models.NullBooleanField()
    punchingplus = models.TextField(blank=True, null=True)
    punchingplusspace = models.TextField(blank=True, null=True)
    punchingminus = models.TextField(blank=True, null=True)
    punchingminusspace = models.TextField(blank=True, null=True)
    gurtverbinder = models.ForeignKey('Beltfastener', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'belt'


class Beltcolors(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    extrakosten = models.NullBooleanField()
    veraltet = models.NullBooleanField()
    kommentar = models.TextField(blank=True, null=True)
    ordering_id = models.IntegerField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'beltcolors'


class Beltcolortoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    beltcolor_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beltcolortoproducttype'


class Beltedges(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'beltedges'


class Beltfastener(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField(blank=True, null=True)
    deprecated = models.NullBooleanField()
    dropoffavailable = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'beltfastener'


class Beltfastenertoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    beltfastener_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beltfastenertoproducttype'


class Beltshapes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltshapes'

    def __str__(self):
        return self.name


class Beltshapetoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    beltshape_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beltshapetoproducttype'


class Beltthickness(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltthickness'

    def __str__(self):
        return self.name


class Beltthicknesstoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    beltthickness_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beltthicknesstoproducttype'


class Beltwidths(models.Model):
    id = models.IntegerField(primary_key=True)
    width = models.FloatField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltwidths'

    def __str__(self):
        return str(self.width)


class Beltwidthtobeltthickness(models.Model):
    beltthickness = models.ForeignKey(Beltthickness, models.DO_NOTHING)
    beltwidth = models.ForeignKey(Beltwidths, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'beltwidthtobeltthickness'


class Beltwidthtoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    beltwidth_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'beltwidthtoproducttype'


class Carriers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'carriers'


class Component(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    stockavailalbe = models.IntegerField(blank=True, null=True)
    localstockavailalbe = models.IntegerField(blank=True, null=True)
    datasheet = models.TextField(blank=True, null=True)
    manufacturecode = models.TextField(blank=True, null=True)
    category = models.ForeignKey('ComponentCategory', models.DO_NOTHING, blank=True, null=True)
    componentdesign = models.ForeignKey('ComponentFootprint', models.DO_NOTHING, blank=True, null=True)
    manufacture = models.ForeignKey('Manufacure', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component'


class ComponentCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_category'


class ComponentFootprint(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_footprint'


class ComponentGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    layoutfile = models.TextField(blank=True, null=True)
    # componentgroup = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_group'


class ComponentOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    orderdate = models.DateTimeField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    componentvendor = models.ForeignKey('ComponentVendor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_order'


class ComponentOrderArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    estimatedtimeofdelivery = models.DateTimeField(blank=True, null=True)
    component = models.ForeignKey(Component, models.DO_NOTHING, blank=True, null=True)
    componentorder = models.ForeignKey(ComponentOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_order_article'


class ComponentVendor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'component_vendor'


class ComponentgroupPart(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    layoutname = models.TextField(blank=True, null=True)
    component = models.ForeignKey(Component, models.DO_NOTHING, blank=True, null=True)
    componentgroup = models.ForeignKey(ComponentGroup, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'componentgroup_part'


class Componentgrouporders(models.Model):
    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    dateoforder = models.DateTimeField(blank=True, null=True)
    deliverydate = models.DateTimeField(blank=True, null=True)
    isdelivered = models.NullBooleanField()
    componentgroup = models.ForeignKey(ComponentGroup, models.DO_NOTHING, blank=True, null=True)
    pcbproducer = models.ForeignKey('PcbProducer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'componentgrouporders'


class Comprovider(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'comprovider'


class Comtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    shortname = models.TextField(blank=True, null=True)
    deprecated = models.NullBooleanField()
    possiblecommunicationproperty = models.ForeignKey('Possiblecommunicationproperty', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comtype'


class Comtypetoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    comtype_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comtypetoproducttype'


class ContactTypes(models.Model):
    id_contact_type = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contact_types'


class Contacts(models.Model):
    id_contact = models.IntegerField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    faktura_address = models.TextField(blank=True, null=True)
    faktura_details = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts'


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    countrycode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Customers(models.Model):
    id_customer_serial = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    organisation = models.TextField(blank=True, null=True)
    cust_ref_number = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    id_customer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customers'


class CustomersContacts(models.Model):
    id_customer = models.ForeignKey(Customers, models.DO_NOTHING, db_column='id_customer')
    id_contact = models.ForeignKey(Contacts, models.DO_NOTHING, db_column='id_contact')
    id_contact_type = models.ForeignKey(ContactTypes, models.DO_NOTHING, db_column='id_contact_type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers_contacts'


class Dropofftoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    dropoff_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dropofftoproducttype'


class Gurtfarbetoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    gurtfarbe_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gurtfarbetoproducttype'


class Gurtkantetoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    gurtkante_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gurtkantetoproducttype'


class Housingtoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    housing_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'housingtoproducttype'


class Itemtype(models.Model):
    dbid = models.IntegerField(primary_key=True)
    deprecated = models.NullBooleanField()
    category = models.TextField(blank=True, null=True)
    classname = models.TextField(blank=True, null=True)
    generation = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    produkttypname = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)
    possiblecommunicationproperty = models.ForeignKey('Possiblecommunicationproperty', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'itemtype'


class LongrangeAccount(models.Model):
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'longrange_account'


class LongrangeContract(models.Model):
    id = models.BigIntegerField(primary_key=True)
    contract_date = models.DateTimeField(blank=True, null=True)
    contract_no = models.TextField(blank=True, null=True)
    modification_date = models.DateTimeField(blank=True, null=True)
    contracttype = models.ForeignKey('LongrangeContracttype', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('Staff', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longrange_contract'


class LongrangeContracttype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    postpayment = models.NullBooleanField()
    prepayment = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'longrange_contracttype'


class LongrangeDeviceDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    activated = models.NullBooleanField()
    actionvation_timestamp = models.DateTimeField(blank=True, null=True)
    additionalemailaddresses = models.TextField(blank=True, null=True)
    deactivated = models.NullBooleanField()
    deactivation_timestamp = models.DateTimeField(blank=True, null=True)
    device_serialno = models.BigIntegerField(blank=True, null=True)
    iccid = models.TextField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    imsi = models.TextField(blank=True, null=True)
    pin = models.TextField(blank=True, null=True)
    pin2 = models.TextField(blank=True, null=True)
    puk = models.TextField(blank=True, null=True)
    puk2 = models.TextField(blank=True, null=True)
    serviceended = models.DateTimeField(blank=True, null=True)
    servicestarted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longrange_device_details'


class LongrangeaccountsDevices(models.Model):
    id_longrangeaccount = models.ForeignKey(LongrangeDeviceDetails, models.DO_NOTHING, db_column='id_longrangeaccount', blank=True, null=True)
    id_device = models.ForeignKey(LongrangeAccount, models.DO_NOTHING, db_column='id_device', primary_key=True)

    class Meta:
        managed = False
        db_table = 'longrangeaccounts_devices'


class Longrangecontractdetails(models.Model):
    id = models.IntegerField(primary_key=True)
    activated = models.NullBooleanField()
    actionvation_timestamp = models.DateTimeField(blank=True, null=True)
    deactivated = models.NullBooleanField()
    deactivation_timestamp = models.DateTimeField(blank=True, null=True)
    device_serialno = models.BigIntegerField(blank=True, null=True)
    iccid = models.TextField(blank=True, null=True)
    imei = models.TextField(blank=True, null=True)
    imsi = models.TextField(blank=True, null=True)
    pin = models.TextField(blank=True, null=True)
    pin2 = models.TextField(blank=True, null=True)
    puk = models.TextField(blank=True, null=True)
    puk2 = models.TextField(blank=True, null=True)
    serviceended = models.DateTimeField(blank=True, null=True)
    servicestarted = models.DateTimeField(blank=True, null=True)
    subscription = models.ForeignKey('Longrangesubscriptions', models.DO_NOTHING, db_column='subscription', blank=True, null=True)
    additionalemailaddresses = models.TextField(blank=True, null=True)
    fakturacontact = models.TextField(blank=True, null=True)
    fakturacustomer = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longrangecontractdetails'


class LongrangecontractsLongrangeaccounts(models.Model):
    id_contract = models.ForeignKey(LongrangeDeviceDetails, models.DO_NOTHING, db_column='id_contract', blank=True, null=True)
    id_account = models.ForeignKey(LongrangeContract, models.DO_NOTHING, db_column='id_account', primary_key=True)

    class Meta:
        managed = False
        db_table = 'longrangecontracts_longrangeaccounts'


class Longrangesubscriptions(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longrangesubscriptions'


class Manufacure(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manufacure'


class PcbProducer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcb_producer'


class PcbProducerStock(models.Model):
    id = models.IntegerField(primary_key=True)
    pcbproducercomponentname = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    pcbproducer = models.ForeignKey(PcbProducer, models.DO_NOTHING, blank=True, null=True)
    component = models.ForeignKey(Component, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcb_producer_stock'


class Pcbtype(models.Model):
    id = models.IntegerField(primary_key=True)
    deviceclass = models.TextField(blank=True, null=True)
    modelname = models.TextField(blank=True, null=True)
    majorversion = models.TextField(blank=True, null=True)
    minorversion = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'pcbtype'


class Possiblecommunicationproperty(models.Model):
    dbid = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
    required = models.NullBooleanField()
    deprecated = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'possiblecommunicationproperty'


class Possiblecommunicationpropertytocommunication(models.Model):
    communication = models.ForeignKey(Communication, models.DO_NOTHING)
    possiblecommunicationproperty = models.ForeignKey(Possiblecommunicationproperty, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'possiblecommunicationpropertytocommunication'


class Productelectronicconfigurationpropertytoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    productelectronicconfigurationproperty_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productelectronicconfigurationpropertytoproducttype'


class Productionbatch(models.Model):
    id = models.IntegerField(primary_key=True)
    allocatedsince = models.DateTimeField(blank=True, null=True)
    isallocated = models.NullBooleanField()
    name = models.TextField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    allocatedbyuser = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    auftrag_id = models.IntegerField(blank=True, null=True)
    produktposten = models.ForeignKey(Orderitem, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productionbatch'


class Productionrecordtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'productionrecordtype'


class Punching(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'punching'


class Refurbisment(models.Model):
    rma = models.TextField()
    salesperson = models.CharField(db_column='salesPerson', max_length=100)  # Field name made lowercase.
    customer_forename = models.TextField()
    customer_name = models.TextField()
    customer_email = models.CharField(max_length=254)
    country = models.TextField()
    content = models.TextField(blank=True, null=True)
    parcel_received = models.DateField()
    comments = models.TextField(blank=True, null=True)
    status = models.ForeignKey('Status', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'refurbisment'


class Shippments(models.Model):
    dbid = models.IntegerField(primary_key=True)
    dateofshippment = models.DateTimeField(blank=True, null=True)
    itemscount = models.IntegerField(blank=True, null=True)
    carrier = models.ForeignKey(Carriers, models.DO_NOTHING, blank=True, null=True)
    id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shippments'


class Shortrangecomtypetoproducttype(models.Model):
    producttype = models.ForeignKey(Producttype, models.DO_NOTHING)
    shortrangecomtype_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shortrangecomtypetoproducttype'


class Staff(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    initialies = models.TextField(blank=True, null=True)
    #email = models.EmailField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'status'


class Supportticket(models.Model):
    id = models.IntegerField(primary_key=True)
    creationtimestamp = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING, blank=True, null=True)
    customercontact = models.ForeignKey(Contacts, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('Supportticketstate', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('Supportticketcategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supportticket'


class Supportticketcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supportticketcategory'


class Supportticketstate(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supportticketstate'


# class UserNotes(models.Model):
#     dbid = models.IntegerField(primary_key=True)
#     sendtimestamp = models.DateTimeField(blank=True, null=True)
#     subject = models.CharField(max_length=255, blank=True, null=True)
#     message = models.CharField(max_length=255, blank=True, null=True)
#     readbyrecipient = models.NullBooleanField()
#     readtimestamp = models.DateTimeField(blank=True, null=True)
#     author = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
#     recipient = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user_notes'
