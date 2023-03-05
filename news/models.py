from django.db import models
from wagtail import blocks
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel


class NewsPage(Page):
    intro = models.CharField(max_length=250)
    content = StreamField([
        ('heading', blocks.CharBlock(form_classname='full title', icon='title')),
        ('paragraph', blocks.RichTextBlock(icon='pilcrow')),
        ('image', ImageChooserBlock(icon='image'))
    ], use_json_field=True)
    image = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('content'),
        FieldPanel('image')
    ]

    api_fields = [
        APIField('intro'),
        APIField('content'),
        APIField('image_thumbnail', serializer=ImageRenditionField('fill-300x300', source='image')),
    ]
