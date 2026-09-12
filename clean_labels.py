import os
from pathlib import Path

# بحث عن المجلد اللي بيبدأ بـ Teeth-Numbering
dataset_dir = None
for p in Path(".").iterdir():
    if p.is_dir() and p.name.startswith("Teeth-Numbering"):
        dataset_dir = p
        break

if not dataset_dir:
    print("لم يتم العثور على مجلد البيانات، تأكد من الاسم!")
else:
    print(f"جاري الفحص داخل: {dataset_dir}")
    cleaned_count = 0
    
    for txt_file in dataset_dir.rglob("*.txt"):
        # تجنب ملفات الإعدادات والـ README
        if txt_file.name.startswith("README") or txt_file.name == "data.yaml":
            continue
            
        with open(txt_file, "r") as f:
            lines = f.readlines()
            
        new_lines = []
        modified = False
        
        for line in lines:
            parts = line.strip().split()
            if len(parts) > 5:
                modified = True
                new_lines.append(" ".join(parts[:5]) + "\n")
            else:
                new_lines.append(line if line.endswith("\n") else line + "\n")
                
        if modified:
            with open(txt_file, "w") as f:
                f.writelines(new_lines)
            cleaned_count += 1
            print(f"تم تصحيح: {txt_file.name}")
            
    print(f"\nتم الانتهاء! إجمالي الملفات المعدلة: {cleaned_count}")