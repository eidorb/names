# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "anywidget==0.11.0",
#     "marimo>=0.24.2",
#     "traitlets==5.16.1",
# ]
# ///

import marimo

__generated_with = "0.24.2"
app = marimo.App(app_title="Names", auto_download=["html"])


@app.cell
def _():
    import math
    import marimo as mo
    import names

    return math, mo, names


@app.cell
def _(mo, names):
    mo.md(rf"""
    # Names

    Sometimes you need to name a bunch of things. But coming up with good names is surprisingly hard! This generates deterministic, human-friendly names without duplicates from a curated list of {len(names.words)} words.
    """)
    return


@app.cell
def _(mo):
    query_params = mo.query_params()
    return (query_params,)


@app.cell
def _(math, mo, names, query_params):
    seed = mo.ui.text(
        value=query_params.get("seed", ""),
        placeholder="Enter a seed...",
        on_change=lambda value: query_params.set("seed", value),
    )

    def n_on_change(value):
        query_params.set("n", str(value))
        # clamp start qparam when n changes
        query_params.set(
            "start",
            str(
                min(
                    int(query_params.get("start", 0)),
                    math.perm(len(names.words), value) - 1,
                )
            ),
        )

    n = mo.ui.dropdown(
        options=list(range(1, 6)),
        value=int(query_params.get("n", "2")),
        on_change=n_on_change,
    )
    count = mo.ui.slider(
        start=1,
        stop=500,
        step=1,
        value=int(query_params.get("count", "10")),
        debounce=True,
        show_value=True,
        on_change=lambda value: query_params.set("count", str(value)),
    )
    return count, n, seed


@app.cell
def _(math, mo, n, names, query_params):
    start = mo.ui.number(
        start=0,
        stop=math.perm(len(names.words), n.value) - 1,
        step=1,
        # clamp value when n changes.
        value=min(
            int(query_params.get("start", 0)),
            math.perm(len(names.words), n.value) - 1,
        ),
        on_change=lambda value: query_params.set("start", str(value)),
    )
    return (start,)


@app.cell
def _(count, math, mo, n, names, seed, start):
    mo.md(rf"""
    ## Name generator

    Choose a **seed** to determine the sequence of names: {seed}

    **n** decides the number of words per name: {n} words gives {math.perm(len(names.words), n.value):,} possible names ($\frac{{{len(names.words)}!}}{{({len(names.words)}-{n.value})!}}$).

    Set **count** to choose how many names to generate: {count}

    Set **start** to jump to any point in the sequence of names: {start}

    The same **seed**, **n**, and **start** will always give you the same name.
    You can bookmark this page and come back to it later — the URL keeps your chosen parameters.
    """)
    return


@app.cell
def _(CopyToClipboard, count, mo, n, names, seed, start):
    mo.md(f"""
    | | | |
    |-|-|-|
    {
        "\n".join(
            f"| {start.value + i} | `{'-'.join(name)}` | {mo.ui.anywidget(CopyToClipboard(text_to_copy='-'.join(name)))} |"
            for i, name in enumerate(
                names.generate_names(seed.value, n.value, count.value, start.value)
            )
        )
    }
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    - Wordlist from [mnemonic encoder project](https://web.archive.org/web/20100105040244/http://tothink.com/mnemonic/index.html)
    - [Source](https://github.com/eidorb/names)
    """)
    return


