"""One Star for Monday -- make.fun entry.

One line, at most 25 words, a one-star review of Monday as if Monday
were a restaurant: the waiter arrived late, the coffee was cold, and
the weekend got blamed. The program validates the word count, prints
the review, and writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

REVIEW = (
    "One star. The waiter -- Monday -- arrived late, served cold "
    "coffee, and blamed me for ordering the weekend."
)

MAX_WORDS = 25
TARGET = "/output/entry.txt"


def check_review(review):
    """One line, at most MAX_WORDS words, starting with the rating."""
    if not isinstance(review, str) or not review:
        raise ValueError("entry must be non-empty text")
    if "\n" in review:
        raise ValueError("entry must be exactly one line")
    if review != review.strip():
        raise ValueError("entry must not start or end with whitespace")
    words = review.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            "entry has %d words, must be at most %d" % (len(words), MAX_WORDS)
        )
    if len(words) < 5:
        raise ValueError("entry is too short to be a review")
    if not review.startswith("One star"):
        raise ValueError("entry must open with the one-star rating")
    if not review.endswith("."):
        raise ValueError("entry must end with a period")
    if review.count(".") < 2:
        raise ValueError("entry needs a rating sentence and a complaint")
    return review


def check_restaurant(review):
    """A restaurant review needs the venue, the service, and the food."""
    lowered = review.lower()
    if "monday" not in lowered:
        raise ValueError("entry must review Monday itself")
    if "waiter" not in lowered:
        raise ValueError("entry must mention the waiter")
    if "coffee" not in lowered:
        raise ValueError("entry must mention what was served")
    return review


def main():
    review = check_restaurant(check_review(REVIEW))
    print(review)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(review + "\n")


if __name__ == "__main__":
    main()
