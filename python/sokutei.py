import numpy as np
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

sheet4 = Sheet("./../data/data.xlsx", "valiable", skiprows=1)

sheet5 = Sheet("./../data/data.xlsx", "valiable2", skiprows=1)

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
            f"../{folder}/min_max_v2.{pdf}",
            x_label=[r"Frequency $\mathrm{[kHz]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(
                minor=40,
                major=np.arange(200, 2201, 400),
                lim=Lim(min=150, max=2250),
            ),
            y1_axis=Axis(lim=Lim(-0.2, 5.2), minor=0.1),
            data=[
                Data(
                    x_col="A",
                    y_col="C",
                    sheet=sheet5,
                    marker=marker3,
                    label="min",
                ),
                Data(
                    x_col="F",
                    y_col="H",
                    sheet=sheet5,
                    marker=marker2,
                    label="max",
                ),
            ],
            horizontal_base_line=[
                BaseLine(value=3.33, linestyle="--", label=r"min/$\sqrt{2}$"),
                BaseLine(value=3.28, linestyle="-.", label=r"max/$\sqrt{2}$"),
            ],
        ),
        Graph(
            f"../{folder}/min_max2_v2.{pdf}",
            x_label=[r"Frequency $\mathrm{[kHz]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(
                minor=40,
                major=np.arange(200, 1501, 200),
                lim=Lim(min=100, max=1500),
            ),
            y1_axis=Axis(lim=Lim(-0.2, 5.2), minor=0.1),
            data=[
                Data(
                    x_col="AH",
                    y_col="AJ",
                    sheet=sheet5,
                    marker=marker3,
                    label="min",
                ),
                Data(
                    x_col="AL",
                    y_col="AN",
                    sheet=sheet5,
                    marker=marker2,
                    label="max",
                ),
            ],
            horizontal_base_line=[
                BaseLine(value=3.459, linestyle="--", label=r"min/$\sqrt{2}$"),
                BaseLine(value=3.03985, linestyle="-.", label=r"max/$\sqrt{2}$"),
            ],
        ),
        Graph(
            f"../{folder}/min_max.{pdf}",
            x_label=[r"Frequency $\mathrm{[kHz]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(lim=Lim(min=150, max=1950), minor=20),
            y1_axis=Axis(lim=Lim(-0.2, 5.2), minor=0.1),
            data=[
                Data(
                    x_col="A",
                    y_col="C",
                    sheet=sheet4,
                    marker=marker3,
                    label="min",
                ),
                Data(
                    x_col="F",
                    y_col="H",
                    sheet=sheet4,
                    marker=marker2,
                    label="max",
                ),
            ],
        ),
        Graph(
            f"../{folder}/min_max2.{pdf}",
            x_label=[r"Frequency $\mathrm{[kHz]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(lim=Lim(min=100, max=1400), minor=20),
            y1_axis=Axis(lim=Lim(-0.2, 5.2), minor=0.1),
            data=[
                Data(
                    x_col="AH",
                    y_col="AJ",
                    sheet=sheet4,
                    marker=marker3,
                    label="min",
                ),
                Data(
                    x_col="AL",
                    y_col="AN",
                    sheet=sheet4,
                    marker=marker2,
                    label="max",
                ),
            ],
        ),
        Graph(
            f"../{folder}/inda_inda.{pdf}",
            x_label=[r"Frequency $\mathrm{[kHz]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(lim=Lim(min=280, max=920), minor=10),
            y1_axis=Axis(minor=0.02, lim=Lim(3.7, 5.1)),
            data=[
                Data(
                    x_col="C",
                    y_col="D",
                    sheet=sheet3,
                    marker=marker3,
                    label="Unit1",
                ),
                Data(
                    x_col="G",
                    y_col="H",
                    sheet=sheet3,
                    marker=marker2,
                    label="Unit2",
                ),
                Data(
                    x_col="J",
                    y_col="K",
                    sheet=sheet3,
                    marker=marker1,
                    label="Unit3",
                ),
            ],
        ),
        # Graph(
        #     f"../{folder}/resi.{pdf}",
        #     x_label=[r"Resistance $\mathrm{[\Omega]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=200, major=[10000, 8000, 6000, 4000, 2000, 0]),
        #     y1_axis=Axis(
        #         minor=0.02,
        #         major=[-0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8],
        #     ),
        #     data=[
        #         Data(
        #             x_col="L",
        #             y_col="N",
        #             sheet=sheet4,
        #             marker=marker2,
        #             label=r"185.193 times",
        #         ),
        #     ],
        # ),
        # Graph(
        #     f"../{folder}/koil.{pdf}",
        #     x_label=[r"Time $\mathrm{[s]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=0.002),
        #     y1_axis=Axis(lim=Lim(min=-0.049, max=0.049), minor=0.001),
        #     data=[
        #         Data(
        #             x_col="P",
        #             y_col="Q",
        #             sheet=sheet4,
        #             marker=marker1,
        #             label=r"185.193 times",
        #         ),
        #     ],
        # ),
        # Graph(
        #     f"../{folder}/koil_diode.{pdf}",
        #     x_label=[r"Time $\mathrm{[s]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=0.002),
        #     y1_axis=Axis(lim=Lim(min=-0.049, max=0.049), minor=0.001),
        #     data=[
        #         Data(
        #             x_col="T",
        #             y_col="U",
        #             sheet=sheet4,
        #             marker=marker1,
        #             label=r"185.193 times",
        #         ),
        #     ],
        # ),
        # Graph(
        #     f"../{folder}/koil_diode_bi.{pdf}",
        #     x_label=[r"Time $\mathrm{[s]}$"],
        #     y1_label=[
        #         r"Voltage $\mathrm{[V]}$",
        #     ],
        #     x_axis=Axis(minor=0.002),
        #     y1_axis=Axis(lim=Lim(min=-0.049, max=0.049), minor=0.001),
        #     data=[
        #         Data(
        #             x_col="Z",
        #             y_col="AA",
        #             sheet=sheet4,
        #             marker=marker1,
        #             label=r"185.193 times",
        #         ),
        #     ],
        # ),
        # Graph(
        #     f"../{folder}/gain.{pdf}",
        #     x_label=[r"Frequency $\mathrm{[Hz]}$"],
        #     y1_label=[
        #         r"Gain $\mathrm{[dB]}$",
        #     ],
        #     y1_axis=Axis(minor=0.5, lim=Lim(min=-2, max=19)),
        #     x_axis=LogAxis(lim=Lim(min=10**1, max=10**7), minor=True),
        #     data=[
        #         Data(
        #             x_col="S",
        #             y_col="V",
        #             sheet=sheet3,
        #             marker=marker1,
        #             label=r"Measured value",
        #         ),
        #     ],
        #     horizontal_base_line=[
        #         BaseLine(
        #             value=15.1175,
        #             label=r"Theoretical value",
        #             linestyle="--",
        #         )
        #     ],
        #     vertical_base_line=[
        #         BaseLine(
        #             value=20,
        #             label=r"Lowest range",
        #             linestyle="-.",
        #         ),
        #         BaseLine(
        #             value=20000,
        #             label=r"Highest range",
        #             linestyle=":",
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
