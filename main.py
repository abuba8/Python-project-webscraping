from bs4 import BeautifulSoup
import requests
import numpy as np
import csv

class screen3():
    @staticmethod
    def s2(batch, get_semester, a, s, address):
        i = int(s)
        url = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Menu=&ShowMenuDetail=&Debug=&DB=PROD&WO=&2504=Y&Dept='+str(a[i][0])+'&Term='+str(batch)+'&Corq=A&Preq=S'
        soup = BeautifulSoup(url, "lxml")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        temp_list1 = []
        temp_list2 = []
        t1 = soup.findAll(True, {"class":["StandardRowOdd", "StandardRowEven", "StandardSubHeader"]})
        for i in range(len(t1)):
            x = t1[i].find_all('td')
            for i in range(5):
                temp_list1.append(x[i].text)
            
            temp_list2.append(temp_list1)

        temp_list3 = []
        temp_list3 = temp_list2[1]
        size = int(len(temp_list3)/5)
        print(str(get_semester)+' > '+ str(a[i][1])+' > Select an option: ')

        a = np.array(temp_list3).reshape(size,5)
        data2 = []
        
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
                data2.append([x1, y1, x2, z1, y2, h, z2, z3])
        temp_list_col = ['Prefix', 'ID', 'Sec', 'Name',' Instructor', 'Hours', 'Seats', 'Enroll.']
         
        for i in range(len(data2)):
            name = data2[i][3]
            name_temp_list = name.split()
            temp = ''
            #x = len(name)
            #print(name[:x])
            for j in range(len(name_temp_list)-2):
                temp = temp+name_temp_list[j][0:5]+' '
            data2[i][3] = temp
            temp2 = ''
            x = len(name_temp_list)-1
            temp2 = temp2+name_temp_list[x]
            data2[i][5] = temp2
            data2[i][6] = int(data2[i][6])
            data2[i][7] = int(data2[i][7])

        print('1) List courses by instructor name') #idk what is instruction name, so i believe its instructor
        print('2) List courses by capacity')
        print('3) List courses by enrollment size')
        print('4) List courses by course prefix')
        print('5) List courses by csv file')
        print('6) Search course by instructor name')
        print('7) Search courses by course prefix')
        print('Q) Go back')

        sort = []
        s = str(input("Selection: "))
        if s == 'Q':
            objx = screen2()
            objx.s_department(get_semester, address, batch)
        if s == '1':
            sort = sorted(data2,key=lambda l:l[4])
            print(temp_list_col)
            for i in range(len(sort)):
                print(sort[i])
        if s == '2':
            sort = sorted(data2,key=lambda l:l[6], reverse=True)
            print(temp_list_col)
            for i in range(len(sort)):
                print(sort[i])
        if s == '3':
            sort = sorted(data2,key=lambda l:l[7], reverse=True)
            print(temp_list_col)
            for i in range(len(sort)):
                print(sort[i])
        if s == '4':
            sort = sorted(data2,key=lambda l:l[0])
            print(temp_list_col)
            for i in range(len(sort)):
                print(sort[i])     
        if s == '5':
            sort = sorted(data2,key=lambda l:l[0])
            select_file_name = str(input('Enter file name: '))
            with open(str(select_file_name)+'.csv', 'w') as f: 
                write = csv.writer(f) 
                write.writerow(temp_list_col) 
                write.writerows(sort)
        if s == '6':
            query = str(input("By by instruction, Enter you search query: "))
            x=0
            for i in range(len(data2)):
                if query == data2[i][4]:
                    screen3.print_col(temp_list_col, x)
                    x = x+1
                    print(data2[i])
            
        if s == '7':
            query = str(input("By by course prefix, Enter you search query: "))
            x=0
            for i in range(len(data2)):
                if query == data2[i][0]:
                    screen3.print_col(temp_list_col,x)
                    x = x+1
                    print(data2[i])

        
    def print_col(temp_list_col, x):
        if x == 0:
            print(temp_list_col)


class screen2():
    @staticmethod
    def ss(n):
        spring = 20
        fall = 80
        summer1 = 40
        summer2 = 50
        word_temp_list = n.split()
        first = word_temp_list[0]
        middle = word_temp_list[1]
        last = word_temp_list[-1]
        if first == 'Spring':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(spring)
            batch_year = str(last)+str(spring)
        if first == 'Fall':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(fall)
            batch_year = str(last)+str(fall)
        if first == 'Summer' and middle == 'I':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(summer1)
            batch_year = str(last)+str(summer1)
        if first == 'Summer' and middle == 'II':
            string = 'http://appsprod.tamuc.edu/Schedule/Schedule.aspx?Term='+str(last)+str(summer2)
            batch_year = str(last)+str(summer2)

        return screen2.s_department(n, string, batch_year)






    @staticmethod
    def s_department(get_semester, address, batch):
        soup = BeautifulSoup(address, "lxml")
        response = requests.get(address)
        soup = BeautifulSoup(response.content, 'html.parser')
        t1 = soup.findAll(True, {"class":["StandardRowOdd", "StandardRowEven"]})
        temp_list1 = []
        temp_list2 = []
        for i in range(len(t1)):
            x = t1[i].find_all('td')
            for i in range(3):
                temp_list1.append(x[i].text)

            temp_list2.append(temp_list1)
            

        
            
        temp_list3 = []
        temp_list3 = temp_list2[1]
        size = int(len(temp_list3)/3)

        a = np.array(temp_list3).reshape(size,3)
        print(get_semester,'> Select a department: ')
        for i in range(len(a)):
            print(i,") ", a[i][1])

        print("Q) Go Back")
        s = str(input("Selection: "))
        if s == 'Q':
            objxx = screen1()
            objxx.select()

        objx = screen3()
        objx.s2(batch, get_semester, a, s, address)





class screen1():
    @staticmethod
    def select():
        source = requests.get('http://appsprod.tamuc.edu/Schedule/Schedule.aspx').text
        soup = BeautifulSoup(source, 'lxml')
        temp_list = []
        data1 = []

        for option in soup.find_all('option'):
            temp_list.append(option['value'])

        data1 = [i for i in temp_list if not 'Mini' in i]
        data1 = data1[:5]
        print('Choose a semester: ')
        for i in range(len(data1)):
            print(i,") ", data1[i])

        s = int(input("Selection: "))
        x = data1[s]
        objx = screen2()
        objx.ss(x) 



obj = screen1()
obj.select()




    
    
