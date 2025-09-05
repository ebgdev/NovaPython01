from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

# object_id (zorunlu)
# content_type (zorunlu)
# content_object (opsiyonel --> product)
class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveBigIntegerField()
    # label hangi urune uygulandi.
    content_object = GenericForeignKey()
