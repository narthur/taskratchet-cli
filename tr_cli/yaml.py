import os
import yaml


class Yaml:
    @staticmethod
    def load(rel_path):
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = '%s/%s' % (base_path, rel_path)
        abs_path = os.path.abspath(full_path)
        is_safe = abs_path.startswith(base_path)

        if not is_safe:
            return {}

        try:
            file = open(abs_path, "r")
            result = yaml.load(file, Loader=yaml.FullLoader)
            file.close()

            return result
        except FileNotFoundError:
            return {}
