def main():
    l= [10,20,30,40,50]

    found = False

    for i in l:
        if i == found:
            found = True


    # if found:
    #     print("ok")
    # else:
    #     print("ko")

    result = "ok" if found else "ko"
    print(result)
    
    l= [10,20,30,40,50]
    for i in l:
        if i == found:
            break
    else:
        print("not found")

if __name__=='__main__':
    main()
