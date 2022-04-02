if __name__ == '__main__':
    N = int(input())
    
    my_list = []
    for _ in range(N):
        command = input().split()
        name, *args = command
        if name == "print":
            print(my_list)
        else:
            args = "(" + ",".join(args) + ")"
            eval("my_list." + name + args)
