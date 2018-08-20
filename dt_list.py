
# -*- coding: UTF-8 -*-

import json
import os
import sys

def get_label_dict(file_name):
    if not file_name:
        return {}
    label_dict={}
    f=open(file_name)
    lines=f.readlines()
    for line in lines:
        line=line.strip('\n')
        line=line.split(' ')
        label_dict[ int(line[0]) ]=line[1]
    return label_dict

def parse_string(item,label_file=''):   
    json_obj = json.loads(item)
    objs=json_obj['objs']
    result=[]
    label_dict=get_label_dict(label_file)
    for obj in objs:
        if label_dict:
            result.append( [ label_dict[obj["classid"]],obj["xmin"],obj["xmax"],obj["ymin"],obj["ymax"] ] )
        else:
             result.append( [ obj["classid"],obj["xmin"],obj["xmax"],obj["ymin"],obj["ymax"] ] )
    return result

def generate_dict(all_items):
    keys=set()
    all_items_dict={}
    for item in all_items:
        keys.add(item[0])
    for key in keys:
        all_items_dict[key]=[]
    for item in all_items:
        all_items_dict[item[0]].append( [ item[1],item[2],item[3],item[4],item[5] ] )
    for key in all_items_dict.keys():
        print(key, len(all_items_dict[key]))  
    return all_items_dict

def get_detect_result(path,label_file=''):
    '''
    输入两个参数,第一个参数是检测结果的储存路径,路径下每个检测结果文件的名字与图片名相同,文件里是一个表示检测结果的json字符串
    第二个参数是一个物品类别id到物体名称的映射关系,如:
    1 gun
    2 knife
    3 phone
    4 container
    5 fireworks
    6 battery
    如果输出字符串直接包含物品名称而非物品id则传入空字符串即可
    '''
    path=path.rstrip('/')+'/'
    file_names=os.listdir(path)
    all_objs=[]
    for file_name in file_names:
        f=open(path+file_name)
        line=f.readlines() 
        f.close()
        line=line[0].rstrip('\n')
        if len(line)<5:            
            continue
        result=parse_string(line,label_file)        
        for item in result:
            all_objs.append( [ item[0],file_name[:-4],item[1],item[2],item[3],item[4] ] )
    result_dict=generate_dict(all_objs)
    return result_dict

if __name__=='__main__':
    item_dict=get_detect_result(sys.argv[1],sys.argv[2])
    for key in item_dict.keys():
        print(key, len(item_dict[key]))


