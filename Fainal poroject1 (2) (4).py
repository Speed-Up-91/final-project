import random as r
class SimpleCalculator:
    def __init__(self):
       self. history = []
        
    def add(self, a, b):
        result = a + b
        self.history.append(result)
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(result)
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(result)
        return result
        
    def divide(self, a, b):
        if b == 0:
            return "EROR : You can't us 0"
        result = a / b
        self.history.append(result)
        return result


    def save_history(self, filename):
       with open(filename ,'w')as file:
           for entry in self.history:
               file.write(str(entry+'/n'))

    def load_history(self, filename):
        try:
             with open (filename, 'r')as file:
                  self.history =file.readlines()
                  self.history=[entry.strip()for entry in self.history]
        except FileNotFoundError:
             print('file not found.')
        
    def Random(self):
         
             operations=[self.add(a,b),self.subtract(a,b),self.multiply(a,b), self.divide(a,b)]
             
             return r.choice(operations)

    def run():

        c=SimpleCalculator()
       
        while True:
            print('''1.Add
2.Subtract
3.Multiply
4.Divide
5.Random
6.Turn off Calculator
7.ذخيره تاريخچه
8. بارگذاري تاريخچه''')           
                   
            s=input('Select an option (1-5): ')
            try:
        
                if  s == '1':
                    a=float(input('please enter number 1 : '))
                    b=float(input('please enter number 2 : '))
                    print(c.add(a,b))

                elif s == '2':
                    a=float(input('please enter number 1 : '))
                    b=float(input('please enter number 2 : '))
                    print(c.subtract(a,b))

                elif s == '3':
                    a=float(input('please enter number 1 : '))
                    b=float(input('please enter number 2 : '))
                    print(c.multiply(a,b))

                elif s == '4':
                    a=float(input('please enter number 1 : '))
                    b=float(input('please enter number 2 : '))
                    print(c.divide(a,b))
            except ValueError:
                print('enter the carect number')
            if s == '5':
                try:
                    a=float(input('please enter number 1 : '))
                    b=float(input('please enter number 2 : '))
                    print(c.Random(a,b))
                except ValueError:
                    print('eror')

            elif s=='7':
                filename=input('enter your file')
                c.save_history(filename)
                print('save do it')

            elif s=='8':
                filename=input('enter your file')
                c.load_history(filename)
                print('load do it')
             
            elif s == '6':
                print('Turn offing Calculator...')
                break
            else:
                print('Eror.Please try agin.')

           
#if __name__=="__run___":
#    run()
Calculator =SimpleCalculator.run()
print(Calculator)
