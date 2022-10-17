def get_list(username):
    url_list = ['dashboard_url','video_url','add_video_url','update_video_url','upload_video_url','comment_url','channel_url','channel_create_url','vimeo_redirect_url']
    if username  == 'PROVIDER':
        return url_list
    else:
        return []