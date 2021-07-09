import matplotlib.figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd


class TrendChart:
    df: pd.DataFrame = None
    columns: list = []

    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.columns = df.columns.values.tolist()

    # -------------------------------------------------------------------------
    def get_canvas(self) -> FigureCanvas:
        fig: matplotlib.figure.Figure = self.gen_chart()
        canvas = FigureCanvas(fig)

        return canvas

    # -------------------------------------------------------------------------
    def gen_chart(self) -> matplotlib.figure.Figure:
        # figsize is used for PowerPoint image
        fig: matplotlib.figure.Figure = plt.figure(dpi=100, figsize=(13.3, 3.5))

        ax: matplotlib.axes._subplots.AxesSubplot = fig.add_subplot(111, title=self.columns[1])
        plt.subplots_adjust(bottom=0.15, left=0.10, right=0.95, top=0.90)

        xlabel: str = self.columns[0]
        ylabel: str = self.columns[1]
        x: pd.Series = self.df[xlabel]
        y: pd.Series = self.df[ylabel]

        # plot
        ax.grid(True)
        ax.plot(x, y, color='darkgray', marker='o', markersize=1)

        # X/Y labels
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        return fig
