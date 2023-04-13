# Wildlife Tracker 🐘
## Custom Wildlife Tracker with YOLOv8, BoTSORT and ByteTrack

### Project Showcase



### Getting Started
Download and Unzip this repository. Navigate to the repository in terminal and type the following:

```Bash
conda create -n yolo_env python==3.8

conda activate yolo_env

conda install pytorch torchvision torchaudio -c pytorch

pip install -U ultralytics wandb

pip install supervision==0.3

pip install selenium
```

These are all the dependencies of the project, navigate to `1_Data_Collection` and start running `data_collection.py`. 

### Project Description 🌌 

The Wildlife Tracker Project is an Object Tracker customized for tracking Wildlife in India. This project is part of a collaborative effort with Weights and Biases to create a beginner friendly introduction to YOLOv8. 

It detects and tracks six classes of animals: 

| Class | Animal|
|------|--------|
|0|Tiger 🐯|
|1|Elephant 🐘| 
|2|Rhinoceros 🦏| 
|3|Bison 🦬| 
|4|Leopard 🐆| 
|5|Lion 🦁|

This project guides you through every step of Object Tracking Pipeline. The pipeline is discuessed briefly:
1. Data Collection: In the Data Collection step, we use Selenium library to Automate WebScraping and saving animal images.
2. Data Annotation: We use ModifiedOpenLabeling (by Ivan Goncharov) to Annotate Images and save it using Custom Train Test Split. 
3. Experiment Tracking with W&B: We upload our dataset as `wandb.Artifact` and visualize our image along with the bounding boxes. Explained in-depth in the blog post (Linked below).
4. Custom Training YOLOv8: We train YOLOv8 with our Scraped Data. We train and log metrics to `wandb`
5. Custom Tracking with YOLOv8: We use the native tracking support provided by `ultralytics` and track with two SOTA tracking algorithms : `BoTSORT` and `ByteTrack`. 

It also has interactive exercises to keep you engaged!

Link to the blog post: Blog post is almost done!

Link to the video: Video will be out soon!

### Credits
The assets in the `Assets` folder are all from this amazing free stock photos website called [Pexels](https://www.pexels.com/). 

Here are image credits (in no particular order):
1. Elephant Grasslands - [Video by P'MA'](https://www.pexels.com/video/a-family-of-elephant-roaming-at-a-grassland-2835528/)
2. Lion - [Photo by Gary Whyte](https://www.pexels.com/photo/pride-of-lions-724626/)
3. Elephants Crossing - [Video by Rihan Bezuidenhout from Pexels](https://www.pexels.com/video/elephants-crossing-a-road-in-a-savanna-12596710/)
4. Bird - [Photo by Philippe Donn](https://www.pexels.com/photo/brown-hummingbird-selective-focus-photography-1133957/)
5. DogVid - [Video by Free Videos](https://www.pexels.com/video/dog-at-the-beach-853936/)
6. Apples - [Photo by Josh Hild](https://www.pexels.com/photo/red-apples-on-wooden-crates-2949140/)

Also, a huge thanks to the following people and resources:
1. Ivan Goncharov - [ModifiedOpenLabeling](https://github.com/ivangrov/ModifiedOpenLabelling)
2. Piotr Skalski and RoboFlow - [Supervision](https://github.com/roboflow/supervision)

**If you are reading this far, consider starring the project to show some love. Reach out if you have any questions.**

My email: mukilan.git@gmail.com 
