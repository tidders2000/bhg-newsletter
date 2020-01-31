from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    content1= RichTextField(blank=True)
    content2 = RichTextField(blank=True)
    content3= RichTextField(blank=True)
    content4 = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
         FieldPanel('content1', classname="full"),
          FieldPanel('content2', classname="full"),
          FieldPanel('content3', classname="full"),
          FieldPanel('content4', classname="full"),
    ]
    