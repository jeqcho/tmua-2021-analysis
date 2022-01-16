from PIL import Image
import sys


def process_file(filename):
    f = open('output/%s.txt' % filename, 'w')
    sys.stdout = f  # Change the standard output to the file we created.
    original_image = 'images/%s.jpg' % filename
    input_image = Image.open(original_image)
    # Extracting pixel map:
    pixel_map = input_image.load()

    def colour_distance(pixel1, pixel2):
        diff = 0
        for x in range(3):
            diff += abs(pixel1[x] - pixel2[x])
        return diff

    def similar_colour(pixel1, pixel2):
        return colour_distance(pixel1, pixel2) < 100

    width, height = input_image.size
    light_blue = [189, 215, 239]
    blue = []
    for i in range(width):
        bar_height = 0
        bar_heights = []
        for j in range(height):
            # getting the RGB pixel value.
            rgb = input_image.getpixel((i, j))
            if similar_colour(rgb, light_blue):
                bar_height += 1
                pixel_map[i, j] = (255, 0, 0)
            else:
                # skip if it is not a bar
                if bar_height > 10:
                    bar_heights.append(bar_height)
                    # skip if it is the same bar with the previous column
                    if not blue or blue[-1] != bar_height:
                        blue.append(bar_height)
                bar_height = 0

    print("Number of bars detected", len(blue))
    total = sum(blue)
    cum = [0]
    for x in range(len(blue)):
        cum.append(cum[-1] + blue[x] / total * 100)
    cum.pop(0)
    print("Cumulative percentage of each bar:")
    for x in cum:
        print(str(round(x, 2)) + '%')
    input_image.save("output/red-%s.png" % filename, format="png")
    f.close()


process_file('paper1')
process_file('paper2')
process_file('overall')
