from pyecharts.charts import Pie
from pyecharts import options

data = [('小米', 200), ('华为', 300), ('oppo', 250), ('vivo', 400), ('1+', 100)]

# 创建图表对象
pie = Pie()

# 将数据渲染到图表上
pie.add(
    # 数据显示
    data_pair=data,
    # 名称显示
    series_name='国产手机销量',
    # 空心部分和数据显示部分的比例
    radius=[30,200],
    rosetype='radius',
    center=[300,300]

)

# 全局设置设置
pie.set_global_opts(
    title_opts=options.TitleOpts(title='国产手机销量')
)

pie.set_series_opts(
    label_opts=options.LabelOpts(formatter='{b}:{d}%')
)

# 显示图表

pie.render('templates/饼图.html')
