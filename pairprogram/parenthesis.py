Callum and Mark
```def balanced(par):
    if par[0] == ')':
        return False
    else:
        opens = 0
        closed = 0
        for i in xrange(len(par)):
            if par[i] == '(':
                opens += 1
                for j in xrange(len(par[i:])):
                    if par[j] == ')':
                        closed += 1
                        break

    return (closed == opens) and (closed + opens == len(par))

print balanced("(()()()())")
print balanced("(((())))")
print balanced("(()((())()))")
print balanced("((((((())")
print balanced("()))")
print balanced("(()()))(()")