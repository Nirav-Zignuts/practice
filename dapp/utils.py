from django.utils.text import slugify
import uuid
def genrate_slug(name):
    from .models import Student
    name = slugify(name)
    while Student.objects.filter(slug=name).exists():
        name = f"{slugify(name)}-{str(uuid.uuid4())[0:4]}"

    return name