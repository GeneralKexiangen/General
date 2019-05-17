#!D:\Python\python.exe 
# -*- coding:utf-8 -*-
# created by General
from pyecharts import Bar
from pyecharts import Gauge

bar = Bar("贵州GDP柱状图", "副标题")
bar.add("GDP",
        ["贵阳市", "遵义市", "六盘水市", "安顺市", "黔东南州"],
        [40, 30, 26, 22, 15])
bar.show_config()
bar.render("b.html")


gauge = Gauge("仪表盘图形", "副图标")
gauge.add("重大项目", "投资占比", 66.66)
gauge.show_config()
gauge.render("g.html")