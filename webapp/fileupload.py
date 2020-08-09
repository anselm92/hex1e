from django.core.files.storage import FileSystemStorage

from hex1e import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


def blog_file_upload_handler(blog, file_name):
    return f"blogs/{blog.title}/{file_name}"


def raffle_file_upload_handler(blog, file_name):
    return f"raffles/{blog.title}/{file_name}"