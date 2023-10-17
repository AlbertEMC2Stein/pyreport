import os.path as path
from os import listdir

__all__ = ["Switch", "get_tags"]


class Switch:
    def __init__(self, name, option1, option2):
        self.name = name
        self.option1 = option1
        self.option2 = option2
        self.current = option1

    def toggle(self):
        if self.current == self.option1:
            self.current = self.option2
        else:
            self.current = self.option1

    def __call__(self):
        return self.current


#####################################################################


def restricted_get(kwargs, key, allowed_keys_or_type, default):
    if key in kwargs:
        if isinstance(allowed_keys_or_type, list):
            if kwargs[key] in allowed_keys_or_type:
                return kwargs[key]
            else:
                raise TypeError(
                    f"Value for '{key}' must be one of {allowed_keys_or_type}."
                )
        elif isinstance(allowed_keys_or_type, type):
            if isinstance(kwargs[key], allowed_keys_or_type):
                return kwargs[key]
            else:
                raise TypeError(
                    f"Value for '{key}' must be of type {allowed_keys_or_type}."
                )
    else:
        return default


def get_tags(root):
    tags_path = path.join(root, ".git/refs/tags")
    def get_creation_time(item):
        item_path = path.join(tags_path, item)
        return path.getctime(item_path)

    items = listdir(tags_path)
    sorted_items = sorted(items, key=get_creation_time)
    return sorted_items


def indented_write(file, n, text, end="\n"):
    file.write("\t" * n + text + end)
    