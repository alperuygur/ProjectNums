from fastapi import APIRouter

router = APIRouter()


def is_float(string):
    """
    :param string:
    :return: float as a string type

    Checks the string if it is similar to float (actually having dot(.);
    1- controls the dot(.) if it is not in the first element like .124
    2- if string remains with minus (-) it is acceptable but after that dot(.) can't be the next element like -.124
    3- dot(.) can be the last element, no need to control, it is still float like 124. ->> that means 124.0

    This string is float (Not python type !! )
    """
    try:
        return float(string) \
               and '.' in string \
               and ((string[0] != '.' and '-' not in string) or (string[1] != '.' and string[0] == '-')), string

    except ValueError:
        return False, string


def is_int(string):
    """
    :param string:
    :return: Int as a string type

    Checks if string is numeric also if string's first element starts with minus like -124

    This string is Integer (Not python type !! )
    """
    try:
        return string.isnumeric() \
               or (string[0] == '-' and string[1:].isnumeric()), string
    except ValueError:
        return False, string


def decimal_op(n):
    """
    :param n:
    :return: float with two decimal places only

    Converts float string like;

    12.3455555 ->> 12.34

    No rounding or any other method contains !
    """
    a, b = n[0], n[1]
    if a:
        ind_x = b.index('.')
        dec_b = b[:ind_x+3]
        return dec_b
    else:
        return a


def check_type(n):
    """
    :param n:
    :return: String type info

    Checks string if it is similar to Int or Float else there will be no action

    www.task, -12.rgg, yyy11 ->> this types are not allowed

    Int or Float required
    """
    if is_int(n)[0]:
        return f'Num is Int: {n}'

    elif is_float(n)[0]:
        return f'Num is Float: {n}'

    else:
        return f'Int or Float required'