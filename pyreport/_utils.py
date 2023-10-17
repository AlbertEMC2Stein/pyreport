"""Utility functions and classes for pyreport."""

from os import path, listdir

__all__ = ["Switch", "get_tags"]


class Switch:
    """A simple switch class that can be used to toggle between two options.
    Can be called to get the current option."""

    def __init__(self, name, option1, option2):
        """Constructor for the Switch class.

        Parameters
        ----------
        name : str
            The name of the switch.
        option1 : any
            The first option.
        option2 : any
            The second option.
        """

        self.name = name
        self.option1 = option1
        self.option2 = option2
        self.current = option1

    def toggle(self):
        """Toggle the switch."""

        if self.current == self.option1:
            self.current = self.option2
        else:
            self.current = self.option1

    def __call__(self):
        return self.current


#####################################################################


def restricted_get(kwargs, key, allowed_keys_or_type, default):
    """Get a value from a dictionary, but only if it is of a certain type or
    one of a list of allowed values.

    Parameters
    ----------
    kwargs : dict
        The dictionary to get the value from.
    key : str
        The key to get the value for.
    allowed_keys_or_type : list or type
        A list of allowed values or a type that the value must be of.
    default : any
        The default value to return if the key is not in the dictionary.
    """

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
    """Get a list of tags in a git repository.

    Parameters
    ----------
    root : str
        The root of the git repository.
    """

    tags_path = path.join(root, ".git/refs/tags")
    def get_creation_time(item):
        item_path = path.join(tags_path, item)
        return path.getctime(item_path)

    items = listdir(tags_path)
    sorted_items = sorted(items, key=get_creation_time)
    return sorted_items


def indented_write(file, n, text, end="\n"):
    """Write text to a file with a given indentation.

    Parameters
    ----------
    file : file
        The file to write to.
    n : int
        The number of tabs to indent the text with.
    text : str
        The text to write.
    end : str
        The end character to use when writing the text.
    """

    file.write("\t" * n + text + end)
    