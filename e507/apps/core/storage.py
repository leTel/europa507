from django.core.files.storage import FileSystemStorage
from django.conf import settings

import redactor.handlers
import datetime

redactor_storage = FileSystemStorage(location=settings.MEDI_ROOT, base_url=settings.MEDIA_URL)


class UploadDateDirectoryUploader(redactor.handlers.SimpleUploader):
    """
    Handler  that saves files in a directory based on the current date
    /2014/3/28/filename.etc
    """
    def get_upload_path(self):
        today = datetime.datetime.today()
        path = '{0}/{1}/{2}'.format(today.year, today.month, today.day)
        import ipdb; ipdb.set_trace()

        return path

