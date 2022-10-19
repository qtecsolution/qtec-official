from django import template

register = template.Library()



@register.filter
def check_active_menu(request, url_name_list_str):
    url_name_list = url_name_list_str.split(",")
    url_name_list = [str(item).strip().lower() for item in url_name_list]
    current_url_name = str(request.resolver_match.url_name).strip().lower()
    if current_url_name in url_name_list:
        return True
    return False