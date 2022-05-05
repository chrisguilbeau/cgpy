from unittest import TestCase
from unittest import main
from cgpy.tags import t

class TestTags(TestCase):
    def test_html(self):
        t.html()
        t._()
        t.div(t.div(t.div()))


if __name__ == "__main__":
    main()
