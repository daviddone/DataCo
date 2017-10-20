f = open("create_table.q",encoding="utf-8")
f2 = open("tpl","w",encoding="utf-8")
for item in f:
	if item.find("tpl") != -1 and item.find("create") != -1:
		newline = item.replace("create","select *").replace("if not","from").replace("IF NOT","from").replace("external","").replace("(","").replace("table","").replace("exists","")
		newline = newline.replace("EXISTS","")
		f2.writelines(newline.replace("\n"," limit 3;\n"))
f2.close()