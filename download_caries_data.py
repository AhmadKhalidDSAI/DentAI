from roboflow import Roboflow
rf = Roboflow(api_key="sSKdFrE92GKY074z8aTo")
project = rf.workspace("dentex").project("dentex-3xe7e")
version = project.version(4)
dataset = version.download("yolov11")
                
print("تم التنزيل بنجاح!")                