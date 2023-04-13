# pip3 install -U wandb
from ultralytics import YOLO
from wandb.integration.yolov8 import add_callbacks as add_wandb_callbacks

model = YOLO("yolov8n.yaml")
add_wandb_callbacks(model, project = "wildlife-yolov8")

results = model.train(data = "../wildlife_dataset.yaml",epochs = 1000, device = 0, save_period = 10)
