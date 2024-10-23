from django.core.exceptions import ValidationError
import os
def allow_only_images_validator(value):   #majorly it can use to remove a raise of an error accoding to a given expression 
  ext=os.path.splitext(value.name)[1]# cove-image.jpg
  print(ext)
  valid_extensions=[".png",".jpg",".jpeg"]
  if not ext.lower() in valid_extensions:
    raise ValidationError('unsupportted file extensions'+str(valid_extensions))