import os
from os.path import join
import time

src_path = r"./lte"
dest_path = r"./lte_day_hive"

start_time = time.time()
for root, dirs, files in os.walk( src_path ):
    for each_file_name in files :
        #print(each_file_name)
        if each_file_name.find != -1 and each_file_name.find("tpl") != -1:
            each_full_file_name = join( root, each_file_name )
            print(each_full_file_name)
            f2 = open(dest_path+"/"+each_file_name,"w",encoding= 'utf-8')
            for line in open( each_full_file_name,encoding= 'utf-8'):
                if line.find("${seq_id}")!=-1:
                    line = line.replace("${seq_id}","${hiveconf:seq_id}")
                f2.writelines(line)
            f2.close()
end_time = time.time()
print(end_time-start_time)   