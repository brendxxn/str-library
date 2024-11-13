# -*- coding: utf-8 -*-
"""lab 07

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17yK973ZoUlWLOenRyDQXEt81VX5x88oi
"""

# V00700546 Brendan Pratt

ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"


def is_alpha(word):
  for character in word:
    if character not in ASCII_LOWERCASE and character not in ASCII_UPPERCASE:
      return False
  return True


def is_digit(s):
  for character in s:
    if(character not in DECIMAL_DIGITS):
      return False
  return True

