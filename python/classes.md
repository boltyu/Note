# note <https://docs.python.org/zh-cn/3/tutorial/classes.html>

## 作用域示例

    def scope_test():
        def do_local():
            spam = "local spam"

        def do_nonlocal():
            nonlocal spam
            spam = "nonlocal spam"

        def do_global():
            global spam
            spam = "global spam"

        spam = "test spam"
        do_local()
        print("After local assignment:", spam)
        do_nonlocal()
        print("After nonlocal assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)

    # The output of the example code is:

    # After local assignment: test spam
    # After nonlocal assignment: nonlocal spam
    # After global assignment: nonlocal spam
    # In global scope: global spam

## 作用域示例2

    # tricks 由所有 Dog 实例共享
    class Dog:
        tricks = []  
    
    # tricks 仅属于创建的 Dog 实例
    class Dog:
        def __init__(self);
            self.tricks = []  

    # private
    __name

    # 'weak' private
    _name