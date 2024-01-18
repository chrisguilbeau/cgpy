from unittest import TestCase
from unittest import main
from tags import t

class TestTags(TestCase):
    def test_html(self):
        t.html()
    def test_meta(self):
        assert t.meta(_async=True, src="test.js") == "<meta async src='test.js'></meta>"

if __name__ == "__main__":
    main()
