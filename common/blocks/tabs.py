# -*- coding: utf-8 -*-
"""
"""


from django.template.loader import render_to_string

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import ListBlock
from wagtail.wagtailcore.blocks import CharBlock
from wagtail.wagtailcore.blocks import StructBlock
from common.blocks.people import PeopleBlock
from common.blocks.columns import ColumnsBlock
from common.blocks.columns import GenericContentStreamBlock


class TabBlock(StructBlock):
    name = CharBlock()
    content = GenericContentStreamBlock()

    class Meta:
        form_template = 'common/block_forms/tab.html'
        template = 'common/blocks/tab.html'


class TabbedBlock(blocks.ListBlock):

    class Meta:
        template = 'common/blocks/tabbed_block.html'
        label = 'Tabbed Block'
    
    def __init__(self, **kwargs):
        return super(TabbedBlock, self).__init__(TabBlock(), **kwargs)

    def render_form(self, value, prefix='', errors=None):
        if errors:
            if len(errors) > 1:
                # We rely on ListBlock.clean throwing a single ValidationError with a specially crafted
                # 'params' attribute that we can pull apart and distribute to the child blocks
                raise TypeError('ListBlock.render_form unexpectedly received multiple errors')
            error_list = errors.as_data()[0].params
        else:
            error_list = None

        list_members_html = [
            self.render_list_member(child_val, "%s-%d" % (prefix, i), i,
                                    errors=error_list[i] if error_list else None)
            for (i, child_val) in enumerate(value)
        ]

        return render_to_string('common/block_forms/tabs.html', {
            'help_text': getattr(self.meta, 'help_text', None),
            'prefix': prefix,
            'list_members_html': list_members_html,
        })


class TabBlockInColumn(blocks.StructBlock):
    id = blocks.CharBlock(required=True)
    isActive = blocks.BooleanBlock(default=False, required=False)
    container = blocks.StreamBlock([
        ('paragraph', blocks.RichTextBlock()),
        ('people_block', PeopleBlock()),
        ('raw_html', blocks.RawHTMLBlock(
            help_text='With great power comes great responsibility. This HTML is unescaped. Be careful!')),

    ])

    class Meta:
        template = 'common/blocks/tab_block.html'
        icon = 'folder-inverse'
        label = 'Tab'


class TabContainerInColumnBlock(blocks.StructBlock):
    tabs = blocks.StreamBlock([('tab', TabBlockInColumn())])
    class Meta:
        template = 'common/blocks/tabs_container_block.html'
        icon = 'placeholder'
        label = 'Tab Container'


class TabIndexEntryBlock(blocks.StructBlock):
    id = blocks.TextBlock(max_length=25, required=True)
    display = blocks.TextBlock(max_length=40, required=True)

    class Meta:
        icon = 'arrow-right'
        label = 'Tab Entry'


class TabIndexBlock(blocks.StructBlock):
    display_style = blocks.ChoiceBlock(required=True, choices=[
        ('vertical', 'vertical'),
        ('horizontal', 'horizontal')])
    tabsIndexes = blocks.StreamBlock([('tab', TabIndexEntryBlock()),
    ])

    class Meta:
        template = 'common/blocks/tab_index_block.html'
        icon = 'list-ul'
        label = "Tab Indexing"


class TabContainerBlock(blocks.StructBlock):
    tabs = blocks.StreamBlock([('tab', TabBlock())])
    class Meta:
        template = 'common/blocks/tabs_container_block.html'
        icon = 'placeholder'
        label = 'Tab Container'
