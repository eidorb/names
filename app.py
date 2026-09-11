import marimo

__generated_with = "0.24.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import names

    return mo, names


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Names
    """)
    return


@app.cell
def _(mo, names):
    mo.ui.table(names.words)
    return


if __name__ == "__main__":
    app.run()
