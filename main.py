import json, csv

# Opening files
f = open("bounding_boxes.labels", "w")
j = open("csvjson.json")
data = json.load(j)

# Writing format stuffs
f.write("{ \n")
f.write('   "version": 1,\n')
f.write('   "type": "bounding-box-labels",\n')
f.write('   "boundingBoxes": {\n')
for k in data['img']:
    for key in k:
        if (key == 'image'):
            image = k[key]
            f.write('       "'+image+'": [{\n')
            f.write('           "label": "car",\n')
        if(key == 'xmin'):
            x = int(k[key])
            f.write('           "x": '+str(x)+',\n')
        if(key == 'ymin'):
            y = int(k[key])
            f.write('           "y": '+str(y)+',\n')
        if(key == 'xmax'):
            width = int(k[key]) - int(x)
            f.write('           "width": '+str(width)+',\n')
        if(key == 'ymax'):
            height = int(k[key]) - int(y)
            f.write('           "height": '+str(height)+'\n         }],\n')

f.write("   }\n")
f.write("}")

f.close()

#open and read the file after the appending:
f = open("bounding_boxes.labels", "r")
print(f.read())
f.close()