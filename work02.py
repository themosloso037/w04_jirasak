# SET
music_club = {"Taylor Swift", "BTS", "Adele"}
color = {"Red", "Blue", "Green","orange"}
friut = {"Apple", "Banana", "Mango","orange"}
all_members = music_club | color | friut


#Intersection (&) = หาสมาชิกร่วมกันของ set ทั้งสอง
color_and_friut = color & friut
print("สีและผลไม้ที่ซ้ำกัน:", color_and_friut)

#Difference (-) = หาสมาชิกที่ไม่ซ้ำกันของ set ทั้งสอง
dif_color_not_friut = color - friut
print("สีที่ไม่ซ้ำกับผลไม้:", dif_color_not_friut)

# symmetric difference (^) = อยู่กลุ่มใดกลุ่มหนึ่ง
symmetric_color_friut = color ^ friut
print("สีและผลไม้ที่ไม่ซ้ำกัน:", symmetric_color_friut)

# การตรวจสอบสมาชิกใน set หรือไม่ ?
set_check = {"orange","banana"}
print("orange" in set_check)  # True
print("grape" in set_check)  # False