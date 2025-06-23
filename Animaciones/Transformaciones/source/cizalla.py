from manim import *
import numpy as np
# Import Slide from manim_slides for presentation features
from manim_slides import Slide

# Define custom colors as ManimColor objects for easy use
class CustomColors:
    LIGHT = ManimColor("#ffffff")
    LIGHTGRAY = ManimColor("#9ed6e7")
    GRAY = ManimColor("#ff5f5c")
    DARKGRAY = ManimColor("#050403")
    DARK = ManimColor("#000000") # Black for text
    SECONDARY = ManimColor("#070c42")
    TERTIARY = ManimColor("#ff5f5c") # Same as GRAY
    # For highlight with alpha, we define a base color and set opacity separately
    HIGHLIGHT_BASE = ManimColor("#84b6d5") # Base color from rgba(132, 182, 213, 0.15)
    TEXT_HIGHLIGHT = ManimColor("#0ffbc4")

class LinearTransformationSceneSlide(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

class LinearTransformationSlide(LinearTransformationSceneSlide, ApplyMatrix):
    
    pass

class SimpleLinearTransformationSlides(Slide, LinearTransformationSlide): # Changed base class to Slide
    
    def construct(self):
        """
        Constructs a simple linear transformation animation as a series of slides.
        """
        self.camera.background_color = CustomColors.LIGHT
        
        title = Tex("Veamos un ejemplo de transformación lineal en el plano", color=BLACK)

        rectangle = Rectangle(color=BLACK, fill_color=WHITE,fill_opacity=1, width=title.width+1, height=title.height+1)
        rectangle.surround(title)
        rect_vgroup = VGroup(rectangle,title)
        rect_vgroup.move_to([0,3,0])
        self.add(rect_vgroup)
        self.wait()
        self.next_slide()

        transform_title = MarkupText(f'Esta transformación se conoce como <span fgcolor="{CustomColors.TERTIARY}">cizalla</span>', color=BLACK)
        transform_title.move_to([0,3,0])
        self.play(
            Transform(title, transform_title),
        )
        self.wait()
        self.next_slide()

        self.remove(rect_vgroup)


        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()
        self.next_slide()

        # # --- Scene Setup: Plane and Basis Vectors ---
        # # Manually create the NumberPlane as LinearTransformationScene is no longer the base class
        # plane = NumberPlane(
        #     x_range=[-5, 5, 1],
        #     y_range=[-5, 5, 1],
        #     axis_config={"color": CustomColors.DARK},
        #     background_line_style={
        #         "stroke_color": CustomColors.SECONDARY, # Dark blue for grid lines
        #         "stroke_width": 3,
        #         "stroke_opacity": 0.6,
        #     }
        # ).add_coordinates(font_size=24, color=CustomColors.DARK)
        # self.next_slide()

        # # Create basis vectors
        # i_hat = Arrow(ORIGIN, RIGHT, buff=0, color=RED).set_stroke(width=8)
        # j_hat = Arrow(ORIGIN, UP, buff=0, color=GREEN).set_stroke(width=8)
        # basis_vectors = VGroup(i_hat, j_hat, NumberPlane())

        # self.add(plane, basis_vectors)
        # self.next_slide() # Slide 1: Show initial grid and basis vectors

        # # --- Define and Apply Matrix ---
        # matrix = [[1, 1], [0, 1]] # Shear matrix

        # self.play(ApplyMatrix(matrix, basis_vectors))
        # self.next_slide()
        # self.wait()

