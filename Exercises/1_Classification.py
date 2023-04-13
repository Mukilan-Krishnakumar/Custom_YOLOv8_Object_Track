from ultralytics import YOLO

# Load the model
model = YOLO('yolov8m-cls.pt')

# Classification result
result = model('../Assets/Bird.jpg', save = True, project = "../Results/")