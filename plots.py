import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from config import STYLES_DIR, RESULTS_DIR


df = pd.read_json(RESULTS_DIR / "bench.jsonl", lines=True)

font = {"size": 14}
matplotlib.rc("font", **font)
with plt.style.context(STYLES_DIR / "rose-pine-moon.mplstyle"):
    plt.figure(figsize=(10, 8))
    plt.title("Standalone 1-CPU Pydantic v1 vs v2")
    splot = sns.barplot(
        data=df,
        x="display_name",
        y="elapsed",
        hue="version",
    )
    splot.set_ylabel("Elapsed time, s")
    splot.set_xlabel("Number of vectors, dimensionality")

    for p_1, p_2 in zip(
        splot.patches[: len(splot.patches) // 2],
        splot.patches[len(splot.patches) // 2 :],
    ):
        splot.annotate(
            str(round(p_1.get_height() / p_2.get_height(), 2)) + "x",
            (p_1.get_x() + p_1.get_width() / 2.0, p_1.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
        )

        splot.annotate(
            "x",
            (p_2.get_x() + p_2.get_width() / 2.0, p_2.get_height()),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
        )
    plt.savefig(RESULTS_DIR / "bench.png")
