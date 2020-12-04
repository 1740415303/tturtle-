from pyecharts import options
from pyecharts.charts import Map

# 数据准备
data = [('湖北', 68149), ('内蒙古', 333), ('四川', 808), ('上海', 1350), ('陕西', 501),('台湾',12000)]

# 生成图表
map = Map()

# 渲染数据

map.add(series_name='国内主要城市感染人数', data_pair=data)  # maptype='world'修改显示国家

map.set_global_opts(
    title_opts=options.TitleOpts(title='感染人数')  # 右下角标题
    , legend_opts=options.LegendOpts(is_show=True)  # 顶部导航series_name=
    , visualmap_opts=options.VisualMapOpts(
        max_=70000,
        min_=0,
        is_piecewise=True,  # 是否按照自己规定的区间显示
        pieces=[
            {'min': 0, 'max': 100, 'label': '0-100', 'color': 'pink'},
            {'min': 100, 'max': 200, 'label': '100-200', 'color': 'yellow'},
            {'min': 200, 'max': 1000, 'label': '200-1000', 'color': 'blue'},
            {'min': 1000, 'max': 2000, 'label': '1000-2000', 'color': 'orange'},
            {'min': 1000, 'label': '>=2000', 'color': 'red'}
        ]
    )
)

# 生成地图
map.render('templates/地图.html')
