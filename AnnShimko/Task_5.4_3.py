### Task 5.4
#Look through file `modules/legb.py`.
#2.2) Modify ONE LINE in `inner_function` to make it print variable 'a' from enclosing function.

def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():
        #let's delete variable declaration 'a' from inner function
        print(a)

    return inner_function
a = "I am global variable!"
reach_inner = enclosing_function()
print(reach_inner())