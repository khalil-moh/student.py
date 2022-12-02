test_1 = "KHALIL ismail"
print(test_1.upper())  # كبيتل لتر
print(test_1.lower())  # اسمول لتر
print(test_1.count("i"))  # عدد القيمة المكررة في الجملة
print(test_1.isspace())  # هل القيمة مسافة فقط
print(test_1.isdigit())  # هل القيمة رقم
print(test_1.endswith("il"))  # هل ينهي بال _____
print(test_1.strip())  # تمس المسافات الزائدة من اول المدخل واخره فقط
print(test_1.replace("i", "k"))  # تبديل القيمة الاولى بالقيمة الثانية
test_2 = test_1.split("i")
print(test_1.isupper())  # هل القيم المدخلة كبيتل لتر
print(test_1.islower())  # هل القيم المدخل سمول
print(test_2[1])
#input1 = input("enter your name")
#input2 = input1[input1.find("s") + 2:].upper()

#print(input2)
f_n="khalil"
l_n="ismail"
fo_n=f_n + " "+l_n
print(fo_n)
