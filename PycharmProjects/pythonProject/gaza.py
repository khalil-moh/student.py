name ="khalil moh ismail"
farst_name_index= name.find(" ")
farst_name=name[0:farst_name_index]
print(farst_name)
second_name_index=name.find(" ",farst_name_index +1)
second_name=name[farst_name_index+1:second_name_index]
print(second_name)
third_name=name[second_name_index+1: ]
print(third_name)
