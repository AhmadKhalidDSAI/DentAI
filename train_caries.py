import os
import torch
from ultralytics import YOLO

def main():
    device = '0' if torch.cuda.is_available() else 'cpu'
    print(f"--- Running Training on Device: {device} ---")
    if torch.cuda.is_available():
        print(f"GPU Model: {torch.cuda.get_device_name(0)}")

    dataset_yaml = os.path.join("dentex-4", "data.yaml")

    if not os.path.exists(dataset_yaml):
        raise FileNotFoundError(f"لم يتم العثور على الملف في المسار: {dataset_yaml}")

    model = YOLO("yolo11n.pt")

    model.train(
        data=dataset_yaml,
        epochs=100,
        imgsz=640,
        batch=16,
        device=0,
        workers=4,
        project="runs/detect",
        name="caries_model",
        exist_ok=True
    )

    print("--- تم الانتهاء من تدريب موديل التسوس بنجاح! ---")

if __name__ == '__main__':
    main()