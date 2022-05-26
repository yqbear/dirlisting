import yaml


ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class Dirlisting:
    """Stores information for requested directory listing."""
    def __init__(self, stream):
        self._data = yaml.load(stream, yaml.SafeLoader)

    def print(self):
        topname, children = self._name_and_children(self._data[0])
        print(topname)
        self._print_children(children)

    def _is_dir(self, entry):
        return isinstance(entry, dict)

    def _name_and_children(self, entry):
        name, children = next(iter(entry.items()))
        if children is None:
            children = []
        return name, children

    def _print_children(self, children, prefix=""):
        num_children = len(children)
        for index, child in enumerate(children):
            if index == num_children - 1:
                connector = ELBOW
                add_prefix = SPACE_PREFIX
            else:
                connector = TEE
                add_prefix = PIPE_PREFIX
            if self._is_dir(child):
                name, next_children = self._name_and_children(child)
                print(f"{prefix}{connector} {name}")
                self._print_children(next_children, prefix + add_prefix)
            else:
                print(f"{prefix}{connector} {child}")
