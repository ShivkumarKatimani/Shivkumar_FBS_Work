#1. To neglect positional para concept
#2. Assign value to parameter in function call
#3. name of parameter in function definition and fuction call should be same
#4. flow from right to left 
#(why - positional para flow from left to right

def  emp (id, name , sal, dept):
    print('id:',id)
    print('Name:',name)
    print('sal:',sal)
    print('Department:',dept)


emp(name='abc',sal=20000,dept= 'IT', id = 123)