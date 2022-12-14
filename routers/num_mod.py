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



data_type = {'Z': '0-1000',
             'K': '1000-1000000',
             'M': '1000000-1000000000',
             'B': '1000000000-1000000000000',
             'T': '1000000000000-1000000000000000',
             'q': '1000000000000000-1000000000000000000',
             'Q': '1000000000000000000-1000000000000000000000',
             's': '1000000000000000000000-1000000000000000000000000',
             'S': '1000000000000000000000000-1000000000000000000000000000'
             }

def num_mod_act(n):
    """
    :param n:
    :return: Int to output format

    converts request string to output format like ->> 1000 to 1K
    """
    if is_int(n)[0]:
        if n[0] == '-':
            add_minus = '-'
            int_n = int(str(n[1:]))

            for key, val in data_type.items():
                if int(val.split('-')[0]) <= int_n < int(val.split('-')[1]):
                    if key != 'Z':
                        int_val = str(float(int_n / int(val.split('-')[0])))[:3]
                        return add_minus + int_val.rstrip('.0') + key if '.0' in int_val else add_minus + int_val.rstrip('.') + key

                    else:
                        return add_minus + str(int_n)

            else:
                return 'No data to display, out of range !'
        else:
            int_n = int(n)

            for key, val in data_type.items():
                if int(val.split('-')[0]) <= int_n < int(val.split('-')[1]):
                    if key != 'Z':
                        int_val = str(float(int_n / int(val.split('-')[0])))[:3]
                        return int_val.rstrip('.0') + key if '.0' in int_val else int_val.rstrip('.') + key

                    else:
                        return str(int_n)
            else:
                return 'No data to display, out of range !'


    elif is_float(n)[0]:
        if n[0] == '-':
            add_minus = '-'
            float_n = float(str(decimal_op(is_float(n)))[1:])

            for key, val in data_type.items():
                if int(val.split('-')[0]) <= float_n < int(val.split('-')[1]):
                    if key != 'Z':
                        int_val = str(float(float_n / int(val.split('-')[0])))[:3]
                        return add_minus + int_val.rstrip('.0') + key if '.0' in int_val else add_minus + int_val.rstrip('.') + key

                    else:
                        return add_minus + str(float_n)
            else:
                return 'No data to display, out of range !'
        else:

            float_n = float(decimal_op(is_float(n)))
            print(float_n)
            for key, val in data_type.items():
                if int(val.split('-')[0]) <= float_n < int(val.split('-')[1]):
                    if key != 'Z':
                        int_val = str(float(float_n / int(val.split('-')[0])))[:3]
                        return int_val.rstrip('.0') + key if '.0' in int_val else int_val.rstrip('.') + key
                    else:
                        return str(float_n)
            else:
                return 'No data to display, out of range !'

    else:
        return 'Output not allowed for that request !'