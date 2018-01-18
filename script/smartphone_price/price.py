f= open(r"tps_tac_gx.csv",encoding= 'utf-8')
f2= open(r"tps_tac_gx_price.csv","w",encoding= 'utf-8')
cnt = 1
for item in f:
	fields = item.split(",")
	item = item.strip()
	phone_type=fields[1].upper()
	newline = item
	if  len(fields)==3:
		print(fields[1])
		if phone_type.find("IPAD")>-1 or phone_type.find("IPHONE")>-1 or fields[1].find("MATE")>-1 or fields[1].find("NOTE")>-1:
			newline = item+","+"1"
		else:
			newline = item+","+"0"
	f2.writelines(newline+"\n")

