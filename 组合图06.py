from pyecharts.charts import Line, Bar, Grid
from pyecharts import options

# 创建需要组合在一起的单独的图表
cate = ['重庆', '黑龙江', '香港', '台湾', '上海']
data = [579, 925, 1035, 427, 640]
data2 = [470, 487, 699, 253, 533]

# 创建对象
bar = Bar()  # 实例化柱状图对象
line = Line()  # 实例化折线图对象

# 画柱状图
bar.add_xaxis(cate)
bar.add_yaxis('确诊人数', data)
bar.add_yaxis('治愈人数', data2)

bar.set_global_opts(
    title_opts=options.TitleOpts(title='疫情信息')
)
# 画折线图
line.add_xaxis(cate)
line.add_yaxis('确诊人数', data)
line.add_yaxis('治愈人数', data2)

# 创建组合对象

grid = Grid(init_opts=options.InitOpts(width='1200px', height='800px'))

# 将柱状图和折线图嵌入

grid.add(bar, grid_opts=options.GridOpts(
    pos_top='50',
    pos_left='60',
    width='550',
    height='300'
))

grid.add(line, grid_opts=options.GridOpts(
    pos_top='50',
    pos_right='0',
    width='550',
    height='300'
))

# 渲染到页面
grid.render('templates/组合.html')
