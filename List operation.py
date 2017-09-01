print("Start of Execution")
    N = int(raw_input())
    list = []
    for i in range(N):
           data = raw_input()
           data = data.split()
            if data[0] == "insert" :
                list.insert(int(data[1]),data[2])
            elif data[0] == "print" :
                print(list)
            elif data[0] == "remove" :
                list.remove (data[1])
            elif data[0] == "append" :
                list.append (data[1])
            elif data[0] == "sort" :
                list.sort ()
            elif data[0] == "pop" :
                list.pop()
            else :
                list.reverse()
            
