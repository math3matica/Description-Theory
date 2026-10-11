"""Generate nested contrast-ordering sets for Description Theory review.

Candidate rule: for 1:n, use n+1 Things, enumerate every ordering, and render
 each ordering as a right-nested contrast chain. The complete rule is subject
to the user's review; this script does not calculate probabilities.
"""

from __future__ import annotations

import argparse
from itertools import permutations
from pathlib import Path


def _label_for_index(index: int) -> str:
    """Return spreadsheet-style lowercase labels: a..z, aa, ab, ..."""
    if index < 0:
        raise ValueError("index must be nonnegative")
    label = ""
    while True:
        index, remainder = divmod(index, 26)
        label = chr(ord("a") + remainder) + label
        if index == 0:
            return label
        index -= 1


def render_nested_contrast(items: tuple[str, ...] | list[str]) -> str:
    """Render an ordering as a right-nested contrast with the first item foreground."""
    if not items:
        raise ValueError("at least one Thing is required")
    if len(items) == 1:
        return f"({items[0]})"
    if len(items) == 2:
        return f"({items[0]}) > ({items[1]})"
    return f"({items[0]}) > ({render_nested_contrast(items[1:])})"


def generate_description_set(n: int) -> list[str]:
    """Generate the candidate associated descriptions for 1:n.

    The proposed interpretation of 1:n uses n+1 Things and includes one
    right-nested contrast for every permutation of those Things.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be an integer greater than or equal to 1")
    things = tuple(_label_for_index(i) for i in range(n + 1))
    return [render_nested_contrast(order) for order in permutations(things)]


def render_review_markdown(max_n: int = 4) -> str:
    """Return a review document containing complete sets from 1:1 to 1:max_n."""
    if not isinstance(max_n, int) or isinstance(max_n, bool) or max_n < 1:
        raise ValueError("max_n must be an integer greater than or equal to 1")

    lines = [
        "# Candidate Description Orderings: 1:1 to 1:n",
        "",
        "> **For review, not yet canonical.** This output applies the candidate",
        "> interpretation that 1:n uses n+1 Things, lists every permutation, and",
        "> renders each permutation as a right-nested contrast. The first Thing",
        "> in each ordering is the foreground; the remaining Things form the",
        "> recursively ordered background. No probabilities are calculated here.",
        "",
    ]
    for n in range(1, max_n + 1):
        descriptions = generate_description_set(n)
        lines.extend([f"## 1:{n} — {len(descriptions)} descriptions", ""])
        lines.extend(f"{i}. `{description}`" for i, description in enumerate(descriptions, 1))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate candidate nested contrast orderings for review."
    )
    parser.add_argument(
        "--max-n",
        type=int,
        default=4,
        help="generate complete sets from 1:1 through 1:n (default: 4)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("flow_orderings_1_to_4_review.md"),
        help="output Markdown path (default: beside this script)",
    )
    args = parser.parse_args()

    document = render_review_markdown(args.max_n)
    args.output.write_text(document, encoding="utf-8")
    total = sum(len(generate_description_set(n)) for n in range(1, args.max_n + 1))
    print(f"Wrote {total} descriptions for 1:1 through 1:{args.max_n} to {args.output}")


if __name__ == "__main__":
    main()
