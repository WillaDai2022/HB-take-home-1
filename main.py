class Canvas:
    """Canvas"""

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
            self._draw_rectangle(rect)
        
        self.print_canvas()

    def add_shape(self,shape):
        """Add a shape to a canvas"""
        if not isinstance(shape, Shape):
            raise TypeError(f"Canvas.addShape is not supported with shape {shape}")
        self.shapes.append(shape)

    def _draw_rectangle(self, rect):
        """Draw a rectangle"""

        for i in range(rect.start_x, rect.end_x + 1):
            for j in range(rect.start_y, rect.end_y + 1):
                if 0 <= i <= self.canvas_width and 0 <= j <= self.canvas_height:
                    self.canvas[i][j] = rect.fill_char

    def print_canvas(self):
        """Print current canvas"""
        for i in self.canvas:
            sum = ""
            for j in i:
                sum += j
            print(sum)

class Shape():
    pass

    
class Rectangle(Shape):
    """A rectangle"""
    
    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        """Constructor
            start_x is the X coordinate of the upper-left-hand corner of the rectangle
            start_y is the Y coordinate of the upper-left-hand corner of the rectangle
            end_x is the X coordinate of the lower-right-hand corner of the rectangle
            end_y is the Y coordinate of the lower-right-hand corner of the rectangle
            fill_char is the character that should be used to draw the rectangle
        """
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char = fill_char


    def change_char(self, fill_char):
        """"Change the fill character"""
        self.fill_char = fill_char
    
    def translate(self, axis, num):
        """translate the shape"""
        if axis not in("x","y"):
            raise TypeError(f"Axis should be either x or y")

        if axis == "x":
            self.start_x += num
            self.end_x += num

        if axis == "y":
            self.start_y += num
            self.end_y += num