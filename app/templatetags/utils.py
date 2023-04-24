from django import template
from django.http import HttpResponse


register = template.Library()


@register.simple_tag(name='draw_menu')
def draw_menu(menu, current_url):
    html = ""
    for item in menu:
        is_active = False
        if item.children.exists():
            for child in item.children.all():
                if child.title in current_url:
                    is_active = True
                    break
        html += f"<li class='{'active' if is_active else ''}'><a href='#'>{item.title}</a>"
        if item.children.exists():
            html += "<ul>"
            html += draw_menu(item.children.all(), current_url)
            html += "</ul>"
        html += "</li>"
    return html

