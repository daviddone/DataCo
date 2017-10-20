#f = open("create_table.q",encoding="utf-8")
f = open("create_external_table.q",encoding="utf-8")
f2 = open("tdl_select_sql","w",encoding="utf-8")
for item in f:
	if item.find("tdl") != -1 and item.find("create") != -1:
		newline = item.replace("create","select *").replace("if not","from").replace("IF NOT","from").replace("external","").replace("(","").replace("table","").replace("exists","")
		newline = newline.replace("EXISTS","")
	#if item.find("tpl") != -1 and item.find("create") != -1:
		#newline = item.replace("create","drop").replace("IF NOT","if").replace("external","").replace("(","")
		#newline = newline.replace("IF NOT EXISTS"," ")
		f2.writelines(newline.replace("\n"," limit 3;\n"))
f2.close()