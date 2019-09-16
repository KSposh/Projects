"""
Web based financial graph
Stock analysis

Integrated into website in /site
"""
from datetime import datetime
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

hours_12 = 12*60*60*1000

start_date = datetime(2015, 11, 1)
end_date = datetime(2016, 3, 10)


df = data.DataReader(name="GOOG", data_source="yahoo",
                     start=start_date, end=end_date)

date_increase = df.index[df.Close > df.Open]
date_decrease = df.index[df.Close < df.Open]


def inc_dec(c, o):
    if c > o:
        return "Increase"
    elif c < o:
        return "Decrease"
    else:
        return "Equal"


df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Open - df.Close)

f = figure(x_axis_type='datetime', title="Candlestick", width=1000, height=300, sizing_mode="scale_width")
f.grid.grid_line_alpha = 0.3

f.segment(df.index, df.High, df.index, df.Low, color="Black")
f.rect(x=df.index[df.Status == "Increase"], y=df.Middle[df.Status == "Increase"], width=hours_12,
       height=df.Height[df.Status == "Increase"], fill_color="green", line_color="black")

f.rect(x=df.index[df.Status == "Decrease"], y=df.Middle[df.Status == "Decrease"], width=hours_12,
       height=df.Height[df.Status == "Decrease"], fill_color="red", line_color="black")

script1, div1 = components(f)
cdn_js = CDN.js_files
cdn_css = CDN.css_files



# output_file("Stock.html")
# show(f)
