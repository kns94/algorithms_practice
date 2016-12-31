def flatten_key(key, value):

    new_dict = {}

    for sk, sv in value.iteritems():
        if type(sv) == dict:
            new_vals = flatten_key(sk, sv)
            for ssk, ssv in new_vals.iteritems():
                new_key = "{}.{}".format(key, ssk)
                new_dict[new_key] = ssv
        else:
            new_key = "{}.{}".format(key, sk)
            new_dict[new_key] = sv

    return new_dict

def flatten(obj):

    original_keys = obj.keys()

    for key in original_keys:
        if type(obj[key]) == dict:
            p_key = key
            temp_vals = obj[key]
            del obj[key]

            flattened = flatten_key(key, temp_vals)
            obj.update(flattened)

    return obj

inp = {'x':1, 'y':1, 'z':{'a':{'k':1, 'c': {'d': 9}},'b':2}} 
#print flatten_key('z', {'a': {'b':2, 'c': 3}})
print flatten(inp)