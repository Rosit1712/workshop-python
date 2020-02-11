#contoh function
def standard_arg(arg):
    print(arg)

#def pos_only_arg(arg, /):
 #   print(arg)

def kwd_only_arg(*,arg):
    print(arg)

#def combined_example(post_only, /, standard,*, kwd_only):
 #   print(pos_only,standard,kwd_only)

standard_arg(2)
standard_arg(arg=2)
#post_only_arg(1)
#kwd_only_org(3)
#kwd_only_arg(arg=3)

def foo(name,**kwds):
    return 'name' in kwds

#foo(1,**{'name':2}) #hapus # didepan foo untuk mencoba

#def foo2(name,/,**kwds):
 #   return 'name' in kwds
 #foo2(1, **{'name': 2})