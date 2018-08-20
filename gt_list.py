# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import os
import sys

def parse_xml(xml_file_name):
    tree = ET.parse(xml_file_name)
    root = tree.getroot()
    file_name=root.find('filename').text
    file_name=file_name[:-4]
    objs=root.findall('object')
    result=[]
    for obj in objs:
        obj_name=obj.find('name').text
        xmin=int(obj.find('bndbox').find('xmin').text)
        xmax=int(obj.find('bndbox').find('xmax').text)
        ymin=int(obj.find('bndbox').find('ymin').text)
        ymax=int(obj.find('bndbox').find('ymax').text)
        obj_label=[obj_name,file_name,xmin,xmax,ymin,ymax]
        result.append(obj_label)
    return result

        

def get_all_groundtruth(path):
    path=path.rstrip('/')+'/'
    items=os.listdir(path)
    items=[item for item in items if item.endswith('xml') ]
    items.sort()
    all_objs=[]    
    all_keys=set()
    for item in items:
        result=parse_xml(path+item)
        if not result:
            continue
        for item in result:
            all_objs.append(item)
            all_keys.add(item[0])
    obj_dict={}
    for key in all_keys:
        obj_dict[key]=[]
    
    for obj in all_objs:    
        obj_dict[obj[0]].append([obj[1],obj[2],obj[3],obj[4],obj[5]])
    
    for key in obj_dict.keys():
        print(key, len(obj_dict[key]))
    return obj_dict


if __name__=='__main__':
    '''
    从所有的标签文件(xml格式)中解析出groundTruth,输出格式如下:
    {
        "knife":[[file_name,xmin,xmax,ymin,ymax], [file_name,xmin,xmax,ymin,ymax] ...]
        "gun":  [[file_name,xmin,xmax,ymin,ymax], [file_name,xmin,xmax,ymin,ymax] ...]
        ...
        }
    '''
    path=sys.argv[1].rstrip('/')+('/')
    item_dict=get_all_groundtruth(path)
    for key in item_dict.keys():
        print(key, len(item_dict[key]))

