import pandas as pd
pd.options.display.max_rows=10000

num_input=[75, 2, 8, 9, 2, 4]
#num_input=[50, 9, 3, 2, 4, 7]

target=1

nums=tuple(sorted(num_input))
nums_hash=hash(nums)

oper=['+', '-', '*', '/']

ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y), "*": (lambda x,y: x*y), "/": (lambda x,y: x/y)}


df = pd.DataFrame(columns=['eqn', 'eqn_key', 'eqn_val'])


for n1 in nums:
    for n2 in nums:
        for n3 in nums:
            for n4 in nums:
                for n5 in nums:
                    for n6 in nums:
                        if(hash(tuple(sorted([n1,n2,n3,n4,n5,n6]))) == nums_hash):
                            for o1 in oper:
                                for o2 in oper:
                                    for o3 in oper:
                                        for o4 in oper:
                                            for o5 in oper:
                                                try:
                                                    if ops[o5](ops[o4](ops[o3](ops[o2](ops[o1](n1,n2),n3),n4),n5),n6)==target:
                                                        eqn=' '.join(map(str, ['(', n1, o1, n2, o2, n3, o3, n4, o4, n5, o5, n6, ')']))
                                                        eqn_key=' '.join(map(str, [n1, o1, n2, o2, n3, o3, n4, o4, n5, o5, n6]))
                                                        eqn_val= ops[o5](ops[o4](ops[o3](ops[o2](ops[o1](n1,n2),n3),n4),n5),n6)
                                                        df=df.append(pd.DataFrame(data=[[eqn, eqn_key, eqn_val]], columns=['eqn', 'eqn_key', 'eqn_val']), ignore_index=True)
                                                        #print(eqn, eqn_key)
                                                except ZeroDivisionError:
                                                    pass
                                                try:
                                                    if ops[o4](ops[o2](ops[o1](n1,n2), ops[o3](n3,n4)), ops[o5](n5,n6))==target:
                                                        eqn=' '.join(map(str, ['((', n1, o1, n2, ')', o2, '(', n3, o3, n4, ')', o4, '(', n5, o5, n6, '))']))
                                                        eqn_key=' '.join(map(str, [n1, o1, n2, o2, n3, o3, n4, o4, n5, o5, n6]))
                                                        eqn_val= ops[o5](ops[o4](ops[o3](ops[o2](ops[o1](n1,n2),n3),n4),n5),n6)
                                                        df=df.append(pd.DataFrame(data=[[eqn, eqn_key, eqn_val]], columns=['eqn', 'eqn_key', 'eqn_val']), ignore_index=True)
                                                        #print(eqn, eqn_key)
                                                except ZeroDivisionError:
                                                    pass
                                                try:
                                                    if ops[o3](ops[o2](ops[o1](n1,n2),n3), ops[o5](ops[o4](n4,n5),n6))==target:
                                                        eqn=' '.join(map(str, ['(((', n1, o1, n2, ')', o2, n3, ')', o3, '((', n4, o4, n5, ')', o5, n6, '))']))
                                                        eqn_key=' '.join(map(str, [n1, o1, n2, o2, n3, o3, n4, o4, n5, o5, n6]))
                                                        eqn_val= ops[o5](ops[o4](ops[o3](ops[o2](ops[o1](n1,n2),n3),n4),n5),n6)
                                                        df=df.append(pd.DataFrame(data=[[eqn, eqn_key, eqn_val]], columns=['eqn', 'eqn_key', 'eqn_val']), ignore_index=True)
                                                        #print(eqn, eqn_key)
                                                except ZeroDivisionError:
                                                    pass
                                                try:
                                                    if ops[o4](ops[o3](ops[o2](ops[o1](n1,n2),n3),n4), ops[o5](n5,n6))==target:
                                                        eqn=' '.join(map(str, ['((((', n1, o1, n2, ')', o2, n3, ')', o3, n4, ')', o4, '(', n5, o5, n6, '))']))
                                                        eqn_key=' '.join(map(str, [n1, o1, n2, o2, n3, o3, n4, o4, n5, o5, n6]))
                                                        eqn_val= ops[o5](ops[o4](ops[o3](ops[o2](ops[o1](n1,n2),n3),n4),n5),n6)
                                                        df=df.append(pd.DataFrame(data=[[eqn, eqn_key, eqn_val]], columns=['eqn', 'eqn_key', 'eqn_val']), ignore_index=True)
                                                        #print(eqn, eqn_key)
                                                except ZeroDivisionError:
                                                    pass
df.sort_values(by='eqn_val', inplace=True)
df.drop_duplicates(subset='eqn_val', keep='first', inplace=True)
print(df['eqn'])
