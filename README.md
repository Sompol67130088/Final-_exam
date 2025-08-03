# Final-_exam
# Final Exam Web App 🧠💻

เว็บสำหรับการส่งงานสอบปลายภาควิชาเทคโนโลยีสารสนเทศ ประกอบด้วยข้อมูลส่วนตัว, งานวิจัย, และระบบจัดการข้อมูลอ้างอิงตามรูปแบบ IEEE

## 👨‍🎓 ข้อมูลนักพัฒนา
- ชื่อ: สมพล ฉิมแสง
- รหัสนักศึกษา: 67130088
- GitHub Repo: [Assignment Repository](https://github.com/Sompol67130088/Final-_exam.git)

---

## 📚 คุณสมบัติของระบบ

- แสดงข้อมูลส่วนตัวของนักศึกษาในหน้า `/about`
- แสดงหัวข้องานวิจัยและรายการอ้างอิงแบบ IEEE ในหน้า `/myresearch`
- เพิ่ม/ลบข้อมูลอ้างอิงจากฐานข้อมูล PostgreSQL ผ่านหน้า `/reference`
- ลิงก์ไปยังไฟล์ PDF ของงานวิจัยได้โดยตรง

---

## 🔧 เทคโนโลยีที่ใช้

| Layer        | Tools & Stack                             |
|--------------|--------------------------------------------|
| Backend      | Flask (Python)                             |
| Database     | PostgreSQL ผ่าน psycopg2                   |
| Frontend     | HTML, Bootstrap (optional for styling)     |
| Containerization | Docker, Docker Compose                 |

---

## 🛠 วิธีใช้งาน (สำหรับผู้พัฒนา)

### 1. คลิกหรือโคลนโปรเจกต์จาก GitHub
```bash
git clone https://github.com/Sompol67130088/Final-_exam.git
cd Final-_exam
