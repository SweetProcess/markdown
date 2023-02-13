import unittest
import markdown

test_text = """
\n\n1. Introduce yourself and explain the purpose of the interview.\n\n2. Outline the general structure of the interview and explain that the participant is free to elaborate on any point they feel is important.\n\n3. Ask open-ended questions about the participant's experience of walking as a child. Questions may include:\n\n• What were your favorite walking destinations as a child?\n\n• How did walking make you feel?\n\n• What did you think about while walking?\n\n• What were the most memorable walking experiences you had as a child?\n\n• What was your relationship with walking as a child?\n\n• How did you and your family use walking as a mode of transportation?\n\n4. Ask follow-up questions to further explore the participant's experience.\n\n5. Thank the participant for their time.
"""

class TestSweetprocess(unittest.TestCase):
    """ Tests basics of the Markdown class. """

    def setUp(self):
        """ Create instance of Markdown. """
        self.md = markdown.Markdown(tab_length=2)

    def test_sample_text(self):
        print(self.md.convert(test_text.replace('•', '  •')))
