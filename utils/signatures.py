from django.utils.crypto import get_random_string


def code_gen(model):
    code = get_random_string(length=8).lower()
    if model.objects.filter(code=code).exists():
        return code_gen(model)
    else:
        return code


def make_random_digits(digits):
    import random
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return str(random.randint(lower, upper))
