from PIL import Image

class Image_File:
    def __init__(self, file_name):
        self.image = Image.open(file_name)
        self.pix = self.image.load()
        self.top_colors = dict()

    def find_top_colors(self):
        """
        Loop through entire picture 
        find colors and add count to dictionary
        """
        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                color = self.pix[x,y]
                if color not in self.top_colors.keys():
                    self.top_colors[color] = 1
                else:
                    self.top_colors[color] += 1

        # Sorts dictionary only for Python 3.6+
        self.top_colors = {k: v for k, v in sorted(self.top_colors.items(), key=lambda x: x[1], reverse=True)}

    def show_nth_popular_color(self, n=list(range(0,5))):

        color_shown = []
        for index in n:
            color_shown.append(list(self.top_colors.keys())[index])

        new_image = self.image.copy()
        pix = new_image.load()
        for x in range(self.image.size[0]):
            for y in range(self.image.size[1]):
                color = self.pix[x,y]
                if color in color_shown:
                    pix[x,y] = (0,0,0,0)
                else:
                    pix[x,y] = (255,255,255,255)
        new_image.show()    

if __name__ == "__main__":
    img = Image_File("images/qrcode_black.png")
    img.find_top_colors()
    print(img.top_colors.items())
    img.show_nth_popular_color(n=[0])