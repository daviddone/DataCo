f2 = open(r"enum.txt","w",encoding= 'utf-8')
f3 = open(r"bean.txt","w",encoding= 'utf-8')
# f2.writelines("package com.boco.wangyou.mdt.entity;\n")
# f2.writelines("public enum IndexEsrvcc {\n")
f3.writelines("public class Test {\n")
count = 0
lists = []
for item in open(r"广西_base表.txt",encoding= 'utf-8'):
    #print(len(line))
    lists.append(item.strip().replace(" ","").upper())
    print(item+"  000")
print(len(lists))       
for item in lists:
    new_item = item.upper() + "("+str(count)+")"+","
    #print(item.upper())
    print("adf:"+item.upper())
    count = count + 1
    if count == len(lists):
        new_item  = new_item.replace(",",";")
        #print(new_item)
    f2.write("\t"+new_item.replace(" ","")+"\n")

common_line = '''
	private int index;

	IndexEsrvcc(int index) {
		this.index = index;
	}

	public int getIndex() {
		return index;
	}

	public void setIndex(int index) {
		this.index = index;
	}

'''
f2.writelines(common_line)
f2.writelines("#################\n")
for item in lists:
    f2.writelines("\tprivate String "+item.lower().replace(" ","") +";" + "\n")
f2.writelines("#################\n")
f2.writelines("#################\n")
for item in lists:
    f2.writelines("\t"+item.lower().replace(" ","") +"," + "\n")
f2.writelines("#################\n")
f2.writelines("create external table IF NOT EXISTS base ("+"\n")
f2.writelines("create table IF NOT EXISTS base ("+"\n")
for item in lists:
    f2.writelines("\t"+item.lower().replace(" ","") +"  string," + "\n")
f2.writelines(") partitioned by (DAY INT) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\|' STORED AS TEXTFILE LOCATION '${ParseInput}/base';"+"\n")
f2.writelines(")partitioned by (DAY INT) row format delimited fields terminated by '\|';"+"\n")
f2.writelines(") row format delimited fields terminated by '\|';"+"\n")
f2.writelines("#################\n")
for item in lists:
    f2.writelines("\tpublic String "+item.lower().replace(" ","") +";" + "\n")
f2.writelines("#################\n")
for item in lists:
	item = item.upper().replace(" ","")
	line = "value.append(lineColumns[IndexUemrBaseEnum.%s"%item
	newline = line+".getIndex()]).append(ConstantsUtil.VERTICAL_LINE);"
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")
for item in lists:
	item = item.upper().replace(" ","")
	firstbig_line = item[0:1].upper()+item[1:len(item)].lower()
	print("f:"+firstbig_line)
	newline = "value.append(entity.get%s()).append(ConstantsUtil.VERTICAL_LINE);"%firstbig_line
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")

for item in lists:
	item = item.upper().replace(" ","")
	line = "value.append(lineColumns[map.get(\"%s\")])"%item.lower()
	newline = line+".append(ConstantsUtil.COMMA);"
	f2.writelines("\t"+newline + "\n")

f2.writelines("#################\n")
count = 0
for item in lists:
	line = item.lower().replace(" ","")
	newline = line+"=lines[%s];"%count
	count = count + 1
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")
for item in lists:
	line = item.lower().replace(" ","")
	newline = "WritableUtils.writeString(out, this.%s);"%line
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")
for item in lists:
	line = item.lower().replace(" ","")
	newline = "this.%s = WritableUtils.readString(in);"%line
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")
f2.writelines("\t"+"MdtRoadBaseWritable outWritable = new MdtRoadBaseWritable();\n")
for item in lists:
	line = item.upper().replace(" ","")
	firstbig_line = line[0:1].upper()+line[1:len(line)].lower()
	newline = "outWritable.set%s(lineColumns[IndexMdtUemrBaseEnum.%s.getIndex()]);"%(firstbig_line,line)
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")
for item in lists:
	line = item.lower().replace(" ","")
	firstbig_line = line[0:1].upper()+line[1:len(line)].lower()
	newline = "entity.set%s(reduceValue.%s);"%(firstbig_line,line)
	f2.writelines("\t"+newline + "\n")
f2.writelines("#################\n")
count = 0
ncLine = ""
ncLine_vertical = ""
for item in lists:
	line = item.upper().replace(" ","")
	newline = "fileds[%s]"%count
	ncLine = ncLine+newline + '+'
	#ncLine_vertical = ncLine_vertical+'"'+line+':"+'+newline+ '+"|"+'
	ncLine_vertical = ncLine_vertical+newline+ '+","+'
	count = count +1
f2.writelines("\t"+ncLine + "\n")
f2.writelines("\t"+ncLine_vertical + "\n")
f3.writelines("}")
f2.writelines("#################\n")
f2.writelines("\tpublic String getLine(){\n")
f2.writelines("\tStringBuffer line = new StringBuffer();\n")
for item in lists:
	newitem = item.lower().replace(" ","")
	newline = "line.append(%s).append(ConstantsUtil.VERTICAL_LINE);"%(newitem);	
	f2.writelines("\t"+newline + "\n")
f2.writelines("\tline.deleteCharAt(line.length() - 1);\n");
f2.writelines("\treturn line.toString();\n")
f2.writelines("}\n")