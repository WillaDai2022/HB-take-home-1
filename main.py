class Canvas:

    def __init__(self, width, height):
        """Constructor of the canvas"""
        self.shapes = []
        self.canvas_width = width
        self.canvas_height = height
        self.canvas = [(["."]*self.canvas_width) for i in range(self.canvas_height)]


    def clear_canvas(self):
        """Render an empty canvas"""
        self.canvas = [(["."]*self.canvas_width) for i in range(self.canvas_height)]
        self.shapes = []
      
        self.print_canvas()

    def render_canvas(self):
        """Show canvas with or shapes"""
        for rect in self.shapes:
            self.draw_rectangle(rect)
        
        self.print_canvas()

    def add_shape(self,rect):
        self.shapes.append(rect)

    def draw_rectangle(self, rect):
        """Draw a rectangle"""

        for i in range(max(0,self.canvas_height - rect.end_y), max(0,self.canvas_height - rect.start_y)):
            for j in range(rect.start_x, min(rect.end_x+1, self.canvas_width)):
                self.canvas[i][j] = rect.fill_char

    def print_canvas(self):
        """Print current canvas"""
        for i in self.canvas:
            sum = ""
            for j in i:
                sum += j
            print(sum)
    
class Rectangle:
    """A rectangle"""
    
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char

        # self.size = [([fill_char]*(end_x - start_x + 1)) for i in range((end_y - start_y + 1))]


    def change_char(self, fill_char):
        """"Change the fill character"""
        self.fill_char = fill_char
    
    def translate(self, axis, num):
        """translate the shape"""
        if axis == "x":
            self.start_x += num
            self.end_x += num

        if axis == "y":
            self.start_y += num
            self.end_y += num