from ultralytics import YOLO

model_nano = YOLO("/runs/detect/train/weights/best.pt")
model_medium = YOLO("/runs/detect/train2/weights/best.pt")

result_nano = model_nano("../Assets/Grassland_Elephants.mp4", save = True, project = "../Results/")
result_medium = model_medium("../Assets/Grassland_Elephants.mp4", save = True, project = "../Results/")

result_nano_pic = model_nano("../Assets/Lion.jpg", save = True, project = "../Results/")
result_medium_pic = model_medium("../Assets/Lion.jpg", save = True, project = "../Results/")