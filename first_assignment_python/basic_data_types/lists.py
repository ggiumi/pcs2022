if __name__ == '__main__':
    N = int(input())
    list =[]
    for i in range(N):
        list.append(input().split())

    result=[]
    for i in range(N):
        if list[i][0]=='insert':
            result.insert(int(list[i][1]),int(list[i][2]))
        elif list[i][0]=='print':
            print(result)
        elif list[i][0]=='remove':
            result.remove(int(list[i][1]))
        elif list[i][0]=='append':
            result.append(int(list[i][1]))
        elif list[i][0]=='pop':
            result.pop()
        elif list[i][0]=='sort':
            result.sort()
        elif list[i][0]=='reverse':
            result.reverse()
