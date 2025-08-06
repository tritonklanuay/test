# main.py

from problems import problems
from checker import check_structure, check_output
import csv
import os
from datetime import datetime

def save_result(problem_id, structure_result, output_result):
    filename = "results.csv"
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["เวลา", "ข้อ", "โครงสร้าง", "ผลลัพธ์", "รวม"])
        summary = "ผ่าน" if structure_result[0] and output_result[0] else "ไม่ผ่าน"
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            problem_id,
            structure_result[1],
            output_result[1],
            summary
        ])

def main():
    print("🔍 ระบบตรวจข้อสอบ Python หลายข้อ")

    for pid, pdata in problems.items():
        print(f"\n=== {pid}: {pdata['description']} ===")
        print("ใส่โค้ดของคุณ (จบบรรทัดว่าง):")

        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        student_code = "\n".join(lines)

        structure_result = check_structure(student_code, pdata["required_keywords"])
        print("✅ ตรวจโครงสร้าง:", structure_result[1])

        output_result = check_output(student_code, pdata["testcases"])
        print("⚙️ ตรวจผลลัพธ์:", output_result[1])

        save_result(pid, structure_result, output_result)
        print("📁 บันทึกผลลง results.csv แล้ว")

if __name__ == "__main__":
    main()