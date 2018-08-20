# -*- coding: UTF-8 -*-
import sys

import dt_list
import gt_list

ratio_thresh=0.5

def union_ratio(gt_box,dt_box):
    x_order = zip( [ gt_box[0],gt_box[1],dt_box[0],dt_box[1] ],['gt_min','gt_max','dt_min','dt_max'] )
    y_order = zip( [ gt_box[2],gt_box[3],dt_box[2],dt_box[3] ],['gt_min','gt_max','dt_min','dt_max'] )
    x_order.sort()
    y_order.sort()
    ratio=0.0
    if x_order[1][1][-3:]=='min' and x_order[2][1][-3:]=='max' and y_order[1][1][-3:]=='min' and y_order[2][1][-3:]=='max':
        union_area=(x_order[2][0]-x_order[1][0])*(y_order[2][0]-y_order[1][0])
        gt_area=(gt_box[1]-gt_box[0])*(gt_box[3]-gt_box[2])
        ratio=float(union_area)/gt_area
        # print(ratio)
    return ratio>ratio_thresh

def pr(gt_list,dt_list):
    gt=len(gt_list)*[0]
    dt=len(dt_list)*[0]
    for i,gt_item in enumerate(gt_list):
        for j,dt_item in enumerate(dt_list):
            box1=[ gt_item[1], gt_item[2], gt_item[3], gt_item[4] ]
            box2=[ dt_item[1], dt_item[2], dt_item[3], dt_item[4] ]
            if gt_item[0]==dt_item[0] and union_ratio(box1,box2):
                # print('same file name')
                gt[i]=1
                dt[j]=1
    return float( sum(dt) )/len(dt),float( sum(gt) )/len(gt)

def evaluate(ground_truth,detect_result):
    '''
        输入两个字典,一个代表groundTruth,一个代表检测结果,输入格式如下:
        {
        "knife":[[file_name,xmin,xmax,ymin,ymax], [file_name,xmin,xmax,ymin,ymax] ...]
        "gun":  [[file_name,xmin,xmax,ymin,ymax], [file_name,xmin,xmax,ymin,ymax] ...]
        ...
        }
    '''
    for key in ground_truth.keys():
        gt_list=ground_truth[key]
        dt_list=detect_result[key]
        precision,recall=pr(gt_list,dt_list)
        print("precision for "+key +" is: ",precision)
        print("recall for "+key +" is: ",recall)

if __name__=='__main__':    
    groundtruth_dict=gt_list.get_all_groundtruth(sys.argv[1])
    detect_dict=dt_list.get_detect_result(sys.argv[2],sys.argv[3])
    evaluate(groundtruth_dict,detect_dict)