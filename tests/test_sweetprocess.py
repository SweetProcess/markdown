import unittest
import markdown

test_text = """
\n\n1. Introduce yourself and explain the purpose of the interview.\n\n2. Outline the general structure of the interview and explain that the participant is free to elaborate on any point they feel is important.\n\n3. Ask open-ended questions about the participant's experience of walking as a child. Questions may include:\n\n• What were your favorite walking destinations as a child?\n\n• How did walking make you feel?\n\n• What did you think about while walking?\n\n• What were the most memorable walking experiences you had as a child?\n\n• What was your relationship with walking as a child?\n\n• How did you and your family use walking as a mode of transportation?\n\n4. Ask follow-up questions to further explore the participant's experience.\n\n5. Thank the participant for their time.
"""

class TestSweetprocess(unittest.TestCase):
    """ Tests basics of the Markdown class. """

    def setUp(self):
        """ Create instance of Markdown. """
        self.md = markdown.Markdown()

    def test_sample_list_text(self):
        # print(self.md.convert(test_text.replace('•', '  •')))
        print(self.md.convert(test_text))

    def test_wrapped_unindented_list_text(self):
        print(self.md.convert("""
        \n\nYou might want to start with this:
        \n\n1. one
        \n\n2. two
        \n\nWhat is going on in here? I have no idea what is going on here.
        \n\n- two
        \n\n* three
        \n\nThen you migth want to do this:
        \n\n1. this
        \n\n2. that
        """))

    def test_weird_stuff(self):
        print(self.md.convert("""
        \n\nThis & that.
        \n\n
        \n\n4 < 5.
        \n\n
        \n\n6 > 5.
        \n\n
        """))
