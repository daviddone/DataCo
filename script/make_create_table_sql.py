import re
reg = re.compile(re.escape('datetime'), re.IGNORECASE)
f = open("广西价值tps_base.txt",encoding="utf-8")
################# 分割线 ########################
#f = open("广西价值tps_e_g_u_week.txt",encoding="utf-8")
#f = open("广西价值tps_e_week.txt",encoding="utf-8")
#f = open("广西价值tps_g_week.txt",encoding="utf-8")
#f = open("广西价值tps_pp_week.txt",encoding="utf-8")
#f = open("广西价值tps_r_week.txt",encoding="utf-8")
#f = open("广西价值tps_score_e_week.txt",encoding="utf-8")
#f = open("广西价值tps_score_g_week.txt",encoding="utf-8")
table_name = "tps_base"
f2 = open(table_name+".txt","w",encoding="utf-8")
count = 0
f2.writelines("create external table IF NOT EXISTS %s ("%table_name+"\n")
#f2.writelines("create table IF NOT EXISTS %s ("%table_name+"\n")
for item in f:
	newline = item
	item_one = item.split("\t")[0].replace(" ","").strip().lower()
	newline = item_one+ "  " + item.split("\t")[1].strip()
	newline = newline.replace("varchar","string")
	newline = newline.replace("Varchar","string")
	newline = newline.replace("VARCHAR","string")
	newline = newline.replace("(50)","")
	newline = newline.replace("(255)","")
	newline = newline.replace("(64)","")
	newline = newline.replace("(128)","")
	newline = newline.replace("smallint","int")
	newline = newline.replace("integer","bigint")
	newline = newline.replace("Integer","bigint")
	newline = newline.replace("int8","bigint")
	newline = newline.replace("datetime","string")
	newline = newline.replace("DATETIME","string")
	newline = reg.sub('string', newline)
	newline = newline.lower()
	count = count + 1
	print(count)
	print(newline)
	f_line = newline +","
	f2.writelines(f_line+"\n")
f2.writelines(") partitioned by (datepart bigint) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\|' STORED AS TEXTFILE LOCATION '${ParseInput}/base';"+"\n")
#f2.writelines(")partitioned by (datepart bigint) row format delimited fields terminated by '\|';"+"\n")
f2.close()