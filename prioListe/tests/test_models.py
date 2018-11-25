import datetime
from django.test import TestCase
from ..models import PriolisteAssignment


class PrioListeAssignmentTestCase(TestCase):
    def setUp(self):
        #minimum setUp
        assignment = PriolisteAssignment.objects.create(staff='CA',
                                                        time_in_weeks=12,
                                                        customer='TEST',
                                                        created_at=datetime.date.today(),
                                                        ordering_number='CA0000'
                                                        )

    def test_assignment(self):
        entry = PriolisteAssignment.objects.get(staff='CA')
        self.assertTrue(entry)