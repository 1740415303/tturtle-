from pyecharts.charts import Bar
from pyecharts import options

province = ['湖北', '北京', '新疆', '山东', '安徽', '云南', '上海']
data = [100000, 50000, 55000, 51000, 60000, 43210, 50334]
data2 = [12000, 5000, 3000, 5400, 2000, 3000, 10000]

# 创建图表对象
bar = Bar()

# 将数据渲染到表格上
bar.add_xaxis(province)
bar.add_yaxis('确诊人数', data)
bar.add_yaxis('死亡人数', data2)

# 设置图表
bar.set_global_opts(
    # 标题和副标题
    title_opts=options.TitleOpts(title='全国重点城市疫情统计', subtitle='确诊人数和死亡人数')
    , toolbox_opts=options.ToolboxOpts()  # 显示工具栏
)

# 系列设置
bar.set_series_opts(
    # 是否显示数值
    label_opts=options.LabelOpts(is_show=False),
    # 添加标记点
    markpoint_opts=options.MarkPointOpts(
        data=[
            options.MarkPointItem(type_='min', name='最小值'),
            options.MarkPointItem(type_='max', name='最大值')
        ]
    )
)

# 生成图表
bar.render('templates/柱状图.html')
