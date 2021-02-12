

class practice():

    def string_functionalities(self,word:str)-> str:
        length = len(word)
        frist_letter = word[0]
        last_letter = word[-1]
        upper_case = word.upper()
        lower_case = word.lower()
        return "the length:{},first_letter:{},last_letter:{},{},{}".format(length,frist_letter,last_letter,upper_case,lower_case)

    def list_functionalities(self,input_list:list)-> list:
        length = len(input_list)
        if length == 2:
            print('going good')
        elif length >= 3:
            print('very good')
        else:
            ('better luck')

    def dict_functionalities(self,input_dict:dict)-> dict:
        length = len(input_dict)
        while length > 1:
            for i in input_dict:
                print (i)

    def loop_functionalities(self,value:int):
        while value < 10:
            print('value is currently: ',value)
            print('value is still less than 10, adding 1 to value')
            value+=1
            if value==3:
                print('Breaking because value==3')
                break
            else:
                print('continuing...')
                continue

    def list_comprehensions(self,input_list:list)-> list:
        pass

    def employee_check_tuples(self,work_hours:tuple)->tuple:
        """
        top performer
        """
        current_max = 0
        employee_of_month = ''
        
        for employee,hours in work_hours:
            if hours > current_max:
                current_max = hours
                employee_of_month = employee
            else:
                pass
        return (employee_of_month,current_max)

    def lesser_of_two_evens(self,a,b):
        if a%2 == 0 and b%2 == 0:
            return min(a,b)
        else:
            return max(a,b)

    def animal_crackers(self,text):
        wordlist = text.split()
        return wordlist[0][0] == wordlist[1][0]
    
    name = 'This is a global name'

def greet():
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()