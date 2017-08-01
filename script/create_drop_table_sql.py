#f = open("create_table_day.q",encoding="utf-8")
f = open("create_mon_table.q",encoding="utf-8")
f2 = open("test","w",encoding="utf-8")
for item in f:
	if item.find("tpl") != -1 and item.find("create") != -1:
		newline = item.replace("create","drop").replace("if not","if").replace("external","").replace("(","")
		f2.writelines(newline.replace("\n",";\n"))
f2.close()