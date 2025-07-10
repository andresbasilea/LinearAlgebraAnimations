from manim import *
# Import Slide from manim_slides for presentation features
from manim_slides import Slide
import sys
sys.path.append("../../")
from CustomColors import CustomColors
import numpy as np


class TwoDVectorSpan(Slide):
    def construct(self):
        self.camera.background_color = CustomColors.LIGHT
        title = Tex("Veamos otro ejemplo de transformación lineal en el plano", color=BLACK)

        # Setup the coordinate plane
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-4.5, 4.5, 1],
            x_length=16,
            y_length=9,
            axis_config={"color": CustomColors.NUMBERPLANEHORIZONTAL},
            background_line_style={
                "stroke_color": CustomColors.DARK,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5
            }
        ).add_coordinates()
        self.add(plane)
        self.next_slide()

        # Define two vectors
        v1 = Vector([2, 1], color=BLUE)
        v2 = Vector([-1, 2], color=CustomColors.RED)

        # Add labels to the vectors
        v1_label = Tex(r"$\vec{v}$", color=BLUE).next_to(v1.get_end(), UP + RIGHT)
        v2_label = Tex(r"$\vec{w}$", color=CustomColors.RED).next_to(v2.get_end(), UP + LEFT)

        # Introduce the vectors
        self.play(Create(v1), Write(v1_label))
        self.next_slide()
        self.play(Create(v2), Write(v2_label))
        self.next_slide()


        # Show w span
        self.play(
            FadeOut(v1),
            FadeOut(v1_label),
            v2_label.animate.next_to(v2.get_end(), RIGHT)
        )
        self.next_slide()

        transform_title = MarkupText(f'Imaginemos que escalamos el vector w, <span fgcolor="{CustomColors.TRANSPARENTRED}">generando una línea</span>', color=BLACK).scale(0.4)
        transform_title.move_to([0,3,0])
        self.play(
            Transform(title, transform_title),
        )
        self.wait()
        self.next_slide()

        line_path = VGroup()
        scalar_factors = np.linspace(-3,-3,50)
        initial_line = Line(ORIGIN, v2.get_end(), color=CustomColors.TRANSPARENTRED, stroke_width=0.8)
        line_path.add(initial_line)
        self.add(initial_line)

        for i in range(1, len(scalar_factors)):
            next_scaled_end = v2.get_end() * scalar_factors[i]
            # Create a small segment from the previous point to the current scaled point
            segment = Line(
                v2.get_end() * scalar_factors[i-1],
                next_scaled_end,
                color=CustomColors.TRANSPARENTRED,
                stroke_width=0.8
            )
            line_path.add(segment)

            self.play(
                Transform(v2, Vector(next_scaled_end, color=CustomColors.TRANSPARENTRED)),
                Create(segment), # Draw the segment
                run_time=0.9,
                rate_func=linear
            )
        self.wait()
        self.next_slide()





        # # Animate scaling of v2 to show it generates a line
        # line_path = VGroup()
        # current_v2 = v2.copy()
        # current_v2.stroke_width=0.8 # Start with a copy to scale

        # # Scale v2 by different factors
        # scalar_factors = np.linspace(-3, 3, 50) # From -3 to 3 to cover the line
        
        # # Initial segment of the line
        # initial_line = Line(ORIGIN, current_v2.get_end() * 0, color=CustomColors.TRANSPARENTRED, stroke_width=0.8)
        # line_path.add(initial_line)

        # # Animate scaling and drawing the line
        # for i in range(1, len(scalar_factors)):
        #     next_scaled_end = v2.get_end() * scalar_factors[i]
        #     # Create a small segment from the previous point to the current scaled point
        #     segment = Line(
        #         v2.get_end() * scalar_factors[i-1],
        #         next_scaled_end,
        #         color=CustomColors.TRANSPARENTRED,
        #         stroke_width=0.8
        #     )
        #     line_path.add(segment)

        #     self.play(
        #         Transform(current_v2, Vector(next_scaled_end, color=CustomColors.TRANSPARENTRED)),
        #         Create(segment), # Draw the segment
        #         run_time=0.5,
        #         rate_func=linear
        #     )
        # self.wait()
        # self.next_slide()
        
        # # Keep the full line generated
        # self.remove(current_v2) # Remove the animating vector
        # self.add(line_path) # Add the full line as a single mobject or VGroup

        # # Label the span of v2
        # span_v2_label = Tex("Span($\\vec{w}$)", color=CustomColors.RED).next_to(line_path, UP + LEFT, buff=0.5)
        # self.play(
        #     FadeOut(scale_text),
        #     Write(span_v2_label)
        # )
        # self.next_slide()

        # # Explain that it's a line
        # explanation = Tex("The span of a single non-zero vector in 2D is a line passing through the origin.").to_edge(DOWN)
        # self.play(Write(explanation))
        # self.next_slide()

        # # Clean up before next segment if any
        # self.play(
        #     FadeOut(line_path),
        #     FadeOut(v2), # v2 might still be there if current_v2 was a transform of it
        #     FadeOut(v2_label),
        #     FadeOut(span_v2_label),
        #     FadeOut(explanation)
        # )
        # self.next_slide()




        # # Explain linear combination
        # title = Tex("Linear Combination: $a\\vec{v} + b\\vec{w}$").to_edge(UP)
        # self.play(Write(title))
        # self.next_slide()

        # # Show a few linear combinations
        # scalars = [(1.5, 0.5), (0.7, 1.3), (-1, -0.8), (2, -0.5)]
        # sum_vectors = VGroup()

        # for a, b in scalars:
        #     scaled_v1 = v1.copy().scale(a)
        #     scaled_v2 = v2.copy().scale(b)
            
        #     # Move scaled_v2 to the end of scaled_v1 for vector addition visualization
        #     shifted_scaled_v2 = scaled_v2.copy().shift(scaled_v1.get_end())
            
        #     # The resultant vector
        #     resultant_vector = Vector(shifted_scaled_v2.get_end(), color=YELLOW)

        #     self.play(
        #         Transform(v1, scaled_v1),
        #         Transform(v2, shifted_scaled_v2),
        #         FadeOut(v1_label), # Fade out labels during transformation
        #         FadeOut(v2_label),
        #         run_time=1.5
        #     )
        #     self.next_slide()
        #     self.play(Create(resultant_vector))
        #     sum_vectors.add(resultant_vector.copy()) # Keep a copy of the sum vector
        #     self.next_slide()
        #     self.play(
        #         FadeOut(scaled_v1),
        #         FadeOut(shifted_scaled_v2),
        #         FadeOut(resultant_vector),
        #         FadeIn(v1), # Bring back original vectors
        #         FadeIn(v2),
        #         FadeIn(v1_label), # Bring back labels
        #         FadeIn(v2_label),
        #         run_time=0.5
        #     )
        #     self.next_slide()

        # self.play(FadeOut(title))
        # self.next_slide()

        # # Define the concept of span
        # span_text = Tex("The span of two vectors is the set of all their linear combinations.").to_edge(UP)
        # self.play(Write(span_text))
        # self.next_slide()

        # # Show the span filling the plane
        # # Create a large number of dots representing the end points of many linear combinations
        # # This creates the visual effect of filling the plane
        # dots = VGroup()
        # for i in range(-20, 20):
        #     for j in range(-20, 20):
        #         a = i * 0.2
        #         b = j * 0.2
        #         point = v1.get_end() * a + v2.get_end() * b
        #         dots.add(Dot(point, radius=0.05, color=YELLOW))

        # self.play(
        #     FadeOut(v1),
        #     FadeOut(v2),
        #     FadeOut(v1_label),
        #     FadeOut(v2_label),
        #     FadeOut(sum_vectors), # Remove previous sum vectors
        #     Create(dots, run_time=5, lag_ratio=0.01) # Animate dots appearing
        # )
        # self.next_slide()
        # self.wait(2)

        # # Conclude
        # conclusion = Tex("For two non-parallel vectors in 2D, their span is the entire 2D plane.").to_edge(DOWN)
        # self.play(Write(conclusion))
        # self.next_slide()
        # self.wait(2)