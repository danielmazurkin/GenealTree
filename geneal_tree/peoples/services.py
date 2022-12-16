from peoples.models import People
from core.service import BaseService


class TreeService(BaseService):
    """Сервисный слой для работы с деревом."""
    @staticmethod
    def form_data():
        """Формируем данные для построения дерева чтобы отдать на фронт."""
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

            if people.pk_marriage:
                dict_info_people["pids"] = [people.pk_marriage]
            if people.pk_mother:
                dict_info_people["mid"] = people.pk_mother
            if people.pk_father:
                dict_info_people['fid'] = people.father.pk
            if people.avatar_url:
                dict_info_people['img'] = people.avatar_url

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
