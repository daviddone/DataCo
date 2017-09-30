#encoding=utf-8
class Site:
    #define basic
    site_home = ''
    site_url = ''
    site_name = ''
    site_rule = ''
    #define method
    def __init__(self,site_home,site_url,site_name,site_rule):
        self.site_home = site_home
        self.site_url = site_url
        self.site_name = site_name
        self.site_rule = site_rule

def get_sites():
    site_list = []
    f = open("data.txt",encoding="utf-8")
    for item in f:
        if item.startswith("//") > 0:
            continue
        site_home = item.split("##")[0].strip()
        site_url = item.split("##")[1].strip()
        site_name = item.split("##")[2].strip()
        site_rule = item.split("##")[3].strip()
        each_site = Site(site_home,site_url,site_name,site_rule)
        site_list.append(each_site)
    print("all site url size :%s" %len(site_list))
    return site_list