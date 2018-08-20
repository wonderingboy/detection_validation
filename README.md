使用方法:
1.数据准备:
  a. ground truth 为xml文件,每张图片对应一个xml文件,标注格式与VOC标注一致
  b. 检测结果为txt文件,每张图片对应一个txt文件,文件名与对应的图片名一致,文件内容为一个json字符串,格式如下所示:
     {"objs":[{"classid":"Battery","xmin":271,"ymin":234,"xmax":433,"ymax":447},{"classid":"gun","xmin":62,"ymin":172,"xmax":408,"ymax":424}]}
  c. 将对应的ground truth xml文件 和 检测结果对应的txt文件放到两个不同的文件夹下,目录结构如下所示:
    --xmls
        ----1.xml
        ----2.xml
        .....
    --txts
        ----1.txt
        ----2.txt
        ........
 
2.调用方式:
    输出的classid为类型名时:
    python evaluate.py xmls/ json/  ''  
    输出的classid 为整数标签时:
    python evaluate.py xmls/ json/  index2label.txt
    
index2label.txt为标签到文件名的映射文件,内容如下所示:
    1 gun
    2 knife
    3 phone
    4 container
    5 fireworks
    6 battery

