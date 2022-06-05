from django.test import TestCase
from .models import Image,Comment,Likes,Profile


# Create your tests here.
class ImageTest(TestCase):
    '''
    test class for Images model
    '''
    def setUp(self):
       
        self.new_image = Image(name='food')
        self.new_image.save_image()
        self.new_comment = Comment(comment='great')
        self.new_comment.save_comment()
        self.new_picture = Image(name='chapati', comment='local food', image='images/food.jpg' )
        self.new_picture.save_image()
        self.picture2 =Image(name='ugali', comment='this is ugali', image='images/ugali.jpg' )
        self.picture2.save_image()
    def tearDown(self):
     
        Image.objects.all().delete()
        Comment.objects.all().delete()
        Image.objects.all().delete()
    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Image.objects.all()) == 2)
    def test_instances(self):
        '''
         method to test instances created successfully during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Image))
        self.assertTrue(isinstance(self.new_comment, Comment))
        

    def test_delete_image(self):
        '''
        test method to ensure an Image is deleted correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Image.objects.all()) == 1)


    def test_search_people(self):
    
        image = Image.search_by_name(self.new_picture.name)
        print(image)




class CommentTest(TestCase):
    '''
    test class for Comment model
    '''
    def setUp(self):
  
        self.new_comment = Comment(comment='very good')
        self.new_comment.save_comment()

    def tearDown(self):
        '''
        test method to delete Category instance
        '''
        Comment.objects.all().delete()

    def test_save_profile(self):
        '''
        test for profile instance has been correctly saved
        '''
        self.assertTrue(len(Profile.objects.all()) == 1)

    def test_delete_profile(self):
        '''
        test a Category instance has been correctly deleted
        '''
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)


