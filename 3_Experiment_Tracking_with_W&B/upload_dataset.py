import wandb
import os

config = {
    "project" : "wildlife-yolov8",
    "num_of_classes" : 6 
}
run = wandb.init(project = config["project"], config = config)

artifact = wandb.Artifact(
    name = "yolov8-data",
    type = "dataset"
)

artifact.add_dir("../data/")
wandb.log_artifact(artifact)