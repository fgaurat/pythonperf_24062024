





# NameError : UpperCamelCase, PascalCase
# nameError : camelCase
# name_error : snake_case
# name-error : kebab-case

a=2

def main():
    global a
    # print("main",a)
    a=12
    print("main",a)

if __name__=='__main__':
    print("before main",a)
    main()
    print("after main",a)
