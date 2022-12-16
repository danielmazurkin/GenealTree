from core.service import BaseService
from photos.models import PhotoPeople


class PhotoService(BaseService):

    @staticmethod
    def form_data():
        photos = PhotoPeople.objects.all()

        urls_images = []
        for photo in photos:
            urls_images.append(photo)

        return urls_images
