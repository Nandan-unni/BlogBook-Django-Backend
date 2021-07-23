from bs4 import BeautifulSoup


def _remove_dots_and_spaces_(chars: list):
    _prev_dot_ = False
    summary = ""
    for char in chars:
        if char == ".":
            if not _prev_dot_:
                summary += char + " "
            _prev_dot_ = True
        elif char.endswith("."):
            summary += char + " "
            _prev_dot_ = True
        else:
            summary += char
            _prev_dot_ = False
    while True:
        if summary.startswith("."):
            summary = summary[1:]
        else:
            break
    summary = summary.strip()
    return summary


def get_summary(rich_text: str):
    soup = BeautifulSoup(rich_text, features="html.parser")
    for tag in soup(["script", "style", "h1", "h2", "code"]):
        tag.extract()
    summary = soup.get_text().strip("\n").replace("\n", ". ").strip()
    summary = _remove_dots_and_spaces_(summary.split())
    return summary
