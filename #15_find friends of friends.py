# def print_all_friends(g, start):  #모든 친구를 찾는 알고리즘
#     qu = []
#     done = set()
#
#     qu.append(start)    #list에 추가
#     done.add(start)     #set에 추가
#
#     while qu:
#         p = qu.pop(0)
#         print(p)
#
#         for x in g[p]:
#             if x not in done:
#                 qu.append(x)
#                 done.add(x)
#
# fr_info = {
#     'Summer': ['John', 'Justin', 'Mike'],
#     'John': ['Summer', 'Justin'],
#     'Justin': ['John', 'Summer', 'Mike', 'May'],
#     'Mike': ['Summer', 'Justin'],
#     'May': ['Justin', 'Kim'],
#     'Kim': ['May'],
#     'Tom': ['Jerry'],
#     'Jerry': ['Tom']
# }
#
# print_all_friends(fr_info, 'Summer')
# print()
# print_all_friends(fr_info, 'Jerry')

def print_all_friends(g, start):    #모든 친구를 찾아서 친밀도를 계산하는 알고리즘
    qu = []
    done = set()

    qu.append((start, 0))    #list에 추가
    done.add(start)     #set에 추가

    while qu:
        (p, d) = qu.pop(0)  #(사람 이름, 친밀도)
        print(p, d)

        for x in g[p]:
            if x not in done:
                qu.append((x, d + 1))
                done.add(x)

fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')
