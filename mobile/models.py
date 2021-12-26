from django.db import models

class Brand_Name(models.Model):
    brand_name = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Brand Name"
        verbose_name_plural = "Brand Names"

    def __str__(self):
        return self.brand_name


class Model_Name(models.Model):
    model_name = models.CharField(max_length=300,unique = True)

    class Meta:
        verbose_name = "Model Name"
        verbose_name_plural = "Model Names"

    def __str__(self):
        return self.model_name     

class Color(models.Model):
    color = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.color   

class Mobile(models.Model):
    brand_name = models.ForeignKey(Brand_Name, related_name='brand', on_delete=models.CASCADE) 
    model_name = models.ForeignKey(Model_Name, related_name='model', on_delete=models.CASCADE) 
    color = models.OneToOneField(Color,related_name='mobile_color',on_delete=models.CASCADE)
    jan_code =  models.CharField(max_length = 300,unique = True)
    image = models.URLField(max_length=200,blank=True, null=True)


    class Meta:
        verbose_name = "Mobile Phone"
        verbose_name_plural = "Mobile Phones"

    def __str__(self):
        return self.jan_code
