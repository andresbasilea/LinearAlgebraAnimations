from manim import *
from manim_slides import Slide # Import Slide for presentation features
import numpy as np
import sys
sys.path.append("../../")
from CustomColors import CustomColors




class ScalarVectorMultiplication(Slide):
    initial_v_coords = [2, 1] # Coordinates for the initial vector

    def construct(self):
        self.camera.background_color = CustomColors.LIGHT
        
        # Setup the coordinate plane
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=8,
            axis_config={"color": CustomColors.GREY_A},
            background_line_style={
                "stroke_color": CustomColors.GREY_A,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3
            }
        ).add_coordinates()
        self.add(plane)
        self.next_slide()

        self.introduce_vector_and_scalar()
        self.show_scaling_animation()
        self.conclude_scalar_multiplication()

    def introduce_vector_and_scalar(self):
        # Create the initial vector
        v = Vector(np.array(self.initial_v_coords), color=CustomColors.BLUE)
        v_label = MathTex(r"\vec{v}", color=CustomColors.BLUE).next_to(v.get_end(), UP+RIGHT, buff=0.1)
        
        # Create coordinates for the initial vector
        coords_v = Matrix(np.array(self.initial_v_coords).reshape(-1, 1)).next_to(v_label, RIGHT, buff=0.5)
        coords_v.add_to_back(BackgroundRectangle(coords_v, fill_opacity=0.8, fill_color=CustomColors.LIGHT))

        # Title for introduction
        intro_title = MarkupText(
            f'Introduciendo un <span fgcolor="{CustomColors.BLUE}">vector</span> y un <span fgcolor="{CustomColors.RED}">escalar</span>',
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        intro_title.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(Write(intro_title))
        self.next_slide()
        self.play(Create(v), Write(v_label), Write(coords_v))
        self.next_slide()

        # Create a ValueTracker for the scalar 'a'
        scalar_val = ValueTracker(1.0) # Start with scalar = 1

        scalar_text = always_redraw(
            lambda: MathTex(f"a = {scalar_val.get_value():.1f}", color=CustomColors.RED)
            .next_to(coords_v, DOWN, buff=1.0) # Position below vector coords
            .add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)
        )
        scalar_label = MathTex(r"a", color=CustomColors.RED).next_to(scalar_text, LEFT, buff=0.2)

        self.play(Write(scalar_text), Write(scalar_label))
        self.next_slide()

        self.v = v
        self.v_label = v_label
        self.coords_v = coords_v
        self.intro_title = intro_title
        self.scalar_val = scalar_val
        self.scalar_text = scalar_text
        self.scalar_label = scalar_label

    def show_scaling_animation(self):
        v, v_label = self.v, self.v_label
        coords_v = self.coords_v
        intro_title = self.intro_title
        scalar_val = self.scalar_val
        scalar_text, scalar_label = self.scalar_text, self.scalar_label

        # Create the scaled vector, its label, and coordinates (always_redraw)
        scaled_v_animated = always_redraw(
            lambda: Vector(np.array(self.initial_v_coords) * scalar_val.get_value(), color=CustomColors.YELLOW)
        )
        scaled_v_label_animated = always_redraw(
            lambda: MathTex(r"a\vec{v}", color=CustomColors.YELLOW)
            .next_to(scaled_v_animated.get_end(), UP+RIGHT, buff=0.1)
        )
        
        scaled_coords_animated = always_redraw(
            lambda: Matrix((np.array(self.initial_v_coords) * scalar_val.get_value()).reshape(-1, 1))
            .next_to(scaled_v_label_animated, RIGHT, buff=0.5)
            .add_to_back(BackgroundRectangle(fill_opacity=0.8, fill_color=CustomColors.LIGHT))
        )

        # Title for scaling process
        scaling_title = MarkupText(
            f'Escalando el vector por un <span fgcolor="{CustomColors.RED}">escalar</span>',
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        scaling_title.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(Transform(intro_title, scaling_title))
        self.next_slide()

        # Fade out original vector and coords, bring in scaled version
        self.play(
            FadeOut(v), FadeOut(v_label),
            FadeOut(coords_v),
            Create(scaled_v_animated),
            Write(scaled_v_label_animated),
            Write(scaled_coords_animated)
        )
        self.next_slide()

        # Animate the scalar changing and the vector scaling
        explan_text = Tex("Si $a > 0$, la dirección se mantiene, la magnitud cambia.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        explan_text.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)
        self.play(Write(explan_text))
        self.play(scalar_val.animate.set_value(2.5))
        self.play(scalar_val.animate.set_value(0.5))
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(explan_text))

        explan_text_neg = Tex("Si $a < 0$, la dirección se invierte, la magnitud cambia.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        explan_text_neg.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)
        self.play(Write(explan_text_neg))
        self.play(scalar_val.animate.set_value(-1.5))
        self.play(scalar_val.animate.set_value(-2.0))
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(explan_text_neg))

        explan_text_zero = Tex("Si $a = 0$, el vector se convierte en el vector nulo.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        explan_text_zero.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)
        self.play(Write(explan_text_zero))
        self.play(scalar_val.animate.set_value(0.0))
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(explan_text_zero))
        self.play(scalar_val.animate.set_value(1.0)) # Reset for conclusion

        self.scaled_v_animated = scaled_v_animated
        self.scaled_v_label_animated = scaled_v_label_animated
        self.scaled_coords_animated = scaled_coords_animated


    def conclude_scalar_multiplication(self):
        # Final conclusion text
        final_text = Tex(
            "La multiplicación escalar cambia la longitud de un vector y puede invertir su dirección.",
            color=CustomColors.DARK
        ).scale(0.7).to_edge(DOWN)
        final_text.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(FadeOut(self.intro_title)) # This is the transformed title
        self.play(Write(final_text))
        self.next_slide()
        self.wait(1)
        self.play(
            FadeOut(self.scaled_v_animated), FadeOut(self.scaled_v_label_animated),
            FadeOut(self.scaled_coords_animated),
            FadeOut(self.scalar_text), FadeOut(self.scalar_label),
            FadeOut(final_text)
        )
        self.next_slide()
