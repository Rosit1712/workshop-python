def standard_arg(arg):
    print(arg)

def pos_only_arg(arg,/):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)