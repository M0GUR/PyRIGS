from bs4 import BeautifulSoup
from django import template
from django.utils.safestring import mark_safe
import markdown

__author__ = 'ghost'

register = template.Library()

@register.filter(name="markdown")
def markdown_filter(text, format='html'):
    html = markdown.markdown(text)
    if format == 'html':
        return mark_safe('<div class="markdown">' + html + '</div>')
    elif format == 'rml':
        # Convert format to RML
        soup = BeautifulSoup(html, "html.parser")

        # Image aren't supported so remove them
        for img in soup('img'):
            img.parent.extract()

        # <code> should become <font>
        for c in soup('code'):
            c.name = 'font'
            c['face'] = "Courier"

        # blockquotes don't exist but we can still do something to show
        for bq in soup('blockquote'):
            bq.name = 'pre'
            bq.string = bq.text

        for list in soup.findAll(['ul','ol']):
            list['style'] = list.name
            for li in list.findAll('li', recursive=False):
                text = li.find(text=True)
                text.wrap(soup.new_tag('p'))

            if list.parent.name != 'li':
                indent = soup.new_tag('indent')
                indent['left'] = '0.6cm'

                list.wrap(indent)

        # Paragraphs have a different tag
        for p in soup('p'):
            p.name = 'para'

        # @todo: <ul> and <li> tags to not appear to be working

        return mark_safe(soup)
