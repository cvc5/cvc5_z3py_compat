from cvc5_pythonic_api import *
a = StringVal('hello world')
b = String('b')
solve(Contains(b,a))
solve(Contains(a,b),PrefixOf(a,b))
solve(Contains(a,b),SuffixOf(a,b))
solve(PrefixOf(a,b),SubString(b,0,2)==StringVal('HE'))
solve(IndexOf(b,a) == 3,b>a,IndexOf(b,a,2)==8)
solve(Replace(a,'h','r')==b)

