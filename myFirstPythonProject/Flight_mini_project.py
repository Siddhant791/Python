'''
Created on Sep 20, 2020

@author: SIDDHANT
'''
from ntpath import split
class Node:
    def __init__(self,name,next):
        self.name=name
        self.next=next
        
class Flight_List:
    head=None
    def __init__(self,Flight_number):
        self.Flight_number=Flight_number
    
    def insert_in_begining(self,name):
        node=Node(name,self.head)
        self.head=node
    
    def insert_in_end(self,name):
        if self.head is None:
            self.head=Node(name,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(name,None)   
    def remove_by_name(self,name):
        itr=self.head
        x=None
        while itr: 
            if itr.name==name:
                if x is None:
                    self.head=itr.next
                    return
                x.next=itr.next
                return
            x=itr   
            itr=itr.next
        else:
            print("No Passenger with this name found")   
    def print_all_Nodes(self):
        if self.head is None:
            print("No Passenger")
            return
        itr=self.head
        while itr:
            print(itr.name)
            itr=itr.next
    
    def print_no_of_passengers(self):
        if self.head is None:
            print("0")
            return
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        print(count)
if __name__=='__main__':
    input_data=input().split()
    input_list=[]
    for i in range(8):
        input_data_operation=input().split()
        #print("s")
        input_list.append(input_data_operation)
    list_of_flights=[]
    n=int(input_data[0])
    for i in range(n):
        list_of_flights.append(Flight_List(input_data[i+1]))
    
    for i in input_list:
        n=int(i[0])
        if n==1:
            input_flight_number=i[1]
            no_of_passengers_to_be_added=int(i[2])
            for k in list_of_flights:
                if k.Flight_number==input_flight_number:
                    for j in range(no_of_passengers_to_be_added):
                        k.insert_in_end(i[j+3])
        elif n==2:
            input_flight_number=i[1]
            no_of_passengers_to_be_cancel=int(i[2])
            for k in list_of_flights:
                if k.Flight_number==input_flight_number:
                    for j in range(no_of_passengers_to_be_cancel):
                        k.remove_by_name(i[j+3])
        
        elif n==3:
            input_flight_number=i[1]
            for k in list_of_flights:
                if k.Flight_number==input_flight_number:
                    k.print_all_Nodes()
        
        elif n==4:
            input_flight_number=i[1]
            for k in list_of_flights:
                if k.Flight_number==input_flight_number:
                    k.print_no_of_passengers()
            
            
            
            
            
                  
                    

                    
            
            
    


# 2 A1 A2
# 1 A1 3 Raja Mohan Phalguni
# 1 A2 3 Sunder Rashmi Srikant 
# 3 A1
# 2 A1 1 Phalguni
# 1 A2 1 Mohit
# 4 A2
# 2 A1 1 Raja
# 3 A1