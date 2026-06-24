# Dictionary
phone_book = {}
phone_book = dict()

 #สร้างค่าใน Dictionary
student = { 
    "name" : "Jirasak",
    "age": 28,
    "city" : "Yasothno",
    "Gender" : "Man",
    "tel" : "0931870600"
} 
name_student = student.get("name")

name_student = student.get("name","ไม่มีข้อมูล")

class_room = {
    "room_number" : "R302",
    "capacity" : 30,
    "equipment" : ["Projector", "Whiteboard", "Computer"],
    "teacher" : {
        "name" : "Mr. Sompong eiei",
        "subject" : "programming",
    }       
}


classroom_check = class_room.get("teacher", "ไม่มีข้อมูล")
print(classroom_check)