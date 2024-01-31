l = [3,3,2,1,4,3,7]
res = []
max_stack = 0
for e in l:
    if e %2==1:
        res.insert(0,e)
    else:
        old =res.pop(0)
        if old > e:
            res.insert(0, e)
    max_stack = max(max_stack, len(res))

print(max_stack)