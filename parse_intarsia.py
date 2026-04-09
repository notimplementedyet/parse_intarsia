import argparse
import math
from PIL import Image

# hex -> name
colors = {}

# hex -> number
max_cakes = {}

# List of segments per row
segments = []

class Segment:
  __slots__ = ['color', 'startIndex', 'endIndex']
  def __init__(self, color, startIndex):
    # hex
    self.color = color
    self.startIndex = startIndex
    self.endIndex = -1

  def __repr__(self):
    return "["+ str(self.color) + ", (" + str(self.startIndex) + ", " + str(self.endIndex) + ")]"

  def toMachineRow(self, imageWidth, ltor=True, offset=None):
    if offset is None:
      offset = math.ceil(imageWidth / 2.0)
    left = abs(self.startIndex - offset)
    if self.startIndex > offset:
      left += 1
    right = abs(self.endIndex - offset)
    if self.endIndex > offset:
      right += 1
    
    c_name = getColor(self.color)
    if ltor:
      return "Color %s, %d to %d" % (c_name, left, right)
    else:
      return "Color %s, %d to %d" % (c_name, right, left)


def preprocess(image):
  width, height = image.size
  pixels = image.load()
  next_color = len(colors)
  
  for y in range(height):
    row = []
    curr_pixel = pixels[0, y]
    
    if curr_pixel not in colors:
      colors[curr_pixel] = next_color
      next_color += 1
      
    start_x = 0
    row_cakes = {}
    
    for x in range(1, width):
      pixel = pixels[x, y]
      if pixel != curr_pixel:
        segment = Segment(curr_pixel, start_x)
        segment.endIndex = x - 1
        row.append(segment)
        
        row_cakes[curr_pixel] = row_cakes.get(curr_pixel, 0) + 1
        
        curr_pixel = pixel
        start_x = x
        if curr_pixel not in colors:
          colors[curr_pixel] = next_color
          next_color += 1

    # Grab the last segment
    segment = Segment(curr_pixel, start_x)
    segment.endIndex = width - 1
    row.append(segment)
    row_cakes[curr_pixel] = row_cakes.get(curr_pixel, 0) + 1

    # Figure out how many cakes of each color we need
    # for this row and keep track of the max for later.
    for color, count in row_cakes.items():
      if count > max_cakes.get(color, 0):
        max_cakes[color] = count
    segments.append(row)

def getColor(color):
  index = colors[color]
  if named_colors and index < len(named_colors) and named_colors[index]:
    return named_colors[index]
  return str(index)


def main(fileName):
  image = Image.open(fileName)

  preprocess(image)

  print("-- File info --")
  print("File: " + fileName + " is " + str(image.width) + " by "+str(image.height) + " pixels")
  print("Expecting work between %d on the left and %d on the right." % (math.ceil(image.width / 2.0), math.floor(image.width / 2.0)))
  print("-- Colors --")
  print(str(len(colors)) + " colors. Indexed from the top left.")
  for color, numCakes in max_cakes.items():
    print("Color " + str(getColor(color)) + ": " + str(numCakes) + " cakes")

  row = len(segments) - 1
  rows_seen = 0
  width = image.width
  offset = math.ceil(width / 2.0)
  print("\nPress ENTER for each row...")
  while row >= 0:
    input()
    print("-- Row %d --" % (len(segments) - row))
    ltor = (rows_seen % 2) == 0
    print("Start on %s" % ("left" if ltor else "right"))
    orderedSegments = segments[row] if ltor else reversed(segments[row])
    for segment in orderedSegments:
      print(segment.toMachineRow(width, ltor=ltor, offset=offset))
    row -= 1
    rows_seen += 1



if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Print out intarsia machine knitting instructions')
  parser.add_argument('--file', type=str,
                    help='the file to read')
  parser.add_argument('--colors', type=str, nargs='+',
                    help='Optional names of colors')

  args = parser.parse_args()
  named_colors = args.colors
  main(args.file)