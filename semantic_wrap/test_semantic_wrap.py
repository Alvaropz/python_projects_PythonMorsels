from contextlib import contextmanager, redirect_stdout
from io import StringIO
from importlib.machinery import SourceFileLoader
import os
import sys
from textwrap import dedent
from tempfile import NamedTemporaryFile
import unittest

from semantic_wrap import semantic_wrap


class SemanticWrapTests(unittest.TestCase):

    """Tests for semantic_wrap"""

    maxDiff = None

    def test_single_sentence(self):
        text = "This text is already all on one line."
        self.assertEqual(semantic_wrap(text).strip(), text)

    def test_long_single_sentence(self):
        text = (
            "Whether I'm teaching new Pythonistas or long-time Python " +
            "programmers, I frequently find that **Python programmers " +
            "underutilize multiple assignment**."
        )
        self.assertEqual(
            semantic_wrap(text).strip(),
            "Whether I'm teaching new Pythonistas or long-time Python " +
            "programmers, I frequently find that **Python programmers " +
            "underutilize multiple assignment**."
        )

    def test_two_sentences(self):
        text = (
            "I avail myself of the opportunity which a third edition of "
            '"Jane Eyre" affords me, of again addressing a word to the '
            "Public, to explain that my claim to the title of novelist rests "
            "on this one work alone. If, therefore, the authorship of other "
            "works of fiction has been attributed to me, an honour is awarded "
            "where it is not merited; and consequently, denied where it is "
            "justly due."
        )
        wrapped = (
            "I avail myself of the opportunity which a third edition of "
            '"Jane Eyre" affords me, of again addressing a word to the '
            "Public, to explain that my claim to the title of novelist rests "
            "on this one work alone.\nIf, therefore, the authorship of other "
            "works of fiction has been attributed to me, an honour is awarded "
            "where it is not merited; and consequently, denied where it is "
            "justly due."
        )
        self.assertEqual(semantic_wrap(text).strip(), wrapped)

    def test_multiple_sentences_and_multiple_paragraphs(self):
        text = (
            "Multiple assignment (also known as tuple unpacking or iterable "
            "unpacking) allows you to assign multiple variables at the same "
            "time in one line of code. This feature often seems simple after "
            "you've learned about it, but **it can be tricky to recall "
            "multiple assignment when you need it most**."
            "\n\n"
            "In this article we'll see what multiple assignment is, we'll "
            "take a look at common uses of multiple assignment, and then "
            "we'll look at a few uses for multiple assignment that are "
            "often overlooked."
        )
        wrapped = (
            "Multiple assignment (also known as tuple unpacking or iterable "
            "unpacking) allows you to assign multiple variables at the same "
            "time in one line of code.\n"
            "This feature often seems simple after you've learned about it, "
            "but **it can be tricky to recall multiple assignment when you "
            "need it most**."
            "\n\n"
            "In this article we'll see what multiple assignment is, we'll "
            "take a look at common uses of multiple assignment, and then "
            "we'll look at a few uses for multiple assignment that are "
            "often overlooked."
        )
        self.assertEqual(semantic_wrap(text).strip(), wrapped)

    # To test the Bonus part of this exercise, comment out the following line
    #@unittest.expectedFailure
    def test_different_punctuation_and_spacing(self):
        text = dedent("""
            This is a sentence.  It's followed by another sentence.

            This is a paragraph.  With three sentences.  Three?  Four!  Five.

            But this paragraph just has one sentence, a long one.
        """).lstrip()
        expected = dedent("""
            This is a sentence.
            It's followed by another sentence.

            This is a paragraph.
            With three sentences.
            Three?
            Four!
            Five.

            But this paragraph just has one sentence, a long one.
        """).lstrip()
        self.assertEqual(semantic_wrap(text), expected)

    # To test the Bonus part of this exercise, comment out the following line
    #@unittest.expectedFailure
    def test_wrap_with_quotes(self):
        text = dedent("""
            I prefer putting quotes "inside the period". But not everyone does.

            Some put "quotes outside punctuation." It's quite common actually.
        """).lstrip()
        expected = dedent("""
            I prefer putting quotes "inside the period".
            But not everyone does.

            Some put "quotes outside punctuation."
            It's quite common actually.
        """).lstrip()
        self.assertEqual(semantic_wrap(text), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)