### Task 4.4
#Look through file `modules/legb.py`.
#2.1) Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a #let's replace line with reference to "global a" variable
        print(a)

    return inner_function
a = "I am global variable!"
reach_inner = enclosing_function()
print(reach_inner())