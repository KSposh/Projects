# Basic bokeh line graph

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
# from bokeh.io import output_file, show
from datetime import datetime as dt
import pandas

def line_plot():
    # Prepare data
    x = [i for i in range(1, 6)]
    y = [i for i in range(6, 11)]

    # Prepare the output file
    output_file("Line.html")
    # Create the figure object
    f = figure()
    # Create the line plot
    f.line(x, y)
    show(f)

def line_plot_csv(i_file, output, x_cor="x", y_cor="y"):
    df = pandas.read_csv(i_file)
    x = df[x_cor]
    y = df[y_cor]

    output_file(output)
    # Create the figure object
    f = figure()
    f.title.text = i_file
    f.xaxis.axis_label = x_cor
    f.yaxis.axis_label = y_cor
    # Create the line plot
    f.line(x, y)
    show(f)


def circle_plt_xlsx(i_file, output, x_cor="x", y_cor="y"):
    df = pandas.read_excel(i_file, sheet_name=0)
    x = df[x_cor] / 10
    y = df[y_cor] / 10

    output_file(output)
    # Create the figure object
    f = figure()
    f.title.text = i_file
    f.xaxis.axis_label = x_cor
    f.yaxis.axis_label = y_cor
    # Create the line plot
    f.circle(x, y, size=0.5)
    show(f)


def time_series_csv(i_file, output, x_cor="x", y_cor="y"):
    df = pandas.read_csv(i_file, parse_dates=["Date"])
    # print(df)
    x = df[x_cor]
    y = df[y_cor]

    output_file(output)
    # Create the figure object
    f = figure(width=500, height=250, x_axis_type="datetime")
    f.title.text = i_file
    f.xaxis.axis_label = x_cor
    f.yaxis.axis_label = y_cor
    # Create the line plot
    f.line(x, y, color="Orange", alpha=0.5)
    show(f)


def motion_csv(i_file, output):
    df = pandas.read_csv(i_file)

    df['Start'] = pandas.to_datetime(df["Start"])
    df['Start_string'] = df['Start'].dt.strftime("%Y-%m-%d %H:%M:%S")
    df['End'] = pandas.to_datetime(df["End"])
    df['End_string'] = df['End'].dt.strftime("%Y-%m-%d %H:%M:%S")

    cds = ColumnDataSource(df)

    f = figure(x_axis_type="datetime", title=i_file, height=100, width=500, sizing_mode="scale_width")

    f.ygrid[0].ticker.desired_num_ticks=1

    hover = HoverTool(
        tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
    f.add_tools(hover)

    f.quad(left="Start", right="End",
           bottom=0, top=1, color="green", source=cds)
    output_file(output)
    show(f)


# line_plot_csv("data.csv", "Line.html")
# line_plot_csv("bachelors.csv", "bachelors.html", x_cor="Year", y_cor="Engineering")
# circle_plt_xlsx("verlegenhuken.xlsx", "Scatter.html", x_cor="Temperature", y_cor="Pressure")
# time_series_csv("adbe.csv", "time_series.html", x_cor="Date", y_cor="Close")
motion_csv("Sample_of_the_produced_time_values.csv", "motion.html")
