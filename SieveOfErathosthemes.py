def main():
    n = input("Input N: ")
    
    prime = [ ]
    list = range(2, n+1)
    
    while len(list) != 0:
        test = list[0]
        prime.append(test)
        for num in list:
            if num % test == 0:
                list.remove(num)

    print prime

if __name__ == '__main__': main()
