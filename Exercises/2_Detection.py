from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

# Object Detection result
result = model('../Assets/DogVid.mp4', save = True, project = "../Results/")