f2 = open(r"enum.txt","w",encoding= 'utf-8')
f3 = open(r"bean.txt","w",encoding= 'utf-8')
# f2.writelines("package com.boco.wangyou.mdt.entity;\n")
# f2.writelines("public enum IndexEsrvcc {\n")
f3.writelines("public class Test {\n")
count = 0
lists = []
for item in open(r"source.txt",encoding= 'utf-8'):
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
for item in lists:
	item = item.upper().replace(" ","")
	line = "value.append(lineColumns[IndexUemrBaseEnum.%s"%item
	newline = line+".getIndex()]).append(ConstantsUtil.VERTICAL_LINE);"
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
f2.writelines("\t"+"MdtRoadBaseWritable outWritable = new MdtRoadBaseWritable();")
for item in lists:
	line = item.upper().replace(" ","")
	newline = "outWritable.setTimestamp(lineColumns[IndexMdtUemrBaseEnum.%s.getIndex()]);"%line
	f2.writelines("\t"+newline + "\n")
f3.writelines("}"