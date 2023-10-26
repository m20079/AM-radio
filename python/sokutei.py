from make_graph import (
    make_graph,
    Graph,
    Data,
    Sheet,
    Axis,
    Lim,
    Marker,
    LogAxis,
    BaseLine,
)
import japanize_matplotlib

sheet1 = Sheet("./../data/data.xlsx", "1kHz", skiprows=1)

sheet2 = Sheet("./../data/data.xlsx", "diff", skiprows=0)

sheet3 = Sheet("./../data/data.xlsx", "k", skiprows=1)

marker1 = Marker(marker="o", markersize=4, color="r", ls="None")

marker2 = Marker(marker="D", markersize=4, color="b", ls="None")

marker3 = Marker(marker="s", markersize=4, color="g", ls="None")

marker4 = Marker(marker=",", markersize=1, color="m")

marker5 = Marker(marker=",", markersize=1, color="c")

pdf = "pdf"
folder = "fig"

make_graph(
    multiprocessing=False,
    graphs=[
        Graph(
            f"../{folder}/gain.{pdf}",
            x_label=[r"Frequency $\mathrm{[Hz]}$"],
            y1_label=[
                r"Gain $\mathrm{[dB]}$",
            ],
            y1_axis=Axis(minor=0.5, lim=Lim(min=-2, max=19)),
            x_axis=LogAxis(lim=Lim(min=10**1, max=10**7), minor=True),
            data=[
                Data(
                    x_col="S",
                    y_col="V",
                    sheet=sheet3,
                    marker=marker1,
                    label=r"Measured value",
                ),
            ],
            horizontal_base_line=[
                BaseLine(
                    value=15.1175,
                    label=r"Theoretical value",
                    linestyle="--",
                )
            ],
            vertical_base_line=[
                BaseLine(
                    value=20,
                    label=r"Lowest range",
                    linestyle="-.",
                ),
                BaseLine(
                    value=20000,
                    label=r"Highest range",
                    linestyle=":",
                ),
            ],
        ),
        # Graph(
        #     f"../{folder}/level12.{pdf}",
        #     x_label=[r"Time $\mathrm{[s]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=0.0002),
        #     y1_axis=Axis(minor=0.2, lim=Lim(-4.5, 4.5)),
        #     data=[
        #         Data(
        #             x_col="A",
        #             y_col="C",
        #             sheet=sheet1,
        #             marker=marker1,
        #             label=r"5.7 times",
        #         ),
        #         Data(
        #             x_col="A",
        #             y_col="B",
        #             sheet=sheet1,
        #             marker=marker2,
        #             label=r"32.49 times",
        #         ),
        #     ],
        # ),
        # Graph(
        #     f"../{folder}/level12.{pdf}",
        #     x_label=[r"Time $\mathrm{[s]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=0.0002),
        #     y1_axis=Axis(minor=0.2, lim=Lim(-4.5, 4.5)),
        #     data=[
        #         Data(
        #             x_col="A",
        #             y_col="C",
        #             sheet=sheet1,
        #             marker=marker1,
        #             label=r"5.7 times",
        #         ),
        #         Data(
        #             x_col="A",
        #             y_col="B",
        #             sheet=sheet1,
        #             marker=marker2,
        #             label=r"32.49 times",
        #         ),
        #     ],
        # ),
        # Graph(
        #     f"../{folder}/level34.{pdf}",
        #     x_label=[r"Time $\mathrm{[s]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=0.0002),
        #     y1_axis=Axis(minor=0.1, lim=Lim(-2.9, 2.9)),
        #     data=[
        #         Data(
        #             x_col="J",
        #             y_col="L",
        #             sheet=sheet1,
        #             marker=marker1,
        #             label=r"185.193 times",
        #         ),
        #         Data(
        #             x_col="J",
        #             y_col="K",
        #             sheet=sheet1,
        #             marker=marker2,
        #             label=r"1055.6001 times",
        #         ),
        #     ],
        # ),
    ],
)
