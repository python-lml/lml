from json import dumps, JSONEncoder
from lml._compact import PY2


class PythonObjectEncoder(JSONEncoder):
    def default(self, obj):
        a_list_of_types = (list, dict, str,
                           int, float, bool, type(None))
        if PY2:
            a_list_of_types += (unicode,)
        if isinstance(obj, a_list_of_types):
            return JSONEncoder.default(self, obj)
        return {'_python_object': str(obj)}


def json_dumps(keywords):
    return dumps(keywords, cls=PythonObjectEncoder)