@app.cell
def _():
    # from https://github.com/koaning/wigglystuff/blob/main/js/copybutton/widget.js
    copybutton_js = """// js/copybutton/widget.js
    const SVG_NS = "http://www.w3.org/2000/svg";

    function createCopyIcon() {
      const svg = document.createElementNS(SVG_NS, "svg");
      svg.setAttribute("viewBox", "0 0 15 15");
      svg.setAttribute("class", "copy-button-icon");
      svg.setAttribute("aria-hidden", "true");
      svg.setAttribute("focusable", "false");

      const path = document.createElementNS(SVG_NS, "path");
      path.setAttribute(
        "d",
        "M1 9.50006C1 10.3285 1.67157 11.0001 2.5 11.0001H4L4 10.0001H2.5C2.22386 10.0001 2 9.7762 2 9.50006L2 2.50006C2 2.22392 2.22386 2.00006 2.5 2.00006L9.5 2.00006C9.77614 2.00006 10 2.22392 10 2.50006V4.00002H5.5C4.67158 4.00002 4 4.67159 4 5.50002V12.5C4 13.3284 4.67158 14 5.5 14H12.5C13.3284 14 14 13.3284 14 12.5V5.50002C14 4.67159 13.3284 4.00002 12.5 4.00002H11V2.50006C11 1.67163 10.3284 1.00006 9.5 1.00006H2.5C1.67157 1.00006 1 1.67163 1 2.50006V9.50006ZM5 5.50002C5 5.22388 5.22386 5.00002 5.5 5.00002H12.5C12.7761 5.00002 13 5.22388 13 5.50002V12.5C13 12.7762 12.7761 13 12.5 13H5.5C5.22386 13 5 12.7762 5 12.5V5.50002Z"
      );
      path.setAttribute("fill", "currentColor");
      path.setAttribute("fill-rule", "evenodd");
      path.setAttribute("clip-rule", "evenodd");
      svg.appendChild(path);
      return svg;
    }

    function fallbackCopy(text) {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.setAttribute("readonly", "");
      textarea.style.position = "fixed";
      textarea.style.top = "0";
      textarea.style.left = "0";
      textarea.style.width = "1px";
      textarea.style.height = "1px";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      textarea.setSelectionRange(0, textarea.value.length);
      const ok = document.execCommand("copy");
      document.body.removeChild(textarea);
      return ok;
    }

    function copyText(text) {
      if (navigator.clipboard && window.isSecureContext) {
        return navigator.clipboard.writeText(text);
      }
      return new Promise((resolve, reject) => {
        try {
          const ok = fallbackCopy(text);
          ok ? resolve() : reject(new Error("Copy command failed"));
        } catch (error) {
          reject(error);
        }
      });
    }

    function render({ model, el }) {
      const wrapper = document.createElement("div");
      wrapper.className = "copy-button-wrapper";

      const button = document.createElement("button");
      button.className = "copy-button";
      button.type = "button";
      button.appendChild(createCopyIcon());

      const label = document.createElement("span");
      const defaultLabel = "Copy to Clipboard";
      label.textContent = defaultLabel;

      wrapper.appendChild(button);
      el.appendChild(wrapper);

      let resetTimer = null;
      const setLabel = (text) => {
        label.textContent = text;
      };

      button.addEventListener("click", () => {
        const text = model.get("text_to_copy") ?? "";
        if (resetTimer) {
          clearTimeout(resetTimer);
          resetTimer = null;
        }
        copyText(text)
          .then(() => setLabel("Copied!"))
          .catch(() => setLabel("Copy failed"))
          .finally(() => {
            resetTimer = setTimeout(() => setLabel(defaultLabel), 1200);
          });
      });
    }

    var widget_default = { render };
    export { widget_default as default };"""
    return (copybutton_js,)


@app.cell
def _():
    # from https://github.com/koaning/wigglystuff/blob/main/wigglystuff/static/copybutton.css
    copybutton_css = """/* CopyToClipboard widget styles - following agents.md pattern */
    .copy-button-wrapper {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      color-scheme: light dark;

      /* CSS Variables for theming - light mode defaults */
      --copy-btn-bg: #e0e0e0;
      --copy-btn-bg-hover: #d0d0d0;
      --copy-btn-bg-active: #c0c0c0;
      --copy-btn-text: #1a1a1a;
      --copy-btn-shadow: rgba(0, 0, 0, 0.1);
      --copy-btn-shadow-hover: rgba(0, 0, 0, 0.15);
    }

     .copy-button {
       display: inline-flex;
       align-items: center;
       justify-content: center;
       width: 20px;
       height: 20px;
       padding: 0;
       color: var(--copy-btn-text);
       background-color: var(--copy-btn-bg);
       border: none;
       border-radius: 3px;
       cursor: pointer;
       transition: background-color 0.15s ease;
       box-shadow: none;
     }

     .copy-button:hover {
       background-color: var(--copy-btn-bg-hover);
     }

     .copy-button:active {
       background-color: var(--copy-btn-bg-active);
     }

    .copy-button:focus {
      outline: 2px solid var(--copy-btn-bg);
      outline-offset: 2px;
    }

    .copy-button:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

     .copy-button-icon {
       width: 11px;
       height: 11px;
       flex-shrink: 0;
     }

    /* Dark mode styles */
    .dark .copy-button-wrapper,
    .dark-theme .copy-button-wrapper,
    [data-theme="dark"] .copy-button-wrapper {
      --copy-btn-bg: #4a4a4a;
      --copy-btn-bg-hover: #5a5a5a;
      --copy-btn-bg-active: #3a3a3a;
      --copy-btn-text: #ffffff;
      --copy-btn-shadow: rgba(0, 0, 0, 0.3);
      --copy-btn-shadow-hover: rgba(0, 0, 0, 0.4);
    }"""
    return (copybutton_css,)


@app.cell
def _(copybutton_css, copybutton_js):
    # from https://github.com/koaning/wigglystuff/blob/main/wigglystuff/copy_to_clipboard.py
    from typing import Any

    import anywidget
    import traitlets

    class CopyToClipboard(anywidget.AnyWidget):
        """Button widget that copies the provided ``text_to_copy`` payload.

        Examples:
            ```python
            import marimo as mo
            from wigglystuff import CopyToClipboard

            button = mo.ui.anywidget(CopyToClipboard(text_to_copy="Hello, world!"))
            button
            ```
        """

        text_to_copy = traitlets.Unicode("").tag(sync=True)
        _esm = copybutton_js
        _css = copybutton_css

        def __init__(self, text_to_copy: str = "", **kwargs: Any):
            """Create a CopyToClipboard button.

            Args:
                text_to_copy: Initial string placed on the clipboard when clicked.
                **kwargs: Forwarded to ``anywidget.AnyWidget``.
            """
            super().__init__(**kwargs)
            self.text_to_copy = text_to_copy

    return (CopyToClipboard,)


if __name__ == "__main__":
    app.run()
