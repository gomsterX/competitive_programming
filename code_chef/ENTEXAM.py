#Problem ID: ENTEXAM
#Problem Name: Entrance Exam

for _ in range(int(input())):
    n, k, e, m = map(int, input().split())
    l = []
    for i in range(n-1):
        l.append(sum(list(map(int, input().split()))))
    ser = sum(list(map(int, input().split())))
    l.sort(reverse = True)
    min_score = l[k-1]+1 -ser
    if(min_score <= m):
        print(min_score) if min_score > 0 else print(0)
    else:
        print("Impossible")

