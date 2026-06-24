# ระบบล็อกอินอย่างง่าย

print("=== ระบบล็อกอิน ===")

username = input("Username: ")
password = input("Password: ")

if username == "jirasak" and password == "12123":
    print("เข้าสู่ระบบสำเร็จ")
    print(f"ยินดีต้อนรับ {username}")
else:
    print("Username หรือ Password ไม่ถูกต้อง")
