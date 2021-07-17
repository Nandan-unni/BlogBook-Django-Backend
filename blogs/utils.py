demo = """<h1 style="text-align:center;"><span style="color: rgb(26,188,156);"><strong><em><ins>Test</ins></em></strong></span></h1>
<h3><span style="color: rgb(250,197,28);"><strong><ins>Test</ins></strong></span></h3>
<p>Test</p>
<div style="text-align:left;"><img src="https://htmlcolorcodes.com/assets/images/html-color-codes-color-tutorials-hero.jpg" alt="undefined" style="height: auto;width: 100px"/></div>
<p></p>
"""
from bs4 import BeautifulSoup


def get_summary(content: str):
    soup = BeautifulSoup(content, features="html.parser")
    for tag in soup(["script", "style", "h1", "h2", "code"]):
        tag.extract()
    for tag in soup.find_all():
        if len(tag.get_text(strip=True)) == 0:
            tag.extract()
    return soup.get_text().strip("\n").replace("\n", ". ").strip()


get_summary(demo)
