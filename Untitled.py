from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
source = requests.get('http://appsprod.tamuc.edu/Schedule/Schedule.aspx').text


soup = BeautifulSoup(source, 'lxml')
list = []
final_list = []


for option in soup.find_all('option'):
    list.append(option['value'])



final_list = [i for i in list if not 'Mini' in i]
final_list = final_list[:5]



sel = 'fall'

class program():
    @staticmethod
    def select():
        print('Choose a semester: ')
        for i in range(len(final_list)):
            print(i,") ", final_list[i])

        selection = int(input("Selection: "))
       # if selection < 6 and selection>=0:
        x = final_list[selection]
        #print(x)
        program.selections(x) #semester name sending
    #    else:
     #       print("Wrong selection kindly try again")
      #      select()

    @staticmethod
    def selections(n):
        spring = 20
        fall = 80
        summer1 = 40
        summer2 = 50
        word_list = n.split()
        first = word_list[0]
        middle = word_list[1]
        last = word_list[-1]
        #print(first, middle, last)
        if first == 'Spring':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(spring)
            f1 = str(last)+str(spring)
            #print(string)
        if first == 'Fall':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(fall)
            f1 = str(last)+str(fall)
            #print(string)
        if first == 'Summer' and middle == 'I':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(summer1)
            f1 = str(last)+str(summer1)
            #print(string)
        if first == 'Summer' and middle == 'II':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(summer2)
            f1 = str(last)+str(summer2)
            #print(string)

        return program.selection_department(n, string, f1)











    @staticmethod
    def selection_department(get_semester, get_link, year):
        soup = BeautifulSoup(get_link, "lxml")
        #headers = {'Code', 'Name', 'Prefixes'}
        response = requests.get(get_link)
        #response.status_code
        soup = BeautifulSoup(response.content, 'html.parser')
        t1 = soup.findAll(True, {"class":["StandardRowOdd", "StandardRowEven"]})
        list1 = []
        list2 = []
        for i in range(len(t1)):
            x = t1[i].find_all('td')
            for i in range(3):
                list1.append(x[i].text)

            list2.append(list1)
            

        
            
        list3 = []
        list3 = list2[1]
        size = int(len(list3)/3)

        a = np.array(list3).reshape(size,3)
        #print(a)
        print(get_semester,'>Select a department: ')
        for i in range(len(a)):
            print(i,") ", a[i][1])

        print("Q  ) Go Back")
        selection = str(input("Selection: "))
        if selection == 'Q':
            program.select()

        program.selection2(year, get_semester, a, selection, get_link)




    @staticmethod
    def selection2(year, get_semester, a, selection, get_link):
        #print(year)
        #print(get_semester)
        #print(selection)
        i = int(selection)
        #print(a[i][1])
        url = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Menu=&ShowMenuDetail=&Debug=&DB=PROD&WO=&2504=Y&Dept='+str(a[i][0])+'&Term='+str(year)+'&Corq=A&Preq=S'
        #print(url)

        soup = BeautifulSoup(url, "lxml")
        #headers = {'Code', 'Name', 'Prefixes'}
        response = requests.get(url)
        #response.status_code
        soup = BeautifulSoup(response.content, 'html.parser')
        list1 = []
        list2 = []
        t1 = soup.findAll(True, {"class":["StandardRowOdd", "StandardRowEven", "StandardSubHeader"]})
        for i in range(len(t1)):
            x = t1[i].find_all('td')
            for i in range(5):
                list1.append(x[i].text)
            
            list2.append(list1)

        list3 = []
        list3 = list2[1]
        size = int(len(list3)/5)
        print(str(get_semester)+' > '+ str(a[i][1])+' > Select an option: ')

        a = np.array(list3).reshape(size,5)
        #print(a)
        final_list1 = []
        
        
        for i in range(len(a)):
            if a[i][4] == '':
                x1 = a[i][0]
                y1 = a[i][1]
                z1 = a[i][2]
            else:
                x2 = a[i][0]
                y2 = a[i][2]
                z2 = a[i][3]
                z3 = a[i][4]
                h = 0
                final_list1.append([x1, y1, x2, z1, y2, h, z2, z3])
        list_col = ['Prefix', 'ID', 'Sec', 'Name',' Instructor', 'Hours', 'Seats', 'Enroll.']
        #print(list_col)
        #for i in range(len(final_list1)):
        #    print(final_list1[i])
        
        
        for i in range(len(final_list1)):
            name = final_list1[i][3]
            name_list = name.split()
            temp = ''
            #x = len(name)
            #print(name[:x])
            for j in range(len(name_list)-2):
                temp = temp+name_list[j][0:5]+' '
            final_list1[i][3] = temp
            temp2 = ''
            x = len(name_list)-1
            temp2 = temp2+name_list[x]
            final_list1[i][5] = temp2
            final_list1[i][6] = int(final_list1[i][6])
            final_list1[i][7] = int(final_list1[i][7])


            
        
        
        print('1 ) List courses by instructor name') #idk what is instruction name, so i believe its instructor
        print('2 ) List courses by capacity')
        print('3 ) List courses by enrollment size')
        print('4 ) List courses by course prefix')
        print('5 ) List courses by csv file')
        print('6 ) Search course by instructor name')
        print('7 ) Search courses by course prefix')
        print('Q ) Go back')

        sort = []
        selection = str(input("Selection: "))
        if selection == 'Q':
            program.selection_department(get_semester, get_link, year)
        if selection == '1':
            sort = sorted(final_list1,key=lambda l:l[4])
            print(list_col)
            for i in range(len(sort)):
                print(sort[i])
        if selection == '2':
            sort = sorted(final_list1,key=lambda l:l[6], reverse=True)
            print(list_col)
            for i in range(len(sort)):
                print(sort[i])
        if selection == '3':
            sort = sorted(final_list1,key=lambda l:l[7], reverse=True)
            print(list_col)
            for i in range(len(sort)):
                print(sort[i])
        if selection == '4':
            sort = sorted(final_list1,key=lambda l:l[0])
            print(list_col)
            for i in range(len(sort)):
                print(sort[i])     
        if selection == '5':
            sort = sorted(final_list1,key=lambda l:l[0])
            select_file_name = str(input('Enter file name: '))
            with open(str(select_file_name)+'.csv', 'w') as f: 
                write = csv.writer(f) 
                write.writerow(list_col) 
                write.writerows(sort)
        if selection == '6':
            query = str(input("By by instruction, Enter you search query: "))
            x=0
            for i in range(len(final_list1)):
                if query == final_list1[i][4]:
                    program.print_col(list_col, x)
                    x = x+1
                    print(final_list1[i])
            
        if selection == '7':
            query = str(input("By by course prefix, Enter you search query: "))
            x=0
            for i in range(len(final_list1)):
                if query == final_list1[i][0]:
                    program.print_col(list_col,x)
                    x = x+1
                    print(final_list1[i])


            
        
        
    def print_col(list_col, x):
        if x == 0:
            print(list_col)

    
    
obj = program()
obj.select()