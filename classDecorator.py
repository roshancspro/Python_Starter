def limiter(limit, unique, lookup):
    def wrapper(class_):
        instances = {}
        lookups = {}

        def getinstance(*args, **kwargs):
            new_obj = class_(*args, **kwargs)
            if "FIRST" not in lookups: lookups["FIRST"] = new_obj

            id = getattr(new_obj, unique)
            if id in instances:
                res = instances[id]
            elif len(instances) < limit:
                instances[id] = new_obj
                res = lookups["LAST"] = new_obj
            else:
                res = lookups[lookup]
            
            lookups["RECENT"] = res
            return res
        return getinstance
    return wrapper