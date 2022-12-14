from peoples.models import People
from django.conf import settings


class TreeService:
    """Сервисный слой для работы с деревом."""

    @staticmethod
    def build_tree():
        # nodes: источник данных.Свойство id является обязательным.
        # pids: идентификаторы партнеров, представляющие связь между двумя партнерами(жена и муж).
        # mid: идентификатор матери.
        # fid: идентификатор отца.
        # пол: мужской или женский.

        # nodes: [
        #    {id: 1, pids: [2], name: "Amber McKenzie"},
        #    {id: 2, pids: [1], name: "Ava Field"},
        #    {id: 3, mid: 1, fid: 2, name: "Peter Stevens"}
        # ]

        nodes = []
        people_set = People.objects.select_related('mother', 'marriage', 'father').all()

        for people in people_set:
            dict_info_people = {"id": people.pk}

            if getattr(people, 'marriage'):
                dict_info_people["pids"] = [people.marriage.pk]

            if getattr(people, 'mother'):
                dict_info_people['mid'] = people.mother.pk

            if getattr(people, 'father'):
                dict_info_people['fid'] = people.father.pk

            if hasattr(people, 'avatarpeople'):
                url_form = f'{settings.SITE_URL}{people.avatarpeople.photo_link.url}' if hasattr(people.avatarpeople,
                                                                                                 'photo_link') else None
                dict_info_people['img'] = url_form

            dict_info_people["name"] = str(people)
            nodes.append(dict_info_people)

        result_dict_tree = {
            "nodeBinding": {
                "field_0": "name",
                "img_0": "img",
            },
            "nodes": nodes
        }

        return result_dict_tree
