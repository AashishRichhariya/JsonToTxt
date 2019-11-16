import json

filePath = "/home/aashishrich/OwnFiles/Learnings/UWM/MWN/Project/Implementation/Dataset/bdd100k_labels_release/bdd100k/labels/bdd100k_labels_images_val.json"

'''
car: 0
bus: 1
train: 2
traffic light: 3


image_index image_absolute_path img_width img_height box_1 box_2 ... box_n
label_index x_min y_min x_max y_max
'''
d = {}
d["car"] = 0
d["bus"] = 1
d["train"] = 2
d["traffic sign"] = 3

lines = []

with open(filePath) as jsonFile:
    data = json.load(jsonFile)    
    for i in range (len(data)):
        s = ""
        s = str(i) + " " + data[i]["name"] + " " + "1920" + " " + "1080" + " " 
        for l in data[i]["labels"]:    
            if(l["category"] == "car" or l["category"] == "bus" or l["category"] == "train" or l["category"] == "traffic sign"):
                s = s + str(d[l["category"]]) + " "
                x1 = int(float(l["box2d"]["x1"]))
                y1 = int(float(l["box2d"]["y1"]))
                x2 = int(float(l["box2d"]["x2"]))                
                y2 = int(float(l["box2d"]["y2"]))
                s = s + str(x1) + " "
                s = s + str(y1) + " "
                s = s + str(x2) + " "
                s = s + str(y2) + " "
        lines.append(s)

f = open("data.txt", "w")
#for l in lines:
f.writelines(lines)
f.close()