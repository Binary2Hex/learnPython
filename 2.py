#!/usr/bin/python

# Prints a sentence in a centered "box" of correct width

sentence = raw_input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - text_width) // 2

print
print ' ' * left_margin + '+' + '-' * text_width + '+'
print ' ' * left_margin + '| '+ ' ' * text_width +' |'
print ' ' * left_margin + '| '+ sentence + ' |'
print ' ' * left_margin + '| '+ ' ' * text_width +' |'
print ' ' * left_margin + '+' + '-' * text_width + '+'
print  
