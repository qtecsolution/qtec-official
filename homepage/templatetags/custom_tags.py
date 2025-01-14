# import re
from django import template
register = template.Library()


@register.filter(name='split')
def split(value, key):
    return value.split(key)


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()


@register.filter(name='proper_paginate')
def proper_paginate(paginator, current_page, neighbors=2):
    if paginator.num_pages > 2 * neighbors:
        start_index = max(1, current_page - neighbors)
        end_index = min(paginator.num_pages, current_page + neighbors)
        if end_index < start_index + 2 * neighbors:
            end_index = start_index + 2 * neighbors
        elif start_index > end_index - 2 * neighbors:
            start_index = end_index - 2 * neighbors
        if start_index < 1:
            end_index -= start_index
            start_index = 1
        elif end_index > paginator.num_pages:
            start_index -= (end_index - paginator.num_pages)
            end_index = paginator.num_pages
        page_list = [f for f in range(start_index, end_index + 1)]
        return page_list[:(2 * neighbors + 1)]
    return paginator.page_range


@register.simple_tag
def comma_seperator(amount):
    try:
        amount= int(amount)
    except Exception as e:
        try:
            amount= float(amount)
        except Exception as e:
            amount= amount

    if isinstance(amount, int) or isinstance(amount, float):
        comma_sep= format(amount, ",")
    else:
       comma_sep=amount
    return comma_sep

# youtube video id extractor filter
# @register.filter
# def extract_id(value):
#     """
#     Extracts the YouTube video ID from various URL formats.
#     """
#     # Pattern to match YouTube video ID
#     patterns = [
#         r'youtu\.be/(?P<id>[a-zA-Z0-9_-]+)',  # Short URL format
#         r'youtube\.com/watch\?v=(?P<id>[a-zA-Z0-9_-]+)',  # Full URL format
#         r'youtube\.com/embed/(?P<id>[a-zA-Z0-9_-]+)',  # Embed URL format
#     ]
#     for pattern in patterns:
#         match = re.search(pattern, value)
#         if match:
#             return match.group('id')
#     return value  # Return original value if no match