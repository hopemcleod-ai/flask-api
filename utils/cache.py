import json

class JSONEncoder(json.JSONEncoder):
    """
        Allow JSON serialisation of a Decimal object by converting them to
        strings. If it's not a Decimal, then let the default function in
        the base class handle it i.e. return an error. If was to try and
        serialise a Decimal, would normally get an error. This class
        converts the Decimal to a string so that it can be serialised.


    Args:
        json (_type_): _description_
    """