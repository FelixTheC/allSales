import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse

DEFAULTBELTSHAPES = ['round-shaped', 'drop-shaped']
BELTTHICKNESSES = ['3.4 mm (SF/SF)', '4.2 mm (ST/SF)', '5 mm (ST/ST)']
DEFAULTEDGES = ['round', 'smooth']
DEFAULTCOLORS = ['black', 'white', 'tan', 'brown', 'yellow', 'other']
DEFAULTWIDTH = ['25 mm', '32 mm', '38 mm', '50 mm', '63 mm', '75 mm']

BELTSHAPES = ((shape, shape) for shape in DEFAULTBELTSHAPES)

BELTWIDTH = ((width, width) for width in DEFAULTWIDTH)

BELTTHICKNESS = ((thickness, thickness) for thickness in BELTTHICKNESSES)

BELTEDGES = ((edge, edge) for edge in DEFAULTEDGES)

BELTCOLORS = ((color, color) for color in DEFAULTCOLORS)

PAYMENTOPTIONS = (
    ('Purchase with Order No.', 'Purchase with Order No.'),
    ('Bank Wire Transfer', 'Bank Wire Transfer'),
    ('Check', 'Check'),
    ('Credit Card', 'Credit Card (3.0% service fee)'),
)

UTCORLMT = (
    ('utc', 'UTC'),
    ('lmt', 'LMT')
)


def upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), filename])


def gps_schedule_upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), 'gps_schedule', filename])


def vhf_schedule_upload_path(instance, filename):
    return '/'.join([settings.MEDIA_ROOT, str(instance.contacts_faktura_id), 'vhf_schedule', filename])


class LinkHash(models.Model):
    class Meta:
        db_table = 'hash'
        app_label = 'sales'
        managed = False

    hash = models.TextField(max_length=255)

    def get_main_root(self):
        return reverse('sales:overview')

    def get_labelname(self):
        return 'To Orderings'


class ProductionRecordInputMiniGL(models.Model):
    co_worker = models.CharField(max_length=100, blank=True, null=True)
    animal_species = models.CharField(max_length=255, blank=True, null=True)
    gps_schedule_name = models.CharField(max_length=255, blank=True, null=True)
    vhf_schedule_name = models.CharField(max_length=255, blank=True, null=True)
    gl_no_of_attempts = models.IntegerField(blank=True, null=True)
    gl_fixes_per_message = models.IntegerField(blank=True, null=True)
    further_instructions_programming = models.TextField(max_length=500, blank=True, null=True)
    path_customer_folder = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        abstract = True


class ProductionRecordInput(ProductionRecordInputMiniGL):
    punching1_dist = models.CharField(max_length=50, default='')
    punching1_pos = models.IntegerField()
    punching1_neg = models.IntegerField()
    punching2 = models.CharField(max_length=50)
    further_instructions_belt = models.TextField(max_length=500, blank=True, null=True)
    ir_contract_type = models.CharField(max_length=255, blank=True, null=True)
    ir_fixes_per_message = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class MiniBaseModel(models.Model):

    class Meta:
        abstract = True

    payment_option = models.CharField(choices=PAYMENTOPTIONS, max_length=255, blank=True, default='check')
    order_no = models.CharField(null=True, blank=True, max_length=255)
    as_post = models.BooleanField(default=False, blank=True)
    as_email = models.BooleanField(default=True, blank=True)
    invoice_mail = models.EmailField(null=True, blank=True)
    number_of_collars = models.CharField(null=True, blank=True, max_length=100)
    customer_faktura_id = models.IntegerField(editable=False, null=True)
    contacts_faktura_id = models.IntegerField(null=True, blank=True)
    same_addr = models.BooleanField(blank=True, default=True)
    globalstar = models.BooleanField(blank=True, default=False)
    iridium = models.BooleanField(blank=True, default=False)
    vhf_beacon_schedule = models.CharField(blank=True, default='24', max_length=255, null=True)
    vhf_beacon_frequency = models.TextField(blank=True, null=True, default=148)
    contact_name_airtime_fee = models.CharField(blank=True, null=True, max_length=255)
    contact_mail_airtime_fee = models.EmailField(blank=True, null=True)
    notification_mail = models.CharField(blank=True, null=True, max_length=500)
    notification_sms = models.CharField(blank=True, null=True, max_length=255)

    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    customer_staff = models.CharField(blank=True, null=True, max_length=255)
    origin = models.TextField(editable=False, null=True, blank=True, max_length=1000)
    order_acceptet = models.BooleanField(default=False)
    operation_number = models.CharField(db_column='operation_Number', max_length=255, blank=True, null=True)
    id_tag = models.BooleanField(blank=True, default=False)
    airtime_contract = models.FileField(blank=True, upload_to=upload_path, null=True)
    vat_ein_number = models.CharField(max_length=255, blank=True, null=True, default='')
    delivery_time = models.DateField(blank=True, null=True)
    inc_or_gmbh = models.CharField(blank=True, null=True, default='gmbh', max_length=13)
    owm_gps_schedule = models.FileField(null=True, blank=True, upload_to=gps_schedule_upload_path)
    own_vhf_schedule = models.FileField(null=True, blank=True, upload_to=vhf_schedule_upload_path)


class BaseModelWithoutBeltDesign(MiniBaseModel):

    class Meta:
        abstract = True

    animal_species = models.CharField(max_length=255, blank=True, null=True)
    battery_size = models.CharField(max_length=100, null=True, blank=True)
    nom_collar_circumference = models.TextField(blank=True, null=True, max_length=255)
    mortality_sensor = models.PositiveIntegerField(blank=True, null=True, default=24)
    utc_lmt = models.CharField(blank=True, default=False, max_length=50, choices=UTCORLMT, null=True)
    utc_correction = models.DecimalField(blank=True, null=True, max_digits=4, decimal_places=2)
    cotton_layers = models.IntegerField(blank=True, null=True)

    gps_schedule = models.CharField(blank=True, default='Every 13h', max_length=255, null=True)
    iridium_num_of_fixes_gps = models.IntegerField(blank=True, null=True)
    iridium_contract_type = models.CharField(max_length=255, null=True, blank=True, default='')


class BaseModel(BaseModelWithoutBeltDesign):

    belt_width = models.CharField(choices=BELTWIDTH, blank=True, null=True, max_length=255)
    belt_thickness = models.CharField(choices=BELTTHICKNESS, blank=True, null=True, max_length=255)
    belt_edge = models.CharField(choices=BELTEDGES, blank=True, null=True, max_length=255, default='round')
    belt_colour = models.CharField(choices=BELTCOLORS, blank=True, null=True, max_length=255)
    other_color = models.CharField(max_length=100, blank=True, null=True)
    belt_labeling = models.BooleanField(blank=True, default=False)
    belt_labeling_instructions = models.CharField(max_length=255, null=True, blank=True)
    belt_plates = models.BooleanField(blank=True, default=False)
    belt_plates_instructions = models.CharField(max_length=76, null=True, blank=True)
    belt_shape = models.CharField(choices=BELTSHAPES, max_length=255, blank=True, null=True)

    reflective_stripes = models.BooleanField(blank=True, default=False)
    reflective_stripes_instructions = models.CharField(max_length=76, null=True, blank=True)

    class Meta:
        abstract = True