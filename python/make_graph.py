import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.ticker as ticker
from dataclasses import dataclass, field
from typing import Optional
from openpyxl.utils import column_index_from_string
from multiprocessing import Process
import scienceplots
import japanize_matplotlib


@dataclass
class Lim:
    min: float
    max: float

    def copy_with(self, min: Optional[float] = None, max: Optional[float] = None):
        return Lim(
            min=min if min is not None else self.min,
            max=max if max is not None else self.max,
        )


@dataclass
class Axis:
    major: Optional[list[float]] = None
    minor: Optional[float] = None
    lim: Optional[Lim] = None

    def copy_with(
        self,
        major: Optional[list[float]] = None,
        minor: Optional[float] = None,
        lim: Optional[Lim] = None,
    ):
        return Axis(
            major=major if major is not None else self.major,
            minor=minor if minor is not None else self.minor,
            lim=lim if lim is not None else self.lim,
        )


@dataclass
class LogAxis:
    major: Optional[list[float]] = None
    minor: Optional[bool] = None
    lim: Optional[Lim] = None

    def copy_with(
        self,
        major: Optional[list[float]] = None,
        minor: Optional[bool] = None,
        lim: Optional[Lim] = None,
    ):
        return LogAxis(
            major=major if major is not None else self.major,
            minor=minor if minor is not None else self.minor,
            lim=lim if lim is not None else self.lim,
        )


@dataclass
class Label:
    xlabel: list[str] = field(default_factory=list)
    y1label: list[str] = field(default_factory=list)
    y2label: list[str] = field(default_factory=list)

    def copy_with(
        self,
        xlabel: Optional[list[str]] = None,
        y1label: Optional[list[str]] = None,
        y2label: Optional[list[str]] = None,
    ):
        return Label(
            xlabel=xlabel if xlabel is not None else self.xlabel,
            y1label=y1label if y1label is not None else self.y1label,
            y2label=y2label if y2label is not None else self.y2label,
        )


@dataclass
class Sheet:
    excel_file: str
    sheet_name: str
    skiprows: Optional[int] = None

    def __post_init__(self):
        self.df_excel = pd.read_excel(
            self.excel_file,
            sheet_name=self.sheet_name,
            skiprows=self.skiprows,
        )


@dataclass
class Marker:
    marker: Optional[str] = None
    markersize: Optional[float] = None
    ls: Optional[str] = None
    color: Optional[str] = None

    def copy_with(
        self,
        marker: Optional[str] = None,
        markersize: Optional[float] = None,
        ls: Optional[str] = None,
        color: Optional[str] = None,
    ):
        return Marker(
            marker=marker if marker is not None else self.marker,
            markersize=markersize if markersize is not None else self.markersize,
            ls=ls if ls is not None else self.ls,
            color=color if color is not None else self.color,
        )


@dataclass
class Data:
    x_col: str
    y_col: str
    legend: bool = True
    marker: Optional[Marker] = None
    label: Optional[str] = None
    sheet: Optional[Sheet] = None

    def __post_init__(self):
        self.x = column_index_from_string(self.x_col) - 1
        self.y = column_index_from_string(self.y_col) - 1

    def copy_with(
        self,
        x_col: Optional[str] = None,
        y_col: Optional[str] = None,
        legend: Optional[bool] = None,
        marker: Optional[Marker] = None,
        label: Optional[str] = None,
        sheet: Optional[Sheet] = None,
    ):
        return Data(
            x_col=x_col if x_col is not None else self.x_col,
            y_col=y_col if y_col is not None else self.y_col,
            legend=legend if legend is not None else self.legend,
            marker=marker if marker is not None else self.marker,
            label=label if label is not None else self.label,
            sheet=sheet if sheet is not None else self.sheet,
        )

    def set_sheet(self, sheet: Optional[Sheet] = None):
        self.sheet = self.sheet or sheet

    def set_data(self):
        if self.sheet is not None:
            self.x_data = self.sheet.df_excel[self.sheet.df_excel.columns[self.x]]
            self.y_data = self.sheet.df_excel[self.sheet.df_excel.columns[self.y]]
            self.label = r"{0}".format(self.label)
            self.x_label = r"{0}".format(self.sheet.df_excel.columns[self.x])
            self.y_label = r"{0}".format(self.sheet.df_excel.columns[self.y])


