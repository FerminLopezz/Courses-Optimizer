import pandas as pd
import numpy as np
from classes import Course

temporal_depths = []
courses_list = []
pending = True

def plan_charging ():
    plan = pd.read_csv('Plan_act_admin.csv', names = ["Id","Name", "VH", "Correlatives"])
    
    # Formatting the id
    plan['Id'] = plan['Id'].astype(str)
    # Formatting the Correlatives serie for better manipulation.
    plan['Correlatives'] = plan['Correlatives'].str.split('-', expand = False)
    
    print('The plan has been formatted successfully')

    return plan

def course_charging (plan):
    
    for i in range(len(plan)):
        row = plan.loc[i]

        new_course = Course(
            Id= row['Id'],
            name= row['Name'],
            VH= row['VH'],
            correlatives= row['Correlatives']
        )
        
        courses_list.append(new_course)

    print('The courses has been charged successfully')

def find_course_index(Id):
    for i in range(len(courses_list)):
        if courses_list[i].Id == Id:
            return i

def up_1(courses_list, Id):
    for i in range(len(courses_list)):
        for n in courses_list[i].correlatives:
            if n == Id:             
                temporal_depths[len(temporal_depths)-1].append(courses_list[i].depth)
                             
def up_2 (courses_list):
    for i in range(len(courses_list)):
        temporal_depths.append([courses_list[i].Id])        
        up_1(courses_list, courses_list[i].Id)
        
def up_3(temporal_depths):
    for i in temporal_depths:
        index = find_course_index(i[0])
        depths = i[1:8]
        
        if len(depths) == 0:
            pass
        else:
            courses_list[index].depth = (max(depths) + 1)

def update_depths():
    counter = 0

    while counter < 10:
        up_2(courses_list)    
        up_3(temporal_depths)
        counter += 1

    print('The depths has been updated succesfully.')
#---------------------------------------------
def eligibility_check():
    for i in range(len(courses_list)):
        if len(courses_list[i].correlatives2) == 0:
            courses_list[i].eligibility = True
        else:
            courses_list[i].eligibility = False

def remove_correlatives(id_list):
    for i in id_list:
        for n in range(len(courses_list)):
            if i in courses_list[n].correlatives2:
                courses_list[n].correlatives2.remove(i)
    
def update_eligibility(selected_courses):
    id_list = []
    for i in selected_courses:
        id_list.append(i[0])
    
    remove_correlatives(id_list)
    eligibility_check()

def match(eligible_courses_list, max_depth, os, n_courses):
    for i in eligible_courses_list:
        if i[1] == max_depth and len(os)< n_courses:
            os.append(i)
            
    return os

def top_n(eligible_courses_list, n_courses):   
    max_depth = 0
    os = []
    for i in eligible_courses_list:
         if i[1] > max_depth:
                max_depth = i[1]
    
    limit = 0
    
    while len(os) < n_courses and limit < 10:
        match(eligible_courses_list, max_depth, os, n_courses)
        limit +=1
        max_depth -= 1
    
    return os
    
def selection(n_courses):
    eligible_courses_list = []
    
    for i in range(len(courses_list)):
        if courses_list[i].eligibility == True and courses_list[i].assigned == False:
            eligible_courses_list.append([courses_list[i].Id, courses_list[i].depth])            
    
    selected_courses = top_n(eligible_courses_list, n_courses)
        
    for i in selected_courses:
        temp_index = 0
        temp_index = find_course_index(i[0])          
        courses_list[temp_index].assigned = True
        print( courses_list[temp_index].name, 'Carga Horaria:', courses_list[temp_index].VH)

    update_eligibility(selected_courses)

def selection_2(pending, n_courses):
    
    for i in range(100):
        if pending == True:
            print('Iteración:', i+1)
            selection(n_courses)
            pending = check_pending_courses(pending)
            print('------------------\n')
        else:
            break
        
def check_pending_courses(pending):
    pending = False
    for i in courses_list:
        if i.assigned == False:
            pending = True
    return pending

def main(n_courses, cbc_exception = True):
    plan = plan_charging()
    course_charging(plan)
    update_depths()

    if cbc_exception == True:
        print('\n')
        print('CBC Exception')
    
        for i in range(0,6):
            courses_list[i].assigned = True
            print(courses_list[i].name, i)
    
        cbc_exception = [['241', 0], ['242', 0], ['243', 0], ['244', 0], ['245', 0], ['246',0]]
        update_eligibility(cbc_exception)

        print('\n')
        print('Ferpes Exception')
        
        lista = [['250',0],['247',0],['248',0],['249',0],['251',0],['252',0],['273',0],['274',0],['276',0],['284',0]]

        for i in lista:
            index = find_course_index(i[0])
            courses_list[index].assigned = True
            print(courses_list[index].name)
        
        update_eligibility(lista)
        print('-----------------------------------------------------------------------')

    selection_2(pending, n_courses)


if __name__ == "__main__":
    os = input('Que cantidad de materias vas a cursar?: ')
    main(n_courses=int(os))

    


    
