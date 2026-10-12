#1. to pass multiple para with meaning
#2. mention 2 asterisk symbol before para name function definition
#3. passed data will be store dictionary format
#4. use for loop to iterate values on dict.iteam()

def emp (**data):
    for key, val in data.items():
        print(key,':',val)

emp(id = 101 ,  name = 'abc', sal = 40000 , dept = 'IT')