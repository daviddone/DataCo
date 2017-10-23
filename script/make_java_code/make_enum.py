f2 = open(r"enum.txt","w",encoding= 'utf-8')
f3 = open(r"bean.txt","w",encoding= 'utf-8')
f2.writelines("package com.boco.wangyou.mdt.entity;\n")
f2.writelines("public enum IndexEsrvcc {\n")
f3.writelines("public class Test {\n")
count = 0
for line in open(r"source.txt",encoding= 'utf-8'):
        lists = line.strip().split(",")
        for item in lists:
            new_item = item.upper() + "("+str(count)+")"+","
            print(item.upper())
            f3.writelines("\t private String "+item.lower().replace(" ","") +";" + "\n")
            count = count + 1
            if count == len(lists):
                new_item  = new_item.replace(",",";")
                print(new_item)
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
}
'''
f2.writelines(common_line)
f3.writelines("}")
