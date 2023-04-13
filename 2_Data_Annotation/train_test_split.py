'''
A modified version of ModifiedOpenLabelling Tool by Ivan Goncharov. 
Modifications include training path and splitting folder structure.
'''
import os
import random
import shutil

imgList = os.listdir('images')


#shuffling images
random.shuffle(imgList)

split = 0.2

path = "../data"
train_path_images = path + '/images/train'
train_path_labels = path + '/labels/train'
val_path_images = path + '/images/val'
val_path_labels = path + '/labels/val'


if os.path.isdir(train_path_images) == False:
    os.makedirs(train_path_images)
if os.path.isdir(train_path_labels) == False:
    os.makedirs(train_path_labels)
if os.path.isdir(val_path_images) == False:
    os.makedirs(val_path_images)
if os.path.isdir(val_path_labels) == False:
    os.makedirs(val_path_labels)

imgLen = len(imgList)
print("Images in total: ", imgLen)

train_images = imgList[: int(imgLen - (imgLen*split))]
val_images = imgList[int(imgLen - (imgLen*split)):]
print("Training images: ", len(train_images))
print("Validation images: ", len(val_images))

for imgName in train_images:
    og_path = os.path.join('images', imgName)
    target_path = os.path.join(train_path_images, imgName)

    shutil.copyfile(og_path, target_path)

    og_txt_path = os.path.join('bbox_txt', imgName.replace('.jpg', '.txt'))
    target_txt_path = os.path.join(train_path_labels, imgName.replace('.jpg', '.txt'))

    shutil.copyfile(og_txt_path, target_txt_path)

for imgName in val_images:
    og_path = os.path.join('images', imgName)
    target_path = os.path.join(val_path_images, imgName)

    shutil.copyfile(og_path, target_path)

    og_txt_path = os.path.join('bbox_txt', imgName.replace('.jpg', '.txt'))
    target_txt_path = os.path.join(val_path_labels, imgName.replace('.jpg', '.txt'))

    shutil.copyfile(og_txt_path, target_txt_path)


print("Done! ")
