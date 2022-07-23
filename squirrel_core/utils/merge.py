

def dict_deep_merge(a: dict, b: dict) -> dict:
    """
    Merge two dictionaries.
    """
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                # Recursive for dict merge.
                try:
                    dict_deep_merge(a[key], b[key])
                except TypeError as e:
                    raise TypeError(f'{key}.{e}') from None
            elif isinstance(a[key], dict) and not isinstance(b[key], dict):
                # dict is fist here. None dict values cannot merge to dict keys.
                raise TypeError(f"{key}:Cannot merge a dictionary with other types.")
            elif a[key] == b[key]:
                # Same value, do nothing.
                pass
            elif isinstance(a[key], list) and isinstance(b[key], list):
                # Merge list.
                a[key].extend(b[key])
            elif isinstance(a[key], set) and not isinstance(b[key], set):
                # Merge set.
                a[key] = a[key] | b[key]
            else:
                # Merge other types.
                a[key] = b[key]
        else:
            a[key] = b[key]
    return a
