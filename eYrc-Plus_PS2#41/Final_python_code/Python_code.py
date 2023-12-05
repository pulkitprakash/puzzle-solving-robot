'''
* Team Id: 		41
* Author List: 		Pulkit Prakash
* Filename: 		python_code
* Theme: 		eYRC-Plus
* Functions: 		No_identify(area, perimeter)
                        cellidentify_D2(cx,cy)
                        play(img)
                        sort_list(a)
                        subset_sum(numbers, target,ln,len_d1, partial=[])
                        rem_comm_elemen(a,b)
                        unique_ele(a)
                        best_poss_case(a)
                        puzzle(D1,D2)
                        rem_comm_elemen_short(a,b)
                        unique_ele_short(a)
                        subset_sum_short(numbers, targ, partial=[])
                        coor_find(ab)
                        cal_dx_dy(ele)
                        shortest_path(path)
                        req_format_serial(out1)
                        req_format_serial1(out1)
* Global Variables:	comb_list, possible_list, ans, plist_all_solns, n_possible_list, numbers_tot, D1, no_pos_list, C_N_D1_x, C_N_D1_y, C_STx, C_STy, STx, STy,
                        ntarget, summn
*
'''




import numpy as np
import cv2
import serial           
import time
comb_list=[[] for i in range(4)]               #global declaration of list containing 4 sublists
possible_list=[[] for i in range(4)]           #global declaration of list containing 4 sublists
ans=[[] for i in range(500)]                   #global declaration of list containing 1000 sublists
######################################
#globals for shortest path
global ntarget
global D1
global n_possible_list
global numbers_tot
global STx
global STy
plist_all_solns=[]
n_possible_list=[]
numbers_tot=[]
D1=[]
no_pos_list=[]
C_N_D1_x=0
C_N_D1_y=0
C_STx=0
C_STy=0
STx=2
STy=0
ntarget=0
summn=0
######################################
'''

* Function Name:	No_identify
* Input:		area ->  integer which stores the area of the contour detected
*			perimeter -> integer which stores the perimeter of the contour detected
* Output:		returns the digit(0-9) whose contour detected 
* Logic:		Digits are the identified by the approximate value identified by us with the help of test-images
*			earlier and then applying the range for those values. 			
* Example Call: No_identify(area,perimeter);
*
'''

def No_identify(area, perimeter):
    (area,perimeter)=int(area),int(perimeter)   
    (area_0,peri_0) =  1650,155                ### 'area_n', 'peri_n'are the area and perimeter of the number - 'n'(btw 0 to 9) displayed in the test_images 
    (area_1,peri_1) =  600,152
    (area_2,peri_2) =  905,225
    (area_3,peri_3) =  887,235
    (area_4,peri_4) =  1111,175
    (area_5,peri_5) =  900,235
    (area_6,peri_6) =  1358,196
    (area_7,peri_7) =  720,194
    (area_8,peri_8) =  1587,175
    (area_9,peri_9) =  1341,198
    z=[]
    z=[(u,v) for u in range(area_0-10, area_0+10) for v in range(peri_0-5, peri_0+5)]  ###(u,v) is a set of two elements in the respective defined ranges for making it equal to the parameters taken 'area' and 'perimeter' in the function.  
    for item in z:
        if item == (area,perimeter):
            return 0

    z=[(u,v) for u in range(area_1-20, area_1+50) for v in range(peri_1-5, peri_1+5)]
    for item in z:
        if item == (area,perimeter):    
            return 1
   
    z=[(u,v) for u in range(area_2-10, area_2+10) for v in range(peri_2-5, peri_2+5)]
    for item in z:
        if item == (area,perimeter):
            return 2
    
    z=[(u,v) for u in range(area_3-5, area_3+5) for v in range(peri_3-5, peri_3+5)]
    for item in z:
        if item == (area,perimeter):
            return 3
    
    z=[(u,v) for u in range(area_4-10, area_4+20) for v in range(peri_4-10, peri_4+10)]
    for item in z:
        if item == (area,perimeter):
            return 4
   
    z=[(u,v) for u in range(area_5-10, area_5+10) for v in range(peri_5-10, peri_5+10)]
    for item in z:
        if item == (area,perimeter):
            return 5
       
    z=[(u,v) for u in range(area_6-10, area_6+10) for v in range(peri_6-10, peri_6+10)]
    for item in z:
        if item == (area,perimeter):
            return 6
        
    z=[(u,v) for u in range(area_7-10, area_7+10) for v in range(peri_7-10, peri_7+10)]
    for item in z:
        if item == (area,perimeter):
            return 7
      
    z=[(u,v) for u in range(area_8-10, area_8+10) for v in range(peri_8-10, peri_8+10)]
    for item in z:
        if item == (area,perimeter):
            return 8
       
    z=[(u,v) for u in range(area_9-10, area_9+10) for v in range(peri_9-10, peri_9+10)]
    for item in z:
        if item == (area,perimeter):
            return 9