@dataclass
class BaseLine:
    value: float
    legend: bool = True
    label: Optional[str] = None
    linestyle: Optional[str] = None
    color: Optional[str] = None
    lim: Optional[Lim] = None

    def copy_with(
        self,
        value: Optional[float] = None,
        legend: Optional[bool] = None,
        label: Optional[str] = None,
        linestyle: Optional[str] = None,
        color: Optional[str] = None,
        lim: Optional[Lim] = None,
    ):
        return BaseLine(
            value=value if value is not None else self.value,
            legend=legend if legend is not None else self.legend,
            label=label if label is not None else self.label,
            linestyle=linestyle if linestyle is not None else self.linestyle,
            color=color if color is not None else self.color,
            lim=lim if lim is not None else self.lim,
        )


@dataclass
class Graph:
    out_file: str
    data: list[Data]
    data2: Optional[list[Data]] = None
    vertical_base_line: Optional[list[BaseLine]] = None
    horizontal_base_line: Optional[list[BaseLine]] = None
    sheet: Optional[Sheet] = None
    marker: Optional[list[Marker]] = None
    x_axis: Optional[Axis | LogAxis] = None
    y1_axis: Optional[Axis | LogAxis] = None
    y2_axis: Optional[Axis | LogAxis] = None
    x_label: list[str] = field(default_factory=list)
    y1_label: list[str] = field(default_factory=list)
    y2_label: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.figure = plt.figure()
        for data in self.data:
            data.set_sheet(self.sheet)
            data.set_data()
        self.ax = self.figure.add_subplot(1, 1, 1)
        self.ax.set_box_aspect(1)
        if self.data2 is not None:
            for data2 in self.data2:
                data2.set_sheet(self.sheet)
                data2.set_data()
            self.ax2 = self.ax.twinx()
            self.ax2.set_box_aspect(1)
        else:
            self.ax2 = None

    def copy_with(
        self,
        out_file: Optional[str] = None,
        data: Optional[list[Data]] = None,
        data2: Optional[list[Data]] = None,
        vertical_base_line: Optional[list[BaseLine]] = None,
        horizontal_base_line: Optional[list[BaseLine]] = None,
        sheet: Optional[Sheet] = None,
        marker: Optional[list[Marker]] = None,
        x_axis: Optional[Axis | LogAxis] = None,
        y1_axis: Optional[Axis | LogAxis] = None,
        y2_axis: Optional[Axis | LogAxis] = None,
        x_label: Optional[list[str]] = None,
        y1_label: Optional[list[str]] = None,
        y2_label: Optional[list[str]] = None,
    ):
        return Graph(
            out_file=out_file if out_file is not None else self.out_file,
            data=data if data is not None else self.data,
            data2=data2 if data2 is not None else self.data2,
            vertical_base_line=vertical_base_line
            if vertical_base_line is not None
            else self.vertical_base_line,
            horizontal_base_line=horizontal_base_line
            if horizontal_base_line is not None
            else self.horizontal_base_line,
            sheet=sheet if sheet is not None else self.sheet,
            marker=marker if marker is not None else self.marker,
            x_axis=x_axis if x_axis is not None else self.x_axis,
            y1_axis=y1_axis if y1_axis is not None else self.y1_axis,
            y2_axis=y2_axis if y2_axis is not None else self.y2_axis,
            x_label=x_label if x_label is not None else self.x_label,
            y1_label=y1_label if y1_label is not None else self.y1_label,
            y2_label=y2_label if y2_label is not None else self.y2_label,
        )

    def plot(self):
        for i, d in enumerate(self.data):
            self.ax.plot(
                d.x_data,
                d.y_data,
                label=d.label,
                markersize=d.marker.markersize
                if d.marker is not None
                else self.marker[i % len(self.marker)].markersize
                if self.marker is not None
                else None,
                marker=d.marker.marker
                if d.marker is not None
                else self.marker[i % len(self.marker)].marker
                if self.marker is not None
                else None,
                ls=d.marker.ls
                if d.marker is not None
                else self.marker[i % len(self.marker)].ls
                if self.marker is not None
                else None,
                color=d.marker.color
                if d.marker is not None
                else self.marker[i % len(self.marker)].color
                if self.marker is not None
                else None,
            )
        if self.data2 is not None and self.ax2 is not None:
            for i, d in enumerate(self.data2):
                self.ax2.plot(
                    d.x_data,
                    d.y_data,
                    label=d.label,
                    markersize=d.marker.markersize
                    if d.marker is not None
                    else self.marker[(i + len(self.data)) % len(self.marker)].markersize
                    if self.marker is not None
                    else None,
                    marker=d.marker.marker
                    if d.marker is not None
                    else self.marker[(i + len(self.data)) % len(self.marker)].marker
                    if self.marker is not None
                    else None,
                    ls=d.marker.ls
                    if d.marker is not None
                    else self.marker[(i + len(self.data)) % len(self.marker)].ls
                    if self.marker is not None
                    else None,
                    color=d.marker.color
                    if d.marker is not None
                    else self.marker[(i + len(self.data)) % len(self.marker)].color
                    if self.marker is not None
                    else None,
                )
        if self.vertical_base_line is not None:
            for line in self.vertical_base_line:
                if self.ax2 is None:
                    self.ax.axvline(
                        x=line.value,
                        label=line.label,
                        ls=line.linestyle,
                        color=line.color,
                        ymax=line.lim.max if line.lim is not None else 1,
                        ymin=line.lim.min if line.lim is not None else 0,
                    )
                else:
                    self.ax2.axvline(
                        x=line.value,
                        label=line.label,
                        ls=line.linestyle,
                        color=line.color,
                        ymax=line.lim.max if line.lim is not None else 1,
                        ymin=line.lim.min if line.lim is not None else 0,
                    )
        if self.horizontal_base_line is not None:
            for line in self.horizontal_base_line:
                if self.ax2 is None:
                    self.ax.axhline(
                        y=line.value,
                        label=line.label,
                        ls=line.linestyle,
                        color=line.color,
                        xmax=line.lim.max if line.lim is not None else 1,
                        xmin=line.lim.min if line.lim is not None else 0,
                    )
                else:
                    self.ax2.axhline(
                        y=line.value,
                        label=line.label,
                        ls=line.linestyle,
                        color=line.color,
                        xmax=line.lim.max if line.lim is not None else 1,
                        xmin=line.lim.min if line.lim is not None else 0,
                    )

    def set_label(self):
        if self.x_label == []:
            self.ax.set_xlabel(self.data[0].x_label)
        else:
            self.ax.set_xlabel("\n".join(self.x_label))
        if self.y1_label == []:
            self.ax.set_ylabel(self.data[0].y_label)
        else:
            self.ax.set_ylabel("\n".join(self.y1_label))
        if self.ax2 is not None and self.data2 is not None:
            if self.y2_label == []:
                self.ax2.set_ylabel(self.data2[0].y_label)
            else:
                self.ax2.set_ylabel("\n".join(self.y2_label))

    def set_axis(self):
        if isinstance(self.x_axis, Axis):
            if self.x_axis.lim is not None:
                self.ax.set_xlim(self.x_axis.lim.min, self.x_axis.lim.max)
            if self.x_axis.major is not None:
                self.ax.set_xticks(self.x_axis.major)
            if self.x_axis.minor is not None:
                self.ax.xaxis.set_minor_locator(
                    ticker.MultipleLocator(self.x_axis.minor),
                )
            else:
                self.ax.xaxis.set_minor_locator(
                    ticker.NullLocator(),
                )
        elif isinstance(self.x_axis, LogAxis):
            self.ax.set_xscale("log")
            if self.x_axis.lim is not None:
                self.ax.set_xlim(self.x_axis.lim.min, self.x_axis.lim.max)
            if self.x_axis.major is not None:
                self.ax.set_xticks(self.x_axis.major)
            if self.x_axis.minor is not None:
                self.ax.xaxis.set_minor_locator(
                    ticker.LogLocator(
                        numticks=14,
                        subs=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9),
                    )
                )
            else:
                self.ax.xaxis.set_minor_locator(
                    ticker.NullLocator(),
                )
        if isinstance(self.y1_axis, Axis):
            if self.y1_axis.lim is not None:
                self.ax.set_ylim(self.y1_axis.lim.min, self.y1_axis.lim.max)
            if self.y1_axis.major is not None:
                self.ax.set_yticks(self.y1_axis.major)
            if self.y1_axis.minor is not None:
                self.ax.yaxis.set_minor_locator(
                    ticker.MultipleLocator(self.y1_axis.minor),
                )
            else:
                self.ax.yaxis.set_minor_locator(
                    ticker.NullLocator(),
                )
        elif isinstance(self.y1_axis, LogAxis):
            self.ax.set_yscale("log")
            if self.y1_axis.lim is not None:
                self.ax.set_ylim(self.y1_axis.lim.min, self.y1_axis.lim.max)
            if self.y1_axis.major is not None:
                self.ax.set_yticks(self.y1_axis.major)
            if self.y1_axis.minor is not None:
                self.ax.yaxis.set_minor_locator(
                    ticker.LogLocator(
                        numticks=14,
                        subs=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9),
                    )
                )
            else:
                self.ax.yaxis.set_minor_locator(
                    ticker.NullLocator(),
                )
        if self.ax2 is not None and isinstance(self.y2_axis, Axis):
            if self.y2_axis.lim is not None:
                self.ax2.set_ylim(self.y2_axis.lim.min, self.y2_axis.lim.max)
            if self.y2_axis.major is not None:
                self.ax2.set_yticks(self.y2_axis.major)
            if self.y2_axis.minor is not None:
                self.ax2.yaxis.set_minor_locator(
                    ticker.MultipleLocator(self.y2_axis.minor),
                )
            else:
                self.ax2.yaxis.set_minor_locator(
                    ticker.NullLocator(),
                )
        elif self.ax2 is not None and isinstance(self.y2_axis, LogAxis):
            self.ax2.set_yscale("log")
            if self.y2_axis.lim is not None:
                self.ax2.set_ylim(self.y2_axis.lim.min, self.y2_axis.lim.max)
            if self.y2_axis.major is not None:
                self.ax2.set_yticks(self.y2_axis.major)
            if self.y2_axis.minor is not None:
                self.ax2.yaxis.set_minor_locator(
                    ticker.LogLocator(
                        numticks=14,
                        subs=(0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9),
                    )
                )
            else:
                self.ax2.yaxis.set_minor_locator(
                    ticker.NullLocator(),
                )

    def set_legend(self):
        h, l = self.ax.get_legend_handles_labels()
        h2, l2 = (
            self.ax2.get_legend_handles_labels() if self.ax2 is not None else ([], [])
        )
        legend = (
            [d.legend for d in self.data]
            + [d.legend for d in self.data2 or []]
            + [line.legend for line in self.vertical_base_line or []]
            + [line.legend for line in self.horizontal_base_line or []]
        )
        empty_l = [(l + l2)[i] for i, le in enumerate(legend) if le]
        empty_h = [(h + h2)[i] for i, le in enumerate(legend) if le]
        self.ax.legend(
            empty_h,
            empty_l,
            loc="best",
            frameon=False,
            fancybox=False,
            framealpha=1,
        )

    def save(self):
        self.ax.tick_params(axis="both", direction="in", which="both")
        # self.ax2.tick_params(axis="both", direction="in", which="both")
        self.ax.tick_params(
            labelbottom=False, labelleft=False, labelright=False, labeltop=False
        )
        # self.ax.tick_params(bottom=False, left=False, right=False, top=False)
        # self.ax.axis("off")
        self.figure.savefig(self.out_file)

    def execute(self):
        self.plot()
        print(f"plot {self.out_file}")
        self.set_label()
        print(f"set label {self.out_file}")
        self.set_axis()
        print(f"set axis {self.out_file}")
        # self.set_legend()
        print(f"set legend {self.out_file}")
        self.save()
        print(f"save {self.out_file}")


def make_graph(
    graphs: list[Graph],
    multiprocessing: bool = True,
):
    plt.style.use(["science", "ieee"])
    if multiprocessing:
        threads: list[Process] = []
        for graph in graphs:
            t = Process(target=graph.execute)
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
    else:
        for graph in graphs:
            graph.execute()
