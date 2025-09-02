from manim import *
from manim_slides import Slide # Import Slide for presentation features
import numpy as np
import sys
sys.path.append("../../")
from CustomColors import CustomColors


class SumOfTwoVectors(Slide):
    v1_coords = [2,1]
    v2_coords = [2,-1]

    def construct(self):
        # Set background color using the  method of ManimColor
        self.camera.background_color = CustomColors.LIGHT
        
        # Setup the coordinate plane
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-6, 6, 1],
            x_length=16,
            y_length=9,
            # Pass  for parameters expecting a string hex value
            axis_config={"color": CustomColors.DARK},
            background_line_style={
                "stroke_color": CustomColors.DARK,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3
            }
        ).add_coordinates()
        self.add(plane)
        self.next_slide()

        self.introduce_vectors_for_sum()
        self.show_graphical_sum()


    def introduce_vectors_for_sum(self):
        # Create the first vector and its coordinates
        # Pass ManimColor objects directly or  if string is required
        v1 = Vector(np.array(self.v1_coords), color=CustomColors.BLUE)
        coords1 = Matrix(np.array(self.v1_coords).reshape(-1, 1)).next_to(v1.get_end(), RIGHT, buff=MED_SMALL_BUFF)
        v1_label = MathTex(r"\vec{v_1}", color=CustomColors.BLUE).next_to(v1.get_end(), UP, buff=0.1)

        # Create the second vector and its coordinates
        v2 = Vector(np.array(self.v2_coords), color=CustomColors.RED)
        coords2 = Matrix(np.array(self.v2_coords).reshape(-1, 1)).next_to(v2.get_end(), RIGHT, buff=MED_SMALL_BUFF)
        v2_label = MathTex(r"\vec{v_2}", color=CustomColors.RED).next_to(v2.get_end(), DOWN, buff=0.1)

        # Title for vector introduction
        intro_title = MarkupText(
            f'Introduciendo dos <span fgcolor="{CustomColors.BLUE}">vectores</span> para la suma',
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        intro_title.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(Write(intro_title))
        self.next_slide()
        self.play(Create(v1), Write(v1_label), Write(coords1))
        self.next_slide()
        self.play(Create(v2), Write(v2_label), Write(coords2))
        self.next_slide()

        self.v1, self.v2 = v1, v2
        self.v1_label, self.v2_label = v1_label, v2_label
        self.coords1, self.coords2 = coords1, coords2
        self.intro_title = intro_title

    def show_graphical_sum(self):
        v1, v2 = self.v1, self.v2
        v1_label, v2_label = self.v1_label, self.v2_label
        coords1, coords2 = self.coords1, self.coords2
        intro_title = self.intro_title

        # Prepare title for graphical sum
        graphical_sum_title = MarkupText(
            f'Suma de vectores: <span fgcolor="{CustomColors.YELLOW}">Método Gráfico</span>',
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        graphical_sum_title.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(Transform(intro_title, graphical_sum_title))
        self.next_slide()

        # Animate moving v2's tail to v1's head
        v2_shifted = v2.copy().shift(v1.get_end())
        v2_shifted_label = v2_label.copy().next_to(v2_shifted.get_end(), RIGHT, buff=0.1)

        self.play(
            v2.animate.become(v2_shifted),
            Transform(v2_label, v2_shifted_label),
            FadeOut(coords1), FadeOut(coords2),
            run_time=1.5
        )
        self.next_slide()

        # Draw the resultant vector
        resultant_coords = np.array(self.v1_coords) + np.array(self.v2_coords)
        resultant_vector = Vector(resultant_coords, color=CustomColors.YELLOW)
        resultant_label = MathTex(r"\vec{v_1} + \vec{v_2}", color=CustomColors.YELLOW).next_to(resultant_vector.get_end(), UP+RIGHT, buff=0.1)

        self.play(Create(resultant_vector), Write(resultant_label))
        self.next_slide()
        self.wait(1)

        self.resultant_vector = resultant_vector
        self.resultant_label = resultant_label
        self.v2_shifted = v2_shifted

    
