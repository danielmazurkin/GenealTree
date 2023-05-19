from core.service import BaseService
from photos.models import PhotoPeople
from typing import List


class PhotoService(BaseService):
    """Сервис для работы с Фото."""

    @staticmethod
    def form_data() -> list[str]:
        photos = PhotoPeople.objects.all()

        urls_images: List[PhotoPeople] = []
        for photo in photos:
            urls_images.append(photo)

        return urls_images
