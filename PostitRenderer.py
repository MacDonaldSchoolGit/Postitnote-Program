import PostitClass
import enum

#all colours of text useable
class TextColours(enum.Enum):
  grey = 1
  red = 2
  green = 3
  yellow = 4
  blue = 5
  magenta = 6
  cyan = 7
  white = 8

#returns a rendered version of the postit for use in console
def renderedPostit(postit):
	return postit.data
