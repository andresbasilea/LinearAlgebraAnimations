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
            show_basis_vectors=True, # Ensure basis vectors are shown        # Ensure grid is shown
            **kwargs
        )

class LinearTransformationSlide(LinearTransformationSceneSlide, ApplyMatrix):
    pass

class SimpleLinearTransformationSlides(Slide, LinearTransformationSlide):
    def construct(self):
        """
        Constructs a simple linear transformation animation as a series of slides.
        """
        self.camera.background_color = CustomColors.LIGHT

        # --- Slide 1: Title Introduction ---
        title = Tex("Veamos un ejemplo de transformación lineal en el plano", color=BLACK)
        rectangle = Rectangle(color=BLACK, fill_color=WHITE, fill_opacity=1, width=title.width+1, height=title.height+1)
        rectangle.surround(title)
        rect_vgroup = VGroup(rectangle, title)
        rect_vgroup.move_to([0,3,0])
        self.add(rect_vgroup)
        self.wait()
        self.next_slide()

        # --- Slide 2: Transformation Type Title ---
        transform_title = MarkupText(f'Esta transformación se conoce como <span fgcolor="{CustomColors.TERTIARY}">cizalla</span>', color=BLACK)
        transform_title.move_to([0,3,0])
        self.play(
            Transform(title, transform_title),
        )
        self.wait()
        self.next_slide()

        # --- Slide 3: Prepare for Transformation ---
        # We need to transition from the title to the linear transformation view.
        # This is where the grid and basis vectors should become the main focus.

        # 1. Fade out the title elements
        self.play(FadeOut(rect_vgroup))
        self.wait(0.5)

        # 2. Now the grid and basis vectors (which were initialized by LinearTransformationSceneSlide)
        #    are the primary focus. They should be visible on screen at their default positions.
        #    The next call to apply_matrix will then animate them FROM these positions.

        matrix = [[1, 1], [0, 1]]

        # You might want to show the matrix itself:
        matrix_mob = Matrix(matrix, h_buff=1.5, v_buff=1.5, element_to_mobject=MathTex, fill_color=WHITE).scale(1.2).set_color(BLACK)
        matrix_mob.to_corner(UL) # Position it
        self.play(FadeIn(matrix_mob))
        self.wait()
        self.next_slide()
        # The apply_matrix animation will start from the current (identity) state
        # of the grid and basis vectors.
        self.apply_matrix(matrix)
        self.wait()
        self.next_slide()

        

        