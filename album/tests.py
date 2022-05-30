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

#Test Image Class and its Methods
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Eldoret')
        self.location.save_location()

        self.category = Category(name='farms')
        self.category.save_category()

        self.image = Image(id=1, name='image', description='This is picture album test',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))    

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)    

    def test_update_image(self):
        self.image.save_image()
        self.image.update_image(self.image.id, 'images/photo1.jpg')
        updated_image = Image.objects.filter(image='images/photo2.jpg')
        self.assertFalse(len(updated_image) > 0)

    def test_get_image_by_id(self):
        found_image = self.image.get_image_by_id(self.image.id)
        images = Image.objects.filter(id=self.image.id)
        self.assertFalse(found_image, images)    
    
    def test_search_by_category(self):
        category = 'technology'
        found_img = self.image.search_by_category(category)
        self.assertFalse(len(found_img) > 1)  
    
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()                