from make_graph import make_graph, Graph, Data, Sheet, Axis, Lim, Marker
import japanize_matplotlib

sheet1 = Sheet("./../data/data.xlsx", "Sheet1", skiprows=0)

sheet2 = Sheet("./../data/data.xlsx", "Sheet1", skiprows=0)

sheet3 = Sheet("./../data/data.xlsx", "Sheet1", skiprows=0)

marker1 = Marker(marker=",", markersize=1, color="r")

marker2 = Marker(marker=",", markersize=1, color="b")

marker3 = Marker(marker=",", markersize=1, color="g")

marker4 = Marker(marker="^", markersize=5, color="c")

marker5 = Marker(marker="s", markersize=5, color="m")

pdf = "svg"
folder = "fig2"

make_graph(
    multiprocessing=False,
    graphs=[
        Graph(
            f"../{folder}/5V.{pdf}",
            x_label=[r"Time $\mathrm{[s]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(minor=0.002),
            y1_axis=Axis(lim=Lim(-8, 8), minor=0.2),
            data=[
                Data(
                    x_col="A",
                    y_col="B",
                    sheet=sheet1,
                    marker=marker1,
                    label=r"$\mathrm{V_{2A} [V]}$",
                ),
            ],
        ),
        Graph(
            f"../{folder}/3V.{pdf}",
            x_label=[r"Time $\mathrm{[s]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(minor=0.002),
            y1_axis=Axis(lim=Lim(-8, 8), minor=0.2),
            data=[
                Data(
                    x_col="D",
                    y_col="E",
                    sheet=sheet1,
                    marker=marker2,
                    label=r"$\mathrm{V_{2A} [V]}$",
                ),
            ],
        ),
        Graph(
            f"../{folder}/Wave.{pdf}",
            x_label=[r"Time $\mathrm{[s]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(minor=0.002),
            y1_axis=Axis(lim=Lim(-8, 8), minor=0.2),
            data=[
                Data(
                    x_col="G",
                    y_col="H",
                    sheet=sheet1,
                    marker=marker3,
                    label=r"$\mathrm{V_{2A} [V]}$",
                ),
            ],
        ),
        Graph(
            f"../{folder}/diode.{pdf}",
            x_label=[r"Time $\mathrm{[s]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(minor=0.002),
            y1_axis=Axis(lim=Lim(-8, 8), minor=0.2),
            data=[
                Data(
                    x_col="J",
                    y_col="K",
                    sheet=sheet1,
                    marker=marker3,
                    label=r"$\mathrm{V_{2A} [V]}$",
                ),
            ],
        ),
        Graph(
            f"../{folder}/capa.{pdf}",
            x_label=[r"Time $\mathrm{[s]}$"],
            y1_label=[
                r"Voltage $\mathrm{[V]}$",
            ],
            x_axis=Axis(minor=0.002),
            y1_axis=Axis(lim=Lim(-8, 8), minor=0.2),
            data=[
                Data(
                    x_col="M",
                    y_col="N",
                    sheet=sheet1,
                    marker=marker3,
                    label=r"$\mathrm{V_{2A} [V]}$",
                ),
            ],
        ),
    ],
)
