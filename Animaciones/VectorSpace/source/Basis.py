from manim import *
from manim_slides import Slide # Import Slide for presentation features
import numpy as np
import sys
sys.path.append("../../")
from CustomColors import CustomColors # Assuming CustomColors is correctly located relative to this script


class BasisOfVectorSpace(Scene, Slide):
    def construct(self):
        self.camera.background_color = CustomColors.LIGHT

        # Setup the 2D coordinate plane
        plane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-6, 6, 1],
            x_length=16,
            y_length=9,
            axis_config={"color": CustomColors.GREY_A},
            background_line_style={
                "stroke_color": CustomColors.DARK,
                "stroke_width": 0.5,
                "stroke_opacity": 0.3
            }
        ).add_coordinates()
        self.add(plane)
        self.next_slide()

        self.introduce_basis_concept()
        self.show_linear_independence(plane)
        self.show_spanning_property(plane)
        self.conclude_basis_concept()

    def introduce_basis_concept(self):
        intro_title = Tex("¿Qué es una Base de un Espacio Vectorial?", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(intro_title))
        self.next_slide()

        basis_text = Tex(
            "Una base es un conjunto de vectores que pueden describir cualquier vector en un espacio dado.",
            color=CustomColors.DARK
        ).scale(0.7).next_to(intro_title, DOWN, buff=0.5)

        conditions_text = VGroup(
            Tex("Para ser una base, el conjunto de vectores debe cumplir dos condiciones:", color=CustomColors.DARK).scale(0.7),
            Tex("1.  Ser **linealmente independiente**.", color=CustomColors.DARK).scale(0.7),
            Tex("2.  **Generar** el espacio vectorial.", color=CustomColors.DARK).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(basis_text, DOWN, aligned_edge=LEFT)
        
        self.play(Write(basis_text))
        self.next_slide()
        for text_mob in conditions_text:
            self.play(FadeIn(text_mob, shift=UP), run_time=0.8)
            self.next_slide()

        self.play(FadeOut(intro_title), FadeOut(basis_text), FadeOut(conditions_text))
        self.next_slide()

    def show_linear_independence(self, plane):
        # Title for this section
        indep_title = Tex("Condición 1: Independencia Lineal", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(indep_title))
        self.next_slide()

        # Demonstrate linear dependence
        dep_title = Tex("Ejemplo: Vectores Linealmente Dependientes", color=CustomColors.DARK).next_to(indep_title, DOWN, buff=0.5)
        self.play(Write(dep_title))
        self.next_slide()

        # Dependent vectors on the same line
        v1_coords = np.array([2, 1, 0])
        v2_coords = np.array([-4, -2, 0])
        v1_dep = Vector(v1_coords, color=CustomColors.RED)
        v2_dep = Vector(v2_coords, color=CustomColors.BLUE)
        v1_dep_label = MathTex(r"\vec{v_1}", color=CustomColors.RED).next_to(v1_dep.get_end(), UP+RIGHT, buff=0.1)
        v2_dep_label = MathTex(r"\vec{v_2}", color=CustomColors.BLUE).next_to(v2_dep.get_end(), DOWN+LEFT, buff=0.1)
        
        self.play(Create(v1_dep), Write(v1_dep_label))
        self.next_slide()
        self.play(Create(v2_dep), Write(v2_dep_label))
        self.next_slide()

        # Show the span of dependent vectors
        span_dep_line = Line(v1_coords * -4, v1_coords * 4, color=CustomColors.TRANSPARENT_YELLOW, stroke_width=5)
        span_text = Tex("Su \"alcance\" (span) es solo una línea.", color=CustomColors.DARK).scale(0.7).to_edge(DOWN)
        
        self.play(Create(span_dep_line, run_time=2), Write(span_text))
        self.next_slide()
        self.play(FadeOut(span_text), FadeOut(v1_dep), FadeOut(v2_dep), FadeOut(v1_dep_label), FadeOut(v2_dep_label), FadeOut(span_dep_line), FadeOut(dep_title))

        # Demonstrate linear independence
        indep_title_2 = Tex("Ejemplo: Vectores Linealmente Independientes", color=CustomColors.DARK).next_to(indep_title, DOWN, buff=0.5)
        self.play(Write(indep_title_2))
        self.next_slide()

        v1_indep_coords = np.array([2, 0, 0])
        v2_indep_coords = np.array([1, 2, 0])
        v1_indep = Vector(v1_indep_coords, color=CustomColors.RED)
        v2_indep = Vector(v2_indep_coords, color=CustomColors.BLUE)
        v1_indep_label = MathTex(r"\vec{v_1}", color=CustomColors.RED).next_to(v1_indep.get_end(), RIGHT, buff=0.1)
        v2_indep_label = MathTex(r"\vec{v_2}", color=CustomColors.BLUE).next_to(v2_indep.get_end(), UP+RIGHT, buff=0.1)

        self.play(Create(v1_indep), Write(v1_indep_label))
        self.next_slide()
        self.play(Create(v2_indep), Write(v2_indep_label))
        self.next_slide()

        self.play(FadeOut(indep_title), FadeOut(indep_title_2))
        self.v1_indep, self.v2_indep = v1_indep, v2_indep
        self.v1_indep_label, self.v2_indep_label = v1_indep_label, v2_indep_label

    def show_spanning_property(self, plane):
        # Spanning title
        span_title = Tex("Condición 2: Generar el Espacio Vectorial", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(span_title))
        self.next_slide()

        # Show a random vector we want to create
        target_point_coords = np.array([4, 3, 0])
        target_vector = Vector(target_point_coords, color=CustomColors.GREEN)
        target_label = MathTex(r"\vec{p}", color=CustomColors.GREEN).next_to(target_vector.get_end(), UP, buff=0.1)

        explain_text = Tex("Podemos usar los vectores independientes para crear cualquier vector en el plano.", color=CustomColors.DARK).scale(0.7).next_to(span_title, DOWN, buff=0.5)

        self.play(Write(explain_text))
        self.next_slide()
        self.play(Create(target_vector), Write(target_label))
        self.next_slide()
        
        # Animate the linear combination
        v1_indep_coords = np.array([2, 0, 0])
        v2_indep_coords = np.array([1, 2, 0])
        c1 = 1.0 # (2*1) + (1*1) = 3 -> (2*2) + (1*1) = 5 (wrong)
        # To get (4, 3), we need to solve:
        # a*v1 + b*v2 = p
        # a*(2,0) + b*(1,2) = (4,3)
        # 2a + b = 4
        # 0a + 2b = 3 -> b = 1.5
        # 2a + 1.5 = 4 -> 2a = 2.5 -> a = 1.25
        c1_val = 1.25
        c2_val = 1.5
        
        scaled_v1 = Vector(v1_indep_coords * c1_val, color=CustomColors.RED)
        scaled_v2_shifted = Vector(v2_indep_coords * c2_val, color=CustomColors.BLUE).shift(scaled_v1.get_end())
        
        sum_eq = MathTex(
            f"{c1_val} \\vec{{v_1}} + {c2_val} \\vec{{v_2}} = \\vec{{p}}",
            color=CustomColors.DARK
        ).scale(0.8).next_to(target_label, RIGHT, buff=1.5)

        self.play(ReplacementTransform(self.v1_indep, scaled_v1))
        self.next_slide()
        self.play(ReplacementTransform(self.v2_indep, scaled_v2_shifted))
        self.next_slide()
        
        # Show tip-to-tail addition
        self.play(
            FadeOut(self.v1_indep_label), FadeOut(self.v2_indep_label),
            Write(sum_eq)
        )
        self.wait(1)
        self.next_slide()
        self.play(
            FadeOut(scaled_v1),
            FadeOut(scaled_v2_shifted),
            FadeOut(target_vector),
            FadeOut(target_label),
            FadeOut(sum_eq)
        )
        self.next_slide()
        self.play(FadeOut(explain_text), FadeOut(span_title))
        
    def conclude_basis_concept(self):
        conclusion_title = Tex("Conclusión: Las dos condiciones", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        conclusion_text = VGroup(
            Tex("Un conjunto de vectores es una base si:", color=CustomColors.DARK).scale(0.7),
            Tex("1.  **Son linealmente independientes** (no redundantes).", color=CustomColors.DARK).scale(0.7),
            Tex("2.  **Generan el espacio** (pueden llegar a cualquier punto).", color=CustomColors.DARK).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(conclusion_title, DOWN, buff=0.5)

        self.play(Write(conclusion_title))
        self.next_slide()
        for text_mob in conclusion_text:
            self.play(Write(text_mob))
            self.next_slide()

        final_thought = Tex(
            "Una base nos da una \"dirección\" y un \"alcance\" para cada dimensión del espacio.",
            color=CustomColors.DARK
        ).scale(0.6).next_to(conclusion_text, DOWN, buff=0.8)

        self.play(Write(final_thought))
        self.next_slide()
        self.play(FadeOut(VGroup(conclusion_title, conclusion_text, final_thought)))
        self.wait(1)
