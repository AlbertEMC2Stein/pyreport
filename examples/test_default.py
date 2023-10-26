from pyreport.section import Segment
from pyreport.figure import Image
from pyreport.table import Table
from pyreport.text import PlainText
from pyreport.report import Reporter


def make_test_report():
    """Creates a test report."""

    kwargs = {
        "author": "Albert Einstein",
        "title": "Annalen der Physik",
        "date": "",
        "maketoc": True,
        "maketitle": False,
        "type": "report",
        "titlepage": "notitlepage",
    }
    reporter = Reporter("test_report", **kwargs)

    chapter1 = Segment("The Final Solution", "chapter", "chapter1")
    content = PlainText("This is a test report.")
    chapter1.add_to_content(content)
    section1 = Segment("Intro", "section", "section1")
    section1.add_to_content(Image("data/test.jpg", name="test",
                            width=0.2, caption="This is an image.", label="test"))

    subsection11 = Segment("Sub Intro", "subsection", "subsection11")
    section2 = Segment("Main", "section", "section2")
    section3 = Segment("Conclusion", "section", "section3")

    subsection11.add_to_content(PlainText("This is some plain text."))
    subsection11.add_to_content(
        Table("data/test.csv", caption="This is a table.", label="test"))

    section1.add_to_content(subsection11)
    chapter1.add_to_content(section1)
    chapter1.add_to_content(section2)
    chapter1.add_to_content(section3)
    reporter.add_to_document(chapter1)

    reporter.print_structure()
    reporter.report()


if __name__ == "__main__":
    make_test_report()