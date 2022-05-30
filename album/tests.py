from django.test import TestCase

# Create your tests here.
#Test Category Class and its Methods
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

#Test Location Class and its Methods
class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='Eldoret')
        self.location.save_location()

    def test_instance(self):
        self.location.save()
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        location_test = Location.get_locations()
        self.assertTrue(len(location_test) > 0)

    def test_get_locations(self):
        self.location.save_location()
        location_test = Location.get_locations()
        self.assertFalse(len(location_test) > 1)

    def test_delete_location(self):
        self.location.delete_location()
        location_test = Location.objects.all()
        self.assertTrue(len(location_test) == 0)          