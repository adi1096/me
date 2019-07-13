def y(x):
    result = 0
    for i in range(1, x + 1):
        result = result * 10 + i
    return result







'''

for i in range(10): 
    for n in range(10): 
        print(i, end=' ')
    print('\n')


'''

'''
# Python program to print list 
# using for loop 
a = ([1, 2, 3, 4, 5])
# printing the list using loop 
for x in range(len(a)): 
    print (a[x])

'''

'''
for x in range(10):
    for i in range(10):
       print(x)
    print('\n')
'''

'''
A = [[1,2,3,4],[4,5,6,4],[7,8,9,4],[1,2,3,4],[1,2,3,4]]
f = 1
print(A)
for i in range(5):
    f *= 10
    for j in range(4):
       A[i][j] *= f
print(A)

'''

'''

# traverse2.py

n = [0,1,2,3,4,5,6,7,8,9]

i = 0
s = len(n)

while i < s:
    
    print(n[i], end=" ")
    i = i + 1

print()

'''

'''
def loops_2(number_of_items2=10, symbol_2=['*']):

    n_list = []
    for i in range(number_of_items2):
        n_list.append(symbol_2*10)
    return n_list

def lp(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    if some_kind_of_list is not None:
        print("\n" + exercise_name)
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print(column, end="")
                print()
        else:
            for column in some_kind_of_list:
                print(column, end="")
            print()
    else:
        print(exercise_name, "maybe you haven't got to this one yet?")


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    lp(loops_2(), "loops_2")


'''

