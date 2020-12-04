from pyecharts.charts import Line
from pyecharts import options

# 准备数据
cuntry = ['美国', '巴西', '印度', '俄罗斯']
data1 = [10000000, 600000, 5000000, 300000]

# 实例化图表对象

line = Line()

# 关联数据
line.add_xaxis(cuntry)
line.add_yaxis(series_name='感染人数', y_axis=data1, is_smooth=True)
# is_smooth=True曲线
# 配置
# 全局设置
line.set_global_opts(
    title_opts=options.TitleOpts(title='世界严重感染国家'),
    toolbox_opts=options.ToolboxOpts()
)
# 系列设置
line.set_series_opts(
    markline_opts=options.MarkLineOpts(
        data=[
            options.MarkLineItem(name='平均值', type_='average'),
        ]
    )
)

line.render('templates/折线图.html')
