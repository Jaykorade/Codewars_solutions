def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

n = [1,2,3,4,5,6,7,8,9,0]
create_phone_number(n)