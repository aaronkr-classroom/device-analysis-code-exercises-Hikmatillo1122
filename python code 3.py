My_list1 = [1,2,'a',"hello"]
My_list2 = [1,'a',3,67]
#index 0 1 2 3
My_list1[1] = 67
My_list2.append(89)

#Tuple
My_t1 = ('arnold', 1984)
My_t23 = (1991, 2003)
print(My_t23[0])#My_t23[0] = 'Aaron'
My_t23 = (100, 1000)

#Dictionary
My_dict = {"name" : "Aaron", "list" : My_list1, "tup" : (1,2,3),}
My_dict['tup'] = (1,4,5)
My_dict['name'] = "Brian"

Set1 = {1,2,'a',"Hello"}
Set2 = {2,3,'b', "Hello"}
Union_Set = Set1 | Set2
Intersection_Set = Set1 |Set2
Diff_Set = Set1 - Set2
Sym_diff_Set = Set1 ^ Set2
print('U:', Union_Set)
print('I:', Intersection_Set)
print('D:', Diff_Set)
print('SD:', Sym_diff_Set)
