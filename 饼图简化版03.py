from pyecharts.charts import Pie
from pyecharts import options

pie=(
    Pie()
    .add(
        series_name='国产手机',
        data_pair=[('小米', 200), ('华为', 300), ('oppo', 250), ('vivo', 400), ('1+', 100)],
        rosetype='radius',
        radius=['1%','90%']
    )
    .set_global_opts(title_opts=options.TitleOpts('国产手机销量'))
    .set_series_opts(
        label_opts=options.LabelOpts(formatter='{b}:{d}%')
    )
)

pie.render('templates/饼图2.html')