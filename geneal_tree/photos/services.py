from core.service import BaseService
from photos.models import PhotoPeople
from typing import List


class PhotoService(BaseService):
    """Сервис для работы с Фото."""

    @staticmethod
    def form_data(pk_user: int) -> list[str]:
        photos = PhotoPeople.objects.filter(owner_user__pk=pk_user)

        urls_images: List[PhotoPeople] = []
        for photo in photos:
            urls_images.append(photo)

        return urls_images
