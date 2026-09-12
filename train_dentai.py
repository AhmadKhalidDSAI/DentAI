import os
import torch
from ultralytics import YOLO

def main():
    # 1. التحقق من توفر كرت الشاشة (GPU Acceleration)
    device = '0' if torch.cuda.is_available() else 'cpu'
    print(f"--- Running Training on Device: {device} ---")
    if torch.cuda.is_available():
        print(f"GPU Model: {torch.cuda.get_device_name(0)}")

    # 2. تحديد مسار ملف data.yaml الخاص بالـ Dataset المنزلة من Roboflow
    dataset_yaml = os.path.join("Teeth-Numbering-Dataset-1", "data.yaml")

    if not os.path.exists(dataset_yaml):
        raise FileNotFoundError(f"لم يتم العثور على الملف في المسار: {dataset_yaml}. تأكد من وجود مجلد Teeth-Numbering-Dataset-1")

    # 3. تحميل نموذج YOLO الأساسي (يمكن اختيار yolov8n.pt أو yolo11n.pt)
    model = YOLO("yolo11n.pt")

    # 4. بدء عملية Fine-Tuning
    model.train(
        data=dataset_yaml,
        epochs=50,             # عدد دورات التدريب (يمكن زيادة العدد لاحقاً حسب النتائج)
        imgsz=640,            # حجم الصور المدخلة للنموذج
        batch=16,             # حجم الـ Batch المناسب لـ 8GB VRAM
        device=0,        # تشغيل التدريب على GPU
        workers=4,            # عدد أنوية قراءة البيانات
        project="runs/detect", # المجلد الذي ستحفظ فيه نتائج التدريب والأوزان
        name="dentai_model",  # اسم التجربة
        exist_ok=True         # الكتابة فوق المجلد السابق إذا تكرر التشغيل
    )

    print("--- تم الانتهاء من تدريب النموذج بنجاح! ---")

if __name__ == '__main__':
    # شرط أساسي على نظام Windows لمنع مشاكل الـ Multiprocessing أثناء التدريب
    main()