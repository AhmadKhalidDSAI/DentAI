from roboflow import Roboflow
rf = Roboflow(api_key="sSKdFrE92GKY074z8aTo")
project = rf.workspace("ahmad-alali").project("teeth-numbering-dataset-vyqoj")
version = project.version(1)
dataset = version.download("yolov11")
                
print("تم التنزيل بنجاح!")                