'''

* Function Name:	cellidentify_D2
* Input:		cx ->  integer which stores the x-coordinate of the contour detected
*			cy -> integer which stores the x-coordinate of the contour detected
* Output:		returns the cell number(of D2) of the contour detected
* Logic:		Reference coordinates for the top-lefmost point of the grid D2 and cell length are stored in the function
*                       which helps to find the cell number						
* Example Call: cellidentify_D2(cx,cy);
*
'''
def cellidentify_D2(cx,cy):
    start_coor_x=450      ###start_coor_x is the x-coordinate of the top-left point of the 0th cell of grid_2  
    start_coor_y=53       ###start_coor_y is the y-coordinate of the top-left point of the 0th cell of grid_2  
    side_length=107       ### side_length is the length of side of one cell of grid_2
    cell_dist_x=int((cx-start_coor_x)/side_length)    ###How many no of cells far away is the required cell from the 0th cell in x-direction.
    cell_dist_y=int((cy-start_coor_y)/side_length)    ###How many no of cells far away is the required cell from the 0th cell in y-direction. 
    cell_no=4*cell_dist_y + cell_dist_x               ###As getting one column down means moving 4 cells  
    return cell_no        


'''

* Function Name:	play
* Input:		img ->  stores the input image
* Output:		returns the numbers of the grid D1 and D2 with their positions
* Logic:		Mid x-coordinate is used to distinguish the numbers present in the D1 from D2,
*                       contours are detected from lower-right corner, so D1 numbers are stored in opposite sequence
*                       which can be corrected by the reversing the list.
*                       For D2 numbers double digits are combined by the concept if they are in the same cell and then
*                       stored in the seperate list.
* Example Call: play(img);
*
'''
def play(img):
    
    ######
    lower = np.array([0,0,0])
    upper = np.array([10,10,10])
    mask = cv2.inRange(img, lower, upper)
    ret,thresh = cv2.threshold(mask,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    i=0;k=0;y=0      ###'i' for making a loop for contours, 'k' for keeping count of numbers in grid_1, 'y' for keeping count of numbers (as single digits) in grid_2
    No_pos_D1=[];cell_no_D2=[];number_D2=[];No_xcord_D2=[];No_pos_D2=[]    ###'cell_no_D2' for storing cellno where digit is placed, 'number_D2' for storing numbers(as single digit) in grid_D2, 'No-xcord_D2' for storing x-coord of centroid of numbers in grid_D2
    for i in range (len(contours)):
        M = cv2.moments(contours[i])
        if all([int(M['m00'])!= 0, 25<cv2.arcLength(contours[i],True)<1000 , 550<cv2.contourArea(contours[i])<2000]):
            area=cv2.contourArea(contours[i])
            perimeter=cv2.arcLength(contours[i],True)
            cv2.drawContours(img,contours,i,(0,255,0),3)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            if cx < 400:        ### for distinguishing numbers in D1 from D2
                number_D1=No_identify(area,perimeter)
                No_pos_D1.append(number_D1)   ###moving the number 'number_D1' to the list-'No_pos_D1'
                k+=1
            else :
                number_grid2=No_identify(area,perimeter)
                cellnumber_grid2=cellidentify_D2(cx,cy)
                cell_no_D2.append(cellnumber_grid2)    ###moving the cell-number 'cellnumber_grid2' to the list-'cell_no_D2'
                number_D2.append(number_grid2)         ###moving the number 'number_D2' to the list-'number_grid2'
                No_xcord_D2.append(cx)             ###moving the x-coordinate 'cx' to the list-'No_xcord_D2'     
                y+=1
    
    
    ### for making of list- 'No_pos_D2' by seperate lists- 'number_D2' and 'cell_no_D2'
    i=0
    while i<y:
        if i < y-1:   #As for last number 'i+1' is not defined 
            if cell_no_D2[i]==cell_no_D2[i+1]:
                if No_xcord_D2[i]>No_xcord_D2[i+1]:
                    No=10*number_D2[i+1]+number_D2[i]
                else:
                   No=10*number_D2[i]+number_D2[i+1] 
                No_pos_D2.append([cell_no_D2[i],No])
                i+=2
            else:
                No_pos_D2.append([cell_no_D2[i],number_D2[i]])
                i=i+1
            
        else:
            No_pos_D2.append([cell_no_D2[i],number_D2[i]])
            i=i+1 
    No_pos_D1.reverse()
    No_pos_D2.reverse()  
    return No_pos_D1, No_pos_D2
############################################
#TASK_2#
'''

* Function Name:	sort_list
* Input:		list-'a' ->  stores the list to be sorted 
* Output:		returns the sorted list
* Logic:		bubble sort using the length for the sublist
* Example Call: sort_list(comb_list[i]);
*
'''
def sort_list(a):                              
    for i in range (len(a)):
        for j in range (len(a)-1-i):
            if len(a[j])> len(a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]        #replacing the jth element by (j+1)th and (j+1)th element by jth
    return a                                   #returning the sorted list 

'''

* Function Name:	subset_sum
* Input:		list-'numbers' ->  stores the numbers available to find the sum of the target number
*                       target -> stores the number whose sum is to be finded
*                       ln -> stores the sublist no of the "possible_list"
*                       len_D1 -> stores the length of the non-zero numbers in the D1 
*                       list-"partial" -> stores the sum elements for the target no
* Output:		all possible sum combinations
* Logic:		appending one element after the other element in the partial and then checking condition of the sum  
* Example Call: subset_sum(D1noz,D2[(2*i)+1],i,len_d1noz);
*
'''
def subset_sum(numbers, target,ln,len_d1, partial=[]):           
    s = sum(partial)                                            #finding sum of elements of list partial
    if target==0:                                               #if target is zero then add zero to possible_list[ln] 
        possible_list[ln].append([0])
        return possible_list[ln]
    
    if s == target:                                             #if s equal to target then add the partial to possible_list[ln]                                      
        possible_list[ln].append(partial)      

    if s >= target:                                             #if s greater than target then return to previous loop
        return
    
    for i in range(len(numbers)):                               #creating loop for finding appropriate element that will add up forming the required sum
        n = numbers[i]                                          #selecting a no from list of numbers "numbers"
        remaining = numbers[i+1:]                               #storing the remaining numbers 
        subset_sum(remaining, target,ln,len_d1, partial + [n])  #recursively calling the same function subset_sum
        if i==(len_d1-1):
            return possible_list[ln]                            #if end of loop then return the list containing the all possible sum

'''

* Function Name:	rem_comm_elemen
* Input:		list-'a' -> stores the list of numbers to be subtracted from the original list               {subtracted means removing the common elements}
*                       list-'b' -> stores the list of numbers of the original list from which the other list is to subtracted
* Output:		list contaning the uncommon elements
* Logic:		checks common elements in the both list and remove them
* Example Call: rem_comm_elemen(comblist0i,D1c);
*
'''
def rem_comm_elemen(a,b):                                      
    for i in a[:]:
         if i in b:
            b.remove(i)                             #removing the element-i from b
    return b

'''

* Function Name:	unique_ele
* Input:		list-'a' -> stores the list from which the duplicate sub-lists to be removed out
* Output:		list contaning only the unique sublists for sum possibilities
* Logic:		sort all the sub-lists and checks if they are equal, then remove the duplicate
* Example Call: unique_ele(comb_list[i]);
*
'''
def unique_ele(a):         
    for i in a:             
        i.sort()           #sorting the no's in the list a
    b=[]                     #initializing an empty list b
    for i in a:
        if i not in b:
            b.append(i)      #appending only unique elements from a to b
    return b                  #returning the list b

'''

* Function Name:	best_poss_case
* Input:		list-'a' -> stores the list from which the best possible sum case is to be find out for all the numbers of the D2
* Output:		list containing the best possible case
* Logic:		firstly check the total no of operands by summing length of operands of all the numbers if that is equal too then check the max operands for 
*                       a particular number, so case having the least max operands for a particular number gives the best possible case
* Example Call: best_poss_case(ans);
*
'''    
def best_poss_case(a):          
    value=0
    min_summ=100
    i=0
    while i<len(a):             #running loop acc to no of elements in a
        if len(a[i])!=0:        #checking if length of a is not equal to zero
            summ=0
            for j in range(len(a[i])):
                summ=summ+len(a[i][j])
            if summ==min_summ:            #checking if length of operands is equal to the previous length 
                list1=[]
                list2=[]
                for x in range(len(a[value])):
                    list1.append(len(a[value][x]))                   #calculating the max vlaue of length of operands of previous case
                for y in range(len(a[i])):
                    list2.append(len(a[i][y]))                       #calculating the max value of length of operands of current case
                if max(list1)>max(list2):                            #checking which length is greater and determining value according to that                    
                    value=i
            if summ<min_summ:                                       #checking if total length of operands is less than the preveious case 
                min_summ=summ
                value=i
            i=i+1
        else:
            break
    return a[value]                                #returning the best possible case 


'''

* Function Name:	puzzle
* Input:		list-'D1' -> stores the list containing the detected numbers from D1
                        list-'D2' -> stores the list containing the detected numbers from D2
* Output:		list containing the best possible sum case for all the numbers present in D2 combinedly
* Logic:		firstly, find all the possible unique combinations for all the numbers in D2 seperatly
*                       secondly, make groups of all combined possible combinations for all the numbers in the D2 combinedly
*                       thirdly, select the best possible case
* Example Call: puzzle(No_pos_D1,No_pos_D2);
*
''' 
def puzzle(D1,D2):
    
    D1noz=[]               #temp list for storing the non-zero numbers in D1
    D2d=[]              #temp list for storing the positions of the numbers of D2
    for i in range(len(D2)):
        for j in range(2):
            D2d.append(D2[i][j])            #appending the D2 values in the D2d list
    D2=D2d                     #initialising the D2 list with the D2d list
    for i in D1:
        if i!=0:               #checking for non-zero numbers       
            D1noz.append(i)    
    len_d1noz=len(D1noz)
    len_D2=len(D2)
    for i in range(len_D2/2):
        comb_list[i]=subset_sum(D1noz,D2[(2*i)+1],i,len_d1noz)       #call the function to find all possible sum numbers of a given target number
        comb_list[i]=unique_ele(comb_list[i])                        #call the function to find only the unique cases among all the cases
        comb_list[i]=sort_list(comb_list[i])                         #call the function to sort list in order of lowest no of operands to max no of operands
        
    a1=0
    for i in range(len(comb_list[0])):                               #running loop according to the number of elements in comb_list[0]
        D1c=D1[:]                          #making a copy of D1 list
        comblist0i=comb_list[0][i][:]       #making a copy of ith element of list comb_list[0]
        new_list=rem_comm_elemen(comblist0i,D1c)          #initializing new_list by calling function rem_comm_elemen and passing two lists as argument
        if (len_D2/2==1):
            ans[a1].append(comb_list[0][i])          #if only one element in D2 then append ith element of comb_list in ans[a1]
            a1=a1+1
        else:          
            for j in range(len(comb_list[1])):         #running a subloop according to the number of elements in comb_list[1]
                z=0
                for i1 in comb_list[1][j][:]:
                      if (comb_list[1][j].count(i1)<=new_list.count(i1)):     #checking whether the no in comb_list[1][j] is present in the new_list or not
                           z=z+1
                if z==len(comb_list[1][j]):             #if all no's of comb_list[1][j] are present in the new_list or not
                    if (len_D2/2==2):                   #if only 2 no's in D2 then add the possibility
                        ans[a1].append(comb_list[0][i])
                        ans[a1].append(comb_list[1][j])
                        a1=a1+1
                    else:
                        duplist=new_list[:]               #creating a copy of new_list 
                        comblist1j=comb_list[1][j][:]     #creating a copy of comb_list[1][j]
                        duplist1=rem_comm_elemen(comblist1j,duplist)         #initializing duplist1 by calling function  
                        for k in range(len(comb_list[2])):                    #running a subloop according to the number of elements in comb_list[2]
                            y=0
                            for i2 in comb_list[2][k][:]:
                                  if (comb_list[2][k].count(i2)<=duplist1.count(i2)):  #checking whether all elements of comb_list[2][k]are present in dup_list1 or not
                                      y=y+1
                            if y==len(comb_list[2][k]):              #if all no's of comb_list[2][k] are present in the duplist1 or not
                                if (len_D2/2==3):                     #if only 3 no's in D2 then add the possibility
                                    ans[a1].append(comb_list[0][i])
                                    ans[a1].append(comb_list[1][j])
                                    ans[a1].append(comb_list[2][k])
                                    a1=a1+1
                                else:
                                    duplist1cp=duplist1                #making a copy of duplist1
                                    comblist2k=comb_list[2][k][:]        #making a copy of comb_list[2][k]
                                    duplist2=rem_comm_elemen(comblist2k,duplist1cp)        #call function rem_comm_elemen  
                                    for l in range(len(comb_list[3])):             #running a subloop according to the number of elements in comb_list[3] 
                                        x=0 
                                        for i3 in comb_list[3][l][:]:
                                            if (comb_list[3][l].count(i3)<=duplist2.count(i3)):
                                                x=x+1
                                        if x==len(comb_list[3][l]):                  #if all no's of comb_list[3][l] are present in duplist2 or not
                                            ans[a1].append(comb_list[0][i])
                                            ans[a1].append(comb_list[1][j])
                                            ans[a1].append(comb_list[2][k])
                                            ans[a1].append(comb_list[3][l])
                                            a1=a1+1
                                            
    fans=best_poss_case(ans)                          #call function to find the case which is the best                                  
    if len(fans)!=0:                                   #checking if there is a possible solution or not
        for i in range(len(fans)):                   #code for printing the output according to the format given in the document
            a=0
            s=sum(fans[i])
            for j in range(len(fans[i])):
                if j==0:
                    print ''
                    print s,'=',fans[i][j],
                else:
                    print '+',fans[i][j],
    else:
        print 'sorry, no possible combination!'

    return fans

############################################
#################################################
#Here, write the code for shortest path
'''D1 will be used for D1
   sublist fans will be used for numbers_tot
   '''

'''

* Function Name:	rem_comm_elemen_short
* Input:		list-'a' ->stores the list of numbers of the original list from which the other list is to subtracted {subtracted means removing the common elements}             
*                       list-'b' -> stores the list of numbers to be subtracted from the original list  
* Output:		list contaning the uncommon elements
* Logic:		checks the elements that have already been used and removes them
* Example Call: rem_comm_elemen_short(numbers_tot,partial+[n]));
*
'''
def rem_comm_elemen_short(a,b):        
    c=[]                                         #new list(temporary)
    for i in a[:]:
         if a.count(i)>(c.count(i)+b.count(i)):  #checking that whether the no of the current element in the original list is greater than the other list + new list
            c.append(i)                          #if yes, then append the current element in the new list
    return c

'''

* Function Name:	unique_ele_short
* Input:		list-'a' -> stores the list from which the duplicate sub-lists to be removed out
* Output:		list contaning only the unique set of numbers to be travelled in D1
* Logic:		checks only the common traversal path and removes them 
* Example Call: unique_ele_short(n_possible_list);
*
'''
def unique_ele_short(a):              
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b

'''

* Function Name:	subset_sum_short
* Input:		list-'numbers' ->  stores the numbers available to find the sum of the target number
*                       target -> stores the number whose sum is to be finded
*                       list-"partial" -> stores the sum elements for the target no
* Output:		all possible permutations for path traversal for calculated set of sum numbers in D1
* Logic:		appending one element after the other element in the partial from the remaining elements after partial fromation and then checking condition of the sum  
* Example Call: subset_sum_short(ret_fans[xmax],len(ret_fans[xmax]));
*
'''
def subset_sum_short(numbers, targ, partial=[]):
    global ntarget
    ntarget=targ
    s = len(partial)               #initialising 's' with the length of the list partial
    if s == targ: 
        n_possible_list.append(partial)      
    if s >= targ:
        return   
    for i in range(len(numbers)):
        n = numbers[i]
        subset_sum_short(rem_comm_elemen_short(numbers_tot,partial+[n]), targ,partial + [n])          #call function subset_sum_short recursively to find the permutations of the sum numbers
        if i==(targ-1):
            return n_possible_list

'''

* Function Name:	coor_find
* Input:		ab ->  stores the cell no of element in D1
* Output:		NONE
* Logic:		by applying the condition of number of columns and number of rows  
* Example Call: coor_find(ele);
*
'''        
def coor_find(ab):
    global C_N_D1_x                  #accessing the global variable C_N_D1_x 
    global C_N_D1_y                  #accessing the global variable C_N_D1_y
    C_N_D1_x=(ab%3)*2+1
    C_N_D1_y=8-(ab/3)*2-1

'''

* Function Name:	cal_dx_dy
* Input:		ele ->  stores the index no of the number in D1
* Output:		returns the distance to be travelled in x-direction and y-direction
* Logic:		by selecting the appropriate side for the input number, function calculates the dx and dy by subtracting the coordinates of the side from
*                       the current position of the bot.
* Example Call: cal_dx_dy(no_pos_list[0][k]);
*
'''      
def cal_dx_dy(ele):
    global C_STx                        #accessing the global variable C_STx
    global C_STy                        #accessing the global variable C_STy  
    side_x=0                          
    side_y=0
    coor_find(ele)                      #call function to set the coordinates of the current number in respective global variables
    if(C_N_D1_x==C_STx and C_N_D1_y-C_STy==1):              #condition when the next number is just above the current position 
        side_x=C_N_D1_x
        side_y=(C_N_D1_y-1)
    elif(C_N_D1_y==C_STy and C_N_D1_x-C_STx==1):            #condition when the next number is just rightwards the current position 
        side_x=(C_N_D1_x+1)
        side_y=C_N_D1_y        
    elif(C_N_D1_x<=C_STx):                                  #condition when the x-coordinate of the number is less than or equal to the current position x-coor
            if (C_N_D1_y>C_STy):                            ##condition when the y-coordinate of the number is greater than the current position y-coor
                side_x=(C_N_D1_x+1)
                side_y=C_N_D1_y
            else:
                side_x=C_N_D1_x
                side_y=(C_N_D1_y)+1   
    else:
            if (C_N_D1_x<2):                               #condition when the x-coordinate of the number is less than 2(i.e. in first column)
                side_x=(C_N_D1_x+1)
                side_y=C_N_D1_y
            elif(C_N_D1_y<=C_STy):                         #condition when the y-coordinate of the number is less than or equal to the current position y-coor
                side_x=(C_N_D1_x-1)
                side_y=(C_N_D1_y)
            else:
                side_x=C_N_D1_x
                side_y=(C_N_D1_y)-1
    dx=side_x-C_STx                                     #calculating the dx by subtracting the current x-coor from current no side x-coor
    dy=side_y-C_STy                                     #calculating the dy by subtracting the current y-coor from current no side y-coor
    if((dx==0 and dy!=0) or (dy==0 and dx!=0)):         
        if (dx==0 and side_x%2!=0):                     #condition when the next number is just one side above the current position
            dx=2
        elif (dy==0 and side_y%2!=0):                   #condition when the next number is just one side righwards the current position
            dy=2       
    return dx,dy


'''

* Function Name:	shortest_path
* Input:		list''path' ->  stores all the permutations of the sum numbers in D1 for path traversal
* Output:		NONE
* Logic:		find that permutation of the numbers for that the sum of the distance to be travelled in x and y direction are least(thus finding the shortest
*                       path for a particular set of sum numbers of a number in D2)
* Example Call: shortest_path(n_possible_list);
*
'''       
def shortest_path(path):
        global C_STx
        global C_STy
        global summn
        global STx
        global STy
        global D1
        plist=[]
        summ=100
        for var in range(len(path)):
            no_pos_list=[]
            for j in range(len(path[var])):
                numbers_pos=[]
                for i in range(len(D1)):
                       if (path[var][j]== D1[i]):
                              numbers_pos.append(i)
                no_pos_list.append(numbers_pos)                              
            
            for k in range(len(no_pos_list[0])):
                dx_T=0
                dy_T=0
                dup_STx=STx
                dup_STy=STy
                n_comb_list=[]
                ##cal dx,dy for 1st
                C_STx=dup_STx
                C_STy=dup_STy
                n_comb_list.append(no_pos_list[0][k])
                ddx,ddy=cal_dx_dy(no_pos_list[0][k])
                '''print C_N_D1_x, C_N_D1_y, 'in_shor_path'
                print abs(ddx), abs(ddy)'''
                dx_T=dx_T+abs(ddx)
                dy_T=dy_T+abs(ddy)
                dup_STx=dup_STx+ddx
                dup_STy=dup_STy+ddy
                dup_comb_list=n_comb_list
                if(ntarget==1):
                    summn=dx_T+dy_T+abs(6-dup_STx)+abs(4-dup_STy)
                    if(summn<summ):
                        plist=n_comb_list
                        summ=summn
                        
                else:    
                    for p in range(len(no_pos_list[1])):
                        dup_comb_list=n_comb_list[:]
                        '''print'dup_comb_list', dup_comb_list'''
                        if (no_pos_list[1][p] not in dup_comb_list):
                                ##cal dx,dy for 2nd
                                dup1_STx=dup_STx
                                dup1_STy=dup_STy
                                dup_dx_T=dx_T
                                dup_dy_T=dy_T
                                dup_summn=summn
                                '''dup_comb_list=comb_list'''
                                C_STx=dup_STx##one before
                                C_STy=dup_STy##one before
                                dup_comb_list.append(no_pos_list[1][p])
                                ddx,ddy=cal_dx_dy(no_pos_list[1][p])
                                '''print dup_comb_list
                                print C_N_D1_x, C_N_D1_y, 'in_shor_path1'
                                print abs(ddx), abs(ddy)'''
                                dup_dx_T=dup_dx_T+abs(ddx)
                                dup_dy_T=dup_dy_T+abs(ddy)
                                dup1_STx=dup1_STx+ddx
                                dup1_STy=dup1_STy+ddy
                                if(ntarget==2):
                                    dup_summn=dup_dx_T+dup_dy_T+abs(6-dup1_STx)+abs(4-dup1_STy)
                                    #print 'dup_summd:',dup_summn
                                    if(dup_summn<summ):
                                        plist=dup_comb_list
                                        summ=dup_summn
                                        '''print 'plist', plist'''
                                        
                                else:                              
                                        for m in range(len(no_pos_list[2])):
                                            dup1_comb_list=dup_comb_list[:]
                                            if (no_pos_list[2][m] not in dup1_comb_list):
                                                ##cal dx,dy for 3rd
                                                dup2_STx=dup1_STx
                                                dup2_STy=dup1_STy
                                                dup1_dx_T=dup_dx_T
                                                dup1_dy_T=dup_dy_T
                                                dup1_summn=dup_summn
                                                '''dup_comb_list=comb_list'''
                                                C_STx=dup1_STx##one before
                                                C_STy=dup1_STy##one before
                                                dup1_comb_list.append(no_pos_list[2][m])
                                                ddx,ddy=cal_dx_dy(no_pos_list[2][m])                                        
                                                '''print dup1_comb_list
                                                print C_N_D1_x, C_N_D1_y, 'in_shor_path1'
                                                print abs(ddx), abs(ddy)'''
                                                dup1_dx_T=dup1_dx_T+abs(ddx)
                                                dup1_dy_T=dup1_dy_T+abs(ddy)
                                                dup2_STx=dup2_STx+ddx
                                                dup2_STy=dup2_STy+ddy
                                                if(ntarget==3):
                                                    dup1_summn=dup1_dx_T+dup1_dy_T+abs(6-dup2_STx)+abs(4-dup2_STy)
                                                    if(dup1_summn<summ):
                                                        plist=dup1_comb_list
                                                        summ=dup1_summn
                                                        
                                                else:                                      
                                                    for n in range(len(no_pos_list[3])):
                                                        dup2_comb_list=dup1_comb_list[:]
                                                        if (no_pos_list[3][n] not in dup2_comb_list):
                                                            ##cal dx,dy for 4th
                                                            dup3_STx=dup2_STx
                                                            dup3_STy=dup2_STy
                                                            dup2_dx_T=dup1_dx_T
                                                            dup2_dy_T=dup1_dy_T
                                                            dup2_summn=dup1_summn
                                                            '''dup_comb_list=comb_list'''
                                                            C_STx=dup2_STx##one before
                                                            C_STy=dup2_STy##one before
                                                            dup2_comb_list.append(no_pos_list[3][n])
                                                            ddx,ddy=cal_dx_dy(no_pos_list[3][n])                                        
                                                            '''print dup2_comb_list
                                                            print C_N_D1_x, C_N_D1_y, 'in_shor_path1'
                                                            print abs(ddx), abs(ddy)'''
                                                            dup2_dx_T=dup2_dx_T+abs(ddx)
                                                            dup2_dy_T=dup2_dy_T+abs(ddy)
                                                            dup3_STx=dup3_STx+ddx
                                                            dup3_STy=dup3_STy+ddy
                                                            if(ntarget==4):
                                                                dup2_summn=dup2_dx_T+dup2_dy_T+abs(6-dup3_STx)+abs(4-dup3_STy)
                                                                if(dup2_summn<summ):
                                                                    plist=dup2_comb_list
                                                                    summ=dup2_summn

        plist_all_solns.append(plist)                                
        for y in range(len(plist)):
            D1[plist[y]]=-1


'''

* Function Name:	req_format_serial
* Input:		list'out1' ->  stores the elements to be modified according which they have to be transferred through serial communication
* Output:		returns list'a3' which contains letter 'a' after each number of the list and length of whole list in the begining of the list,
*                       for detection of numbers in embedded c code after serial communication    
* Logic:		just appending the letter 'a3' after each index of the input list and length of whole list in the begining
* Example Call: req_format_serial(No_pos_D1);
*
''' 
def req_format_serial(out1):
    a1=[str(i) for i in out1]            #converts all elements to string
    #print a1
    a2=[]
    a3=[]
    for i in range(len(a1)):
        a2.append(a1[i])
        a2.append('a')                         #append 'a' after each element of the list
    len1 = len(a2) 
    a3.append((str)(len1))                     #append length of the list at the beginning
    a3.append('a')
    a3=a3+a2
    return a3

'''

* Function Name:	req_format_serial1
* Input:		list'out1' ->  stores the elements to be modified according which they have to be transferred through serial communication
* Output:		returns list'a2' which contains letter 'a' after each number of the list and length of each sublist before the elements of that subllist
*                       and length of the whole list at the very begining, for detection of numbers in embedded c code after serial communication
* Logic:		just appending the letter 'a3' after each index of the input list and length of sublist before each sublist elements and
*                       length of the whole list at the very begining
* Example Call: req_format_serial1(out1);
*
'''
def req_format_serial1(out1):
    a1=[str(i) for i in out1]               #converts all elements to string
    #print a1
    a2=[]
    a3=[]
    for i in range(len(a1)):
        a2.append(a1[i])
        a2.append('a')                          #append 'a' after each element of the list
    return a2
#################################################

#################################################
'''
* Name:	        Main Program
* Input:		None
* Output:		None
* Logic:		Take one input image
*                       Through image processing find the numbers located in the image with their positions
*                       Find the sum of D2 numbers
*                       Find the shortest path for travelling the sum numbers 
* Example Call:	Called automatically by the Operating System
*
'''

if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('pract_image2.jpg')
    No_pos_D1,No_pos_D2 = play(img)                          #call function to detect numbers
    print 'OUTPUT-1:',No_pos_D1
    print 'OUTPUT-2:',No_pos_D2
    ###############
    out1=[]
    for x in range(len(No_pos_D2)):
        for y in range(len(No_pos_D2[x])):
            out1.append(No_pos_D2[x][y])
    ###############
    ret_fans=puzzle(No_pos_D1,No_pos_D2)           #returned final ans stores the output of the called function puzzle


    ######################################
    output1 = req_format_serial(No_pos_D1)
    for i in range(len(output1)):
        if output1[i]=='0':
                output1[i]='c'
        
    ######################################
    D1=No_pos_D1
    '''return_fans=[[8, 8], [5, 9], [3, 7]]'''
    for xmax in range(len(ret_fans)):              # loop according to the number of elements in D2

        if (xmax>=1):
            STx=6
            STy=4
        numbers_tot=ret_fans[xmax]
        n_possible_list=[]
        n_possible_list=subset_sum_short(ret_fans[xmax],len(ret_fans[xmax]))         #call function to find all the permutations for a given set of sum numbers
        '''print possible_list''' 
        n_possible_list=unique_ele_short(n_possible_list)    #call funcion to find unique permutaions
        '''print possible_list'''
        shortest_path(n_possible_list)                      #call function to find shortest path

    ##################
    #for appending the length of the sublists and total sub-lists in case of sending output-3 through serial communication
    out2_par=[]
    out2=[]                                               
    for x in range(len(plist_all_solns)):
        out2_par.append(2*len(plist_all_solns[x]))
        for y in range(len(plist_all_solns[x])):
            out2_par.append(plist_all_solns[x][y])
    out2.append(len(plist_all_solns))
    out2=out2+out2_par

    ##################
    ##################
    output2 = req_format_serial(out1)             #call function for generating required output for serial communication
    for i in range(len(output2)):
        if output2[i]=='0':
                output2[i]='c'     
    output3 = req_format_serial1(out2)          #call function for generating required output for serial communication
    for i in range(len(output3)):
        if output3[i]=='0':
                output3[i]='c' 
    output3.append('b')
 
    # Serial Communication
    ComPort = serial.Serial('COM5')  # open COM24 
    ComPort.baudrate = 9600 # set Baud rate to 9600
    ComPort.bytesize = 8    # Number of data bits = 8
    ComPort.parity   = 'N'  # No parity
    ComPort.stopbits = 1    # Number of Stop bits = 1
    for i in range(len(output1)):
                         data = bytearray(output1[i])
                         No = ComPort.write(data)
                         time.sleep(.1)
    for i in range(len(output2)):
                         data = bytearray(output2[i])
                         No = ComPort.write(data)
                         time.sleep(.1)
    for i in range(len(output3)):
                         data = bytearray(output3[i])
                         No = ComPort.write(data)
                         time.sleep(.1)
                         
    ComPort.close() 
    ####################
    
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
