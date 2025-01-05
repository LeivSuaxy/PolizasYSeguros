def generate_code(length=6):
    """
    Generate a random code of length n
    Util for generating verification codes
    :param length: Length of the code
    :return: A random code
    """

    import random
    import string

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))