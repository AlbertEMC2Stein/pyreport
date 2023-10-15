__all__ = ['switch']


class switch:
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
                raise TypeError(f"Value for '{key}' must be one of {allowed_keys_or_type}.")
        elif isinstance(allowed_keys_or_type, type):
            if isinstance(kwargs[key], allowed_keys_or_type):
                return kwargs[key]
            else:
                raise TypeError(f"Value for '{key}' must be of type {allowed_keys_or_type}.")
    else:
        return default