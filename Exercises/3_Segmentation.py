from ultralytics import YOLO

# Load the model
model = YOLO('yolov8m-seg.pt')

# Segmentation result
result = model('../Assets/Apples.jpg', save = True, project = "../Results/")