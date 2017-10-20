import os
from os.path import join
import time

src_path = r"D:\david_work\亿阳工作\技术知识\10月 调测mro的小工具\lte"
dest_path = r"D:\david_work\亿阳工作\技术知识\10月 调测mro的小工具\lte_day_hive"
f3 = open("hive_wangyou.sh","w",encoding="utf-8")
f3.writelines("seq_id=$1"+"\n")
f3.writelines("echo ${seq_id}"+"\n")
start_time = time.time()
for root, dirs, files in os.walk( src_path ):
    for each_file_name in files :
        #print(each_file_name)
        if each_file_name.find(".q") != -1 and each_file_name.find("tpl") != -1:
            if each_file_name.find("basetable") == -1 and each_file_name.find("grid_ue") ==-1:
                sh_line = "hive -hiveconf seq_id=${seq_id} -f  upload/schedule/lte_day_hive/"
                f3.writelines(sh_line+each_file_name+" ;"+"\n")
            each_full_file_name = join( root, each_file_name )
            print(each_full_file_name)
            f2 = open(dest_path+"/"+each_file_name,"w",encoding= 'utf-8')
            for line in open( each_full_file_name,encoding= 'utf-8'):
                if line.find("${seq_id}")!=-1:
                    line = line.replace("${seq_id}","${hiveconf:seq_id}")
                f2.writelines(line)
            f2.close()
f3.close()
end_time = time.time()
print(end_time-start_time)   