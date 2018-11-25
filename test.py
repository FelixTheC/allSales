# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Dropoff(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.TextField(blank=True, null=True)
    dropoffcode = models.TextField(blank=True, null=True)
    external = models.NullBooleanField()
    internal = models.NullBooleanField()
    radiocontrolled = models.NullBooleanField()
    timercontrollvalue = models.CharField(max_length=255, blank=True, null=True)
    timercontrolled = models.NullBooleanField()
    timercontrolledabsolute = models.NullBooleanField()
    timercontrolledrelative = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'DropOff'


class Producttype(models.Model):
    id = models.IntegerField(primary_key=True)
    generation = models.CharField(max_length=255, blank=True, null=True)
    hatantenne = models.NullBooleanField()
    hatbatterie = models.NullBooleanField()
    hatbeacon = models.NullBooleanField()
    hatgurt = models.NullBooleanField()
    hatcottonspacer = models.NullBooleanField()
    hatdropoff = models.NullBooleanField()
    hatexternesensoren = models.NullBooleanField()
    hatgehaeuse = models.NullBooleanField()
    hatlongrangekommunikation = models.NullBooleanField()
    hatradiokommunikation = models.NullBooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    veraltet = models.NullBooleanField()
    typ = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)

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


class Surveyordermodel(models.Model):
    payment_option = models.CharField(max_length=255)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    number_of_collars = models.CharField(max_length=100, blank=True, null=True)
    customer_faktura_id = models.IntegerField(blank=True, null=True)
    contacts_faktura_id = models.IntegerField(blank=True, null=True)
    same_addr = models.BooleanField()
    battery_size = models.CharField(max_length=100, blank=True, null=True)
    animal_species = models.CharField(max_length=255, blank=True, null=True)
    belt_shape = models.CharField(max_length=255, blank=True, null=True)
    nom_collar_circumference = models.TextField(blank=True, null=True)
    vhf_beacon_frequency = models.TextField(blank=True, null=True)
    mortality_sensor = models.IntegerField(blank=True, null=True)
    external_dropoff = models.BooleanField()
    external_dropoff_real_time = models.CharField(max_length=200, blank=True, null=True)
    external_dropoff_abs_time = models.CharField(max_length=200, blank=True, null=True)
    utc_lmt = models.CharField(max_length=50, blank=True, null=True)
    utc_correction = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    vhf_beacon_schedule = models.CharField(max_length=255, blank=True, null=True)
    globalstar = models.BooleanField()
    iridium = models.BooleanField()
    contact_name_airtime_fee = models.CharField(max_length=255, blank=True, null=True)
    contact_mail_airtime_fee = models.CharField(max_length=254, blank=True, null=True)
    notification_mail = models.CharField(max_length=500, blank=True, null=True)
    notification_sms = models.CharField(max_length=255, blank=True, null=True)
    belt_width = models.CharField(max_length=255, blank=True, null=True)
    belt_thickness = models.CharField(max_length=255, blank=True, null=True)
    belt_edge = models.CharField(max_length=255, blank=True, null=True)
    belt_colour = models.CharField(max_length=255, blank=True, null=True)
    belt_labeling = models.BooleanField()
    belt_labeling_instructions = models.CharField(max_length=255, blank=True, null=True)
    belt_plates = models.BooleanField()
    belt_plates_instructions = models.CharField(max_length=76, blank=True, null=True)
    cotton_layers = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    customer_staff = models.CharField(max_length=255, blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    order_acceptet = models.BooleanField()
    customer_invoice_address = models.ForeignKey('OrdercontactOrdercontactinvoiceaddresse', models.DO_NOTHING, blank=True, null=True)
    delivery_addresse = models.ForeignKey('OrdercontactOrdercontactdeliveryaddresse', models.DO_NOTHING, blank=True, null=True)
    as_email = models.BooleanField()
    as_post = models.BooleanField()
    other_color = models.CharField(max_length=100, blank=True, null=True)
    external_dropoff_controll = models.CharField(max_length=200, blank=True, null=True)
    invoice_mail = models.CharField(max_length=254, blank=True, null=True)
    gps_schedule = models.CharField(max_length=255, blank=True, null=True)
    operation_number = models.CharField(db_column='operation_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    airtime_contract = models.CharField(max_length=100)
    id_tag = models.BooleanField()
    iridium_num_of_fixes_gps = models.IntegerField(blank=True, null=True)
    iridium_num_of_fixes_iridium = models.IntegerField(blank=True, null=True)
    reflective_stripes = models.BooleanField()
    reflective_stripes_instructions = models.CharField(max_length=76, blank=True, null=True)
    iridium_contract_type = models.CharField(max_length=255, blank=True, null=True)
    vat_ein_number = models.CharField(max_length=255, blank=True, null=True)
    delivery_time = models.DateField(blank=True, null=True)
    inc_or_gmbh = models.CharField(max_length=10, blank=True, null=True)
    owm_gps_schedule = models.CharField(max_length=100, blank=True, null=True)
    own_vhf_schedule = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SurveyOrderModel'


class Vertexliteordermodel(models.Model):
    payment_option = models.CharField(max_length=255)
    order_no = models.CharField(max_length=255, blank=True, null=True)
    as_post = models.BooleanField()
    as_email = models.BooleanField()
    invoice_mail = models.CharField(max_length=254, blank=True, null=True)
    number_of_collars = models.IntegerField(blank=True, null=True)
    customer_faktura_id = models.IntegerField()
    contacts_faktura_id = models.IntegerField(blank=True, null=True)
    same_addr = models.BooleanField()
    animal_species = models.CharField(max_length=255, blank=True, null=True)
    battery_size = models.CharField(max_length=100, blank=True, null=True)
    belt_shape = models.CharField(max_length=255, blank=True, null=True)
    nom_collar_circumference = models.TextField(blank=True, null=True)
    vhf_beacon_frequency = models.TextField(blank=True, null=True)
    mortality_sensor = models.IntegerField(blank=True, null=True)
    external_dropoff = models.BooleanField()
    external_dropoff_controll = models.CharField(max_length=200, blank=True, null=True)
    external_dropoff_real_time = models.CharField(max_length=200, blank=True, null=True)
    external_dropoff_abs_time = models.CharField(max_length=200, blank=True, null=True)
    utc_lmt = models.CharField(max_length=50, blank=True, null=True)
    utc_correction = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    vhf_beacon_schedule = models.CharField(max_length=255, blank=True, null=True)
    gps_schedule = models.CharField(max_length=255, blank=True, null=True)
    further_programming_settings = models.CharField(max_length=255, blank=True, null=True)
    globalstar = models.BooleanField()
    iridium = models.BooleanField()
    gsm = models.BooleanField()
    iridium_mode = models.CharField(max_length=100, blank=True, null=True)
    iridium_num_of_fixes = models.IntegerField(blank=True, null=True)
    gsm_vectronic_sim = models.IntegerField(blank=True, null=True)
    gsm_customer_sim_telephone_no = models.CharField(max_length=255, blank=True, null=True)
    gsm_customer_sim_pin = models.CharField(max_length=255, blank=True, null=True)
    gsm_customer_sim_puk = models.CharField(max_length=255, blank=True, null=True)
    contact_name_airtime_fee = models.CharField(max_length=255, blank=True, null=True)
    contact_mail_airtime_fee = models.CharField(max_length=254, blank=True, null=True)
    notification_mail = models.CharField(max_length=254, blank=True, null=True)
    notification_sms = models.CharField(max_length=255, blank=True, null=True)
    belt_width = models.CharField(max_length=255, blank=True, null=True)
    belt_thickness = models.CharField(max_length=255, blank=True, null=True)
    belt_edge = models.CharField(max_length=255, blank=True, null=True)
    belt_colour = models.CharField(max_length=255, blank=True, null=True)
    other_color = models.CharField(max_length=100, blank=True, null=True)
    belt_labeling = models.BooleanField()
    belt_labeling_instructions = models.CharField(max_length=255, blank=True, null=True)
    belt_plates = models.BooleanField()
    belt_plates_instructions = models.CharField(max_length=76, blank=True, null=True)
    cotton_layers = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    customer_staff = models.CharField(max_length=255, blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    order_acceptet = models.BooleanField()
    operation_number = models.CharField(db_column='operation_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer_invoice_address = models.ForeignKey('OrdercontactOrdercontactinvoiceaddresse', models.DO_NOTHING, blank=True, null=True)
    delivery_addresse = models.ForeignKey('OrdercontactOrdercontactdeliveryaddresse', models.DO_NOTHING, blank=True, null=True)
    airtime_contract = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'VertexLiteOrderModel'


class Animalspecies(models.Model):
    id = models.IntegerField(primary_key=True)
    hint = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animalspecies'


class Antennas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antennas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Batteries(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    hasdropoff = models.NullBooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)
    screwthread = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batteries'


class Beltcolors(models.Model):
    id = models.IntegerField(primary_key=True)
    kommentar = models.TextField(blank=True, null=True)
    extrakosten = models.NullBooleanField()
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltcolors'


class Beltedges(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltedges'


class Beltfastener(models.Model):
    id = models.IntegerField(primary_key=True)
    dropoffavailable = models.NullBooleanField()
    value = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltfastener'


class Beltshapes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    veraltet = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltshapes'


class Beltthickness(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltthickness'


class Beltwidths(models.Model):
    id = models.IntegerField(primary_key=True)
    obsolete = models.NullBooleanField()
    ordering_id = models.IntegerField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beltwidths'


class Comtype(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    deprecated = models.NullBooleanField()
    shortname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comtype'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Hash(models.Model):
    hash = models.TextField()

    class Meta:
        managed = False
        db_table = 'hash'


class Housings(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'housings'


class LongrangeContracttype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()
    postpayment = models.NullBooleanField()
    prepayment = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'longrange_contracttype'


class OrdercontactOrdercontactdeliveryaddresse(models.Model):
    delivery_organisation_name = models.CharField(max_length=355, blank=True, null=True)
    delivery_complete_addresse = models.CharField(max_length=355, blank=True, null=True)
    delivery_zip_code = models.CharField(max_length=15, blank=True, null=True)
    delivery_city = models.CharField(max_length=255, blank=True, null=True)
    delivery_country = models.CharField(max_length=255, blank=True, null=True)
    delivery_contact_person = models.CharField(max_length=255, blank=True, null=True)
    delivery_email_addresse = models.CharField(max_length=254, blank=True, null=True)
    delivery_telephone_nr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderContact_ordercontactdeliveryaddresse'


class OrdercontactOrdercontactinvoiceaddresse(models.Model):
    organisation_name = models.CharField(max_length=355, blank=True, null=True)
    complete_addresse = models.CharField(max_length=355, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=355, blank=True, null=True)
    email_addresse = models.CharField(max_length=254, blank=True, null=True)
    telephone_nr = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderContact_ordercontactinvoiceaddresse'


class Pcbtype(models.Model):
    id = models.IntegerField(primary_key=True)
    deviceclass = models.TextField(blank=True, null=True)
    majorversion = models.TextField(blank=True, null=True)
    minorversion = models.TextField(blank=True, null=True)
    modelname = models.TextField(blank=True, null=True)
    obsolete = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'pcbtype'


class Productionrecordtype(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productionrecordtype'


class SalesSalesinputsurvey(models.Model):
    co_worker = models.CharField(max_length=100, blank=True, null=True)
    animal_species = models.CharField(max_length=255, blank=True, null=True)
    punching1_dist = models.CharField(max_length=50)
    punching1_pos = models.IntegerField()
    punching1_neg = models.IntegerField()
    punching2 = models.CharField(max_length=50)
    further_instructions_belt = models.TextField(blank=True, null=True)
    gps_schedule_name = models.CharField(max_length=255, blank=True, null=True)
    vhf_schedule_name = models.CharField(max_length=255, blank=True, null=True)
    gl_no_of_attempts = models.IntegerField(blank=True, null=True)
    gl_fixes_per_message = models.IntegerField(blank=True, null=True)
    ir_fixes_per_message = models.IntegerField(blank=True, null=True)
    further_instructions_programming = models.TextField(blank=True, null=True)
    order = models.ForeignKey(Surveyordermodel, models.DO_NOTHING, blank=True, null=True)
    ir_contract_type = models.CharField(max_length=255, blank=True, null=True)
    path_customer_folder = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_salesinputsurvey'


class SalesSurveyprodrec(models.Model):
    order_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sales_surveyprodrec'


class SalesSurveyprodrecSalesinput(models.Model):
    surveyprodrec_id = models.IntegerField()
    salessalesinputsurvey = models.ForeignKey(SalesSalesinputsurvey, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sales_surveyprodrec_salesinput'
        unique_together = (('surveyprodrec_id', 'salessalesinputsurvey'),)


class Staff(models.Model):
    id = models.BigIntegerField(primary_key=True)
    initialies = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'
