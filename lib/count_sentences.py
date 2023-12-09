#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value=''):
      self.value = value
  pass

  def get_value(self):
   return self._value
  pass

  def set_value(self,value):
    if not isinstance(value, str):
      print("The value must be a string.")
    else:  
      self._value = value

  value = property(get_value,set_value) 

  def is_sentence(self):
    return self._value.endswith('.')
  
  def is_question(self):
    return self._value.endswith('?')
  
  def is_exclamation(self):
    return self._value.endswith('!')
  
  def count_sentences(self):
    # Split the string into sentences based on punctuation marks
    sentences = re.split('[.!?]', self._value)
    # Filter out any empty strings resulting from the split
    sentences = list(filter(None, sentences))
    # Return the count of sentences
    return len(sentences)