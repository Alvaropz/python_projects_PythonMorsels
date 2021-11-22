def pluck(d, *key, sep=".", default=""):
    if len(key) == 1:
        key = separator(key[0], sep)
        return checker(d, key, default)
    else:
        list_otucome = []
        for val in key:
            val = separator(val, sep)
            list_otucome.append(checker(d, val, default))
        return tuple(list_otucome)

def separator(key, sep="."):
    if sep == ".":
        keys = key.split(".")
    elif sep == "/":
        keys = key.split("/")
    elif sep == " ":
        keys = key.split(" ")
    return keys

def checker(d, keys, default=""):
    if keys[0] in d:
        if len(keys) == 1:
            return d[keys[0]]
        elif len(keys) == 2:
            if keys[1] in d[keys[0]]:
                return d[keys[0]][keys[1]]
            elif default is None:
                return None
            elif default is not "":
                return default
            else:
                raise KeyError(keys[1])
        elif len(keys) == 3:
            if keys[2] in d[keys[0]][keys[1]]:
                return d[keys[0]][keys[1]][keys[2]]
            elif default is None:
                return None
            elif default is not "":
                return default
            else:
                raise KeyError(keys[2])
        elif len(keys) == 4:
            if keys[3] in d[keys[0]][keys[1]][keys[2]]:
                return d[keys[0]][keys[1]][keys[2]][keys[3]]
            elif default is None:
                return None
            elif default is not "":
                return default
            else:
                raise KeyError(keys[3])
        elif len(keys) == 5:
            if keys[4] in d[keys[0]][keys[1]][keys[2]][keys[3]]:
                return d[keys[0]][keys[1]][keys[2]][keys[3]][keys[4]]
            elif default is None:
                return None
            elif default is not "":
                return default
            else:
                raise KeyError(keys[4])
    elif default is None:
        return None
    elif default is not "":
        return default
    else:
        raise KeyError(keys[0])