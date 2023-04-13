import wandb
import os

PATH_TRAIN_IMAGES = "../data/images/train/"
PATH_TRAIN_LABELS = "../data/labels/train/"
PATH_VAL_IMAGES = "../data/images/val/"
PATH_VAL_LABELS = "../data/labels/val/"

class_labels = {0 : 'indian_tiger', 1 : 'indian_elephant', 2 : 'indian_rhinoceros' , 3 : 'indian_bison', 4 : 'indian_leopard' , 5 : 'asiatic_lion'}

config = {
    "project" : "wildlife-yolov8",
    "num_of_classes" : 6 
}
run = wandb.init(project = config["project"], config = config)

def box_dict_maker(no_of_times, bounding_box):
    box_list = []
    class_num = 0
    for n in range(no_of_times):
        intermediate = {
                    "position": {
                    "middle" : [float(bounding_box[5*n + 1]),float(bounding_box[5*n + 2])],
                    "width" : float(bounding_box[5*n + 3]),
                    "height" : float(bounding_box[5*n +4]),
                    },
                    "class_id" : int(bounding_box[5*n + 0]),
                    "box_caption": class_labels[int(bounding_box[5*n + 0])],
        }
        class_num = int(bounding_box[5*n + 0])
        box_list.append(intermediate)
    return (class_num, box_list)

def bounding_box_fn(file_name):
    box = []
    box_dict = {}
    with open(file_name) as f:
        for w in f.readlines():
            for l in w.split(" "):
                box.append(l)
    no_of_times = int(len(box) / 5)
    class_num, box_list = box_dict_maker(no_of_times, box)
    final_dict = {
        "ground_truth" : {
            "box_data" : box_list,
            "class_labels" : class_labels
        }
    }
    return (class_num, final_dict)

def execute(PATH_IMAGE, PATH_TEXT, NAME):
    NAME_LIST = []
    for x in os.listdir(PATH_TEXT):
        if x.endswith(".txt"):
            NAME_LIST.append(x[:-4])
    tabular_data = []
    count = 0
    for x in NAME_LIST:
        box_path = PATH_TEXT + str(x) + ".txt"
        image_path = PATH_IMAGE + str(x) + ".jpg"
        class_num, final_dict = bounding_box_fn(box_path)
        tabular_data.append([count, wandb.Image(image_path,
        boxes = final_dict), class_labels[class_num]])
        count += 1
    columns = ['index', 'image', 'label']
    test_table = wandb.Table(data = tabular_data, columns = columns)
    run.log({NAME : test_table})
    
execute(PATH_TRAIN_IMAGES, PATH_TRAIN_LABELS, "Test")
execute(PATH_VAL_IMAGES, PATH_VAL_LABELS, "Validation")