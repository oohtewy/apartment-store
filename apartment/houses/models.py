from django.db import models
from PIL import Image

class HousesModel(models.Model):
    IMAGES_FOLDER ='houses'
    
    
    title = models.CharField('Title',max_length=250,default='House')
    images = models.ImageField("Images", upload_to=IMAGES_FOLDER)
    image_width = models.PositiveIntegerField(null=True, blank=True)
    image_height = models.PositiveIntegerField(null=True, blank=True)
    description = models.TextField('Description',max_length=1000)
    address = models.CharField('Address', max_length=100)
    num_of_rooms = models.DecimalField('Number of rooms',max_digits=4, decimal_places=2 )
    price= models.DecimalField('Price', max_digits=100, decimal_places=2)
    space=models.DecimalField('Space',max_digits=10, decimal_places=2)
    repair = models.BooleanField('Repaire',default=False)
    
    def __str__(self) -> str:
        return self.title
    
    
    class Meta: 
        verbose_name = 'House'
        verbose_name_plural = 'Houses'