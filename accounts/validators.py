from django.core.exceptions import ValidationError

import os

def allow_extension_validatotr(value):
    ext = os.path.splitext(value.name)[-1]
    print(ext)
    valid = [".png",".jpg",".jpeg"]

    if ext.lower() not in valid:
        print(ext)
        raise ValidationError("Unsupported file extension"+str(valid))