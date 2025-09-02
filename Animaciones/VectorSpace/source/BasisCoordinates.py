from manim import *
from manim_slides import Slide # Import Slide for presentation features
import numpy as np
import sys
sys.path.append("../../")
from CustomColors import CustomColors # Assuming CustomColors is correctly located relative to this script


class VectorRepresentation(Slide, Scene): # Changed the inheritance order to fix the TypeError
    def construct(self):
        self.camera.background_color = CustomColors.LIGHT

        # Setup the 2D coordinate plane
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            axis_config={"color": CustomColors.GREY_A},
            background_line_style={
                "stroke_color": CustomColors.DARK,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3
            }
        ).add_coordinates()
        self.add(plane)
        self.next_slide()

        self.show_standard_basis(plane)
        self.show_new_basis(plane)
        self.re_express_vector_in_new_basis()
        self.conclude()

    def show_standard_basis(self, plane):
        # Title for standard basis
        std_basis_title = Tex("Representación en la Base Estándar", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(std_basis_title))
        self.next_slide()

        # Standard basis vectors
        i_hat = Vector(RIGHT, color=CustomColors.BLUE).add_tip()
        j_hat = Vector(UP, color=CustomColors.RED).add_tip()
        i_label = MathTex(r"\hat{i}", color=CustomColors.BLUE).next_to(i_hat, RIGHT, buff=0.1)
        j_label = MathTex(r"\hat{j}", color=CustomColors.RED).next_to(j_hat, UP, buff=0.1)
        self.play(Create(i_hat), Write(i_label))
        self.next_slide()
        self.play(Create(j_hat), Write(j_label))
        self.next_slide()
        
        # Target vector to represent
        self.target_vector_coords = np.array([3, 2, 0])
        self.target_vector = Vector(self.target_vector_coords, color=CustomColors.YELLOW).add_tip()
        self.target_label = MathTex(r"\vec{v}", color=CustomColors.YELLOW).next_to(self.target_vector, UP+RIGHT, buff=0.1)
        self.play(Create(self.target_vector), Write(self.target_label))
        self.next_slide()
        
        # Show linear combination
        scaled_i = Vector(self.target_vector_coords[0] * RIGHT, color=CustomColors.BLUE)
        scaled_j = Vector(self.target_vector_coords[1] * UP, color=CustomColors.RED).shift(scaled_i.get_end())
        self.play(Create(scaled_i), Create(scaled_j))
        self.next_slide()
        
        # Show coordinates
        coordinates = MathTex(
            r"\vec{v} = 3\hat{i} + 2\hat{j} \quad \implies \quad \begin{pmatrix} 3 \\ 2 \end{pmatrix}",
            color=CustomColors.DARK
        ).scale(0.8).next_to(std_basis_title, DOWN, buff=1.0)
        self.play(Write(coordinates))
        self.next_slide()
        
        self.play(
            FadeOut(i_hat), FadeOut(j_hat), FadeOut(i_label), FadeOut(j_label),
            FadeOut(scaled_i), FadeOut(scaled_j),
            FadeOut(coordinates), FadeOut(std_basis_title)
        )
        self.next_slide()

    def show_new_basis(self, plane):
        # Title for new basis
        new_basis_title = Tex("Representación en una Nueva Base", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(new_basis_title))
        self.next_slide()

        # Define a new basis
        self.b1_coords = np.array([2, 1, 0])
        self.b2_coords = np.array([-1, 2, 0])
        self.b1 = Vector(self.b1_coords, color=CustomColors.BLUE).add_tip()
        self.b2 = Vector(self.b2_coords, color=CustomColors.RED).add_tip()
        self.b1_label = MathTex(r"\vec{b_1}", color=CustomColors.BLUE).next_to(self.b1, RIGHT, buff=0.1)
        self.b2_label = MathTex(r"\vec{b_2}", color=CustomColors.RED).next_to(self.b2, UP, buff=0.1)
        
        self.play(Create(self.b1), Write(self.b1_label))
        self.next_slide()
        self.play(Create(self.b2), Write(self.b2_label))
        self.next_slide()
        
        # Keep the target vector on the screen
        self.play(
            self.target_vector.animate.set_color(CustomColors.YELLOW),
            self.target_label.animate.set_color(CustomColors.YELLOW)
        )
        self.play(Write(new_basis_title))
        self.next_slide()
        
    def re_express_vector_in_new_basis(self):
        # Animate the linear combination in the new basis
        # Solve for c1*b1 + c2*b2 = v
        # c1*(2,1) + c2*(-1,2) = (3,2)
        # 2*c1 - c2 = 3
        # c1 + 2*c2 = 2
        # From eq2: c1 = 2 - 2*c2. Substitute into eq1:
        # 2*(2-2*c2) - c2 = 3
        # 4 - 4*c2 - c2 = 3
        # -5*c2 = -1 -> c2 = 0.2
        # c1 = 2 - 2*0.2 = 1.6
        c1_val = 1.6
        c2_val = 0.2
        
        scaled_b1 = Vector(self.b1_coords * c1_val, color=CustomColors.BLUE).add_tip()
        scaled_b2 = Vector(self.b2_coords * c2_val, color=CustomColors.RED).add_tip().shift(scaled_b1.get_end())
        
        self.play(Create(scaled_b1))
        self.next_slide()
        self.play(Create(scaled_b2))
        self.next_slide()
        
        # Show coordinates in the new basis
        new_coordinates = MathTex(
            r"\vec{v} = 1.6\vec{b_1} + 0.2\vec{b_2} \quad \implies \quad \begin{pmatrix} 1.6 \\ 0.2 \end{pmatrix}",
            color=CustomColors.DARK
        ).scale(0.8).next_to(self.target_label, RIGHT, buff=1.5)
        self.play(Write(new_coordinates))
        self.next_slide()
        
        self.play(
            FadeOut(scaled_b1), FadeOut(scaled_b2),
            FadeOut(new_coordinates),
            FadeOut(self.b1), FadeOut(self.b2), FadeOut(self.b1_label), FadeOut(self.b2_label),
            FadeOut(self.target_vector), FadeOut(self.target_label)
        )
        self.next_slide()
        
    def conclude(self):
        conclusion_title = Tex("Conclusión: La misma flecha, diferentes números", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(conclusion_title))
        self.next_slide()
        
        summary_text = VGroup(
            Tex("El vector $\\vec{v}$ no cambió.", color=CustomColors.DARK),
            Tex("Sus **coordenadas** cambiaron porque usamos una **nueva base**.", color=CustomColors.DARK)
        ).scale(0.7).arrange(DOWN, buff=0.5).next_to(conclusion_title, DOWN, buff=0.5)
        
        self.play(Write(summary_text[0]))
        self.next_slide()
        self.play(Write(summary_text[1]))
        self.next_slide()
        
        self.play(FadeOut(conclusion_title), FadeOut(summary_text))
        self.wait(1)
