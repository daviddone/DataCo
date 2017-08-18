from lxml import etree

html = '''
<div style="display: block;">
                <ul class="lesson-lists">
                    
                    <li><a href="/course/458-7430/" target="_blank" class="font14 color66"><span class="fl">1.scrapy是什么</span><span class="fr color99">08:31</span></a></li>
                    
                    <li><a href="/course/458-7431/" target="_blank" class="font14 color66"><span class="fl">2.初步使用scrapy</span><span class="fr color99">15:27</span></a></li>
                    
                    <li><a href="/course/458-7432/" target="_blank" class="font14 color66"><span class="fl">3.scrapy的基本使用步骤</span><span class="fr color99">13:55</span></a></li>
                    
                    <li><a href="/course/458-7433/" target="_blank" class="font14 color66"><span class="fl">4.基本概念介绍1-scrapy命令行工具</span><span class="fr color99">13:16</span></a></li>
                    
                    <li><a href="/course/458-7901/" target="_blank" class="font14 color66"><span class="fl">5.基本概念介绍2-scrapy的重要组件</span><span class="fr color99">15:40</span></a></li>
                    
                    <li><a href="/course/458-7902/" target="_blank" class="font14 color66"><span class="fl">6.基本概念介绍3-scrapy中的重要对象</span><span class="fr color99">11:09</span></a></li>
                    
                    <li><a href="/course/458-7903/" target="_blank" class="font14 color66"><span class="fl">7.scrapy内置服务介绍</span><span class="fr color99">11:54</span></a></li>
                    
                    <li><a href="/course/458-7904/" target="_blank" class="font14 color66"><span class="fl">8.抓取进阶-对“西刺”网站的抓取</span><span class="fr color99">09:47</span></a></li>
                    
                    <li><a href="/course/458-7905/" target="_blank" class="font14 color66"><span class="fl">9.“西刺”网站爬虫的核心代码解读</span><span class="fr color99">14:48</span></a></li>
                    
                    <li><a href="/course/458-8059/" target="_blank" class="font14 color66"><span class="fl">10.Scrapy框架解读—深入理解爬虫原理</span><span class="fr color99">13:24</span></a></li>
                    
                    <li><a href="/course/458-8060/" target="_blank" class="font14 color66"><span class="fl">11.实用技巧1—多级页面的抓取技巧</span><span class="fr color99">12:28</span></a></li>
                    
                    <li><a href="/course/458-8061/" target="_blank" class="font14 color66"><span class="fl">12.实用技巧2—图片的抓取</span><span class="fr color99">10:54</span></a></li>
                    
                    <li><a href="/course/458-8139/" target="_blank" class="font14 color66"><span class="fl">13.抓取过程中的常见问题1—代理ip的使用</span><span class="fr color99">09:56</span></a></li>
                    
                    <li><a href="/course/458-8140/" target="_blank" class="font14 color66"><span class="fl">14.抓取过程中的常见问题2—cookie的处理</span><span class="fr color99">09:02</span></a></li>
                    
                    <li><a href="/course/458-8230/" target="_blank" class="font14 color66"><span class="fl">15.抓取过程中的常见问题3—js的处理技巧</span><span class="fr color99">18:22</span></a></li>
                    
                    <li><a href="/course/458-8231/" target="_blank" class="font14 color66"><span class="fl">16.scrapy的部署工具介绍-scrapyd</span><span class="fr color99">05:15</span></a></li>
                    
                    <li><a href="/course/458-8247/" target="_blank" class="font14 color66"><span class="fl">17.部署scrapy到scrapyd</span><span class="fr color99">12:39</span></a></li>
                    
                    <li><a href="/course/458-8248/" target="_blank" class="font14 color66"><span class="fl">18.Scrapy课程总结</span><span class="fr color99">07:48</span></a></li>
                    
                </ul>
	</div>
'''

#print(html)
selector = etree.HTML(html)
title_list = selector.xpath('//span/text()')
time_list = selector.xpath('//span[@class="fr color99"]/text()')   # //代表所有的节点  /代表根节点
for each in title_list:
    print(each)
for item in time_list:
	print(item)
