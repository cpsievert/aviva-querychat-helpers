import os
import polars as pl
import plotly.express as px
from faicons import icon_svg
from querychat.data import titanic
from querychat.express import QueryChat
from shiny.express import render, ui
from shinywidgets import render_plotly

# Keep tool results details collapsed by default.
# os.environ.setdefault("QUERYCHAT_TOOL_DETAILS", "collapsed")

# Initialize querychat
qc = QueryChat(
    titanic(),
    "titanic",
    client="openai/gpt-4.1",
    tools=["update", "filter", "visualize"],
)

# Place sidebar chat component
qc.sidebar()

# Summary statistics of filtered data.
with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("users")):
        "Passengers"

        @render.text
        def count():
            return str(len(qc.df()))

    with ui.value_box(showcase=icon_svg("heart")):
        "Survival Rate"

        @render.text
        def survival():
            rate = qc.df()["survived"].mean() * 100
            return f"{rate:.1f}%"

    with ui.value_box(showcase=icon_svg("coins")):
        "Avg Fare"

        @render.text
        def fare():
            avg = qc.df()["fare"].mean()
            return f"${avg:.2f}"

# 1st row of filtered data views.
with ui.layout_columns():
    with ui.card():
        with ui.card_header():
            "Data Table"

            @render.text
            def table_title():
                return f" - {qc.title()}" if qc.title() else ""

        @render.data_frame
        def data_table():
            return qc.df()

    with ui.card():
        ui.card_header("Survival by Class")

        @render_plotly
        def survival_by_class():
            summary = qc.df().group_by("pclass").agg(pl.col("survived").mean()).sort("pclass")
            return px.bar(
                summary,
                x="pclass",
                y="survived",
                labels={"pclass": "Class", "survived": "Survival Rate"},
            )

# 2nd row of filtered data views.
with ui.layout_columns():
    with ui.card():
        ui.card_header("Age Distribution")

        @render_plotly
        def age_dist():
            df = qc.df()
            return px.histogram(df, x="age", nbins=30)

    with ui.card():
        ui.card_header("Fare by Class")

        @render_plotly
        def fare_by_class():
            df = qc.df()
            return px.box(df, x="pclass", y="fare", color="survived")


ui.page_opts(
    title="Titanic Survival Analysis",
    fillable=True,
    class_="bslib-page-dashboard",
)
