# ระบบล็อกอินอย่างง่าย

users = {
    "admin": "1234"
}

print("=== ระบบล็อกอิน ===")

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("เข้าสู่ระบบสำเร็จ")
    print(f"ยินดีต้อนรับ {username}")
else:
    print("Username หรือ Password ไม่ถูกต้อง")