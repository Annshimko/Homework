### Task 5.4
#Look through file `modules/legb.py`.

#1) Find a way to call `inner_function` without moving it from inside of `enclosed_function`.


a = "I am global variable!"


def enclosing_function():

    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"

        print(a)

    return inner_function


reach_inner = enclosing_function() #let's call inner_fuction by obtaining it as the result of enclosing_function()
print(reach_inner())