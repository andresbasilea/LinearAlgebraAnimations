from manim import *
from manim_slides import Slide # Import Slide for presentation features
import numpy as np
import sys
sys.path.append("../../")
from CustomColors import CustomColors



class VectorSubspaces(ThreeDScene, Slide): # Inherit from ThreeDScene and Slide
    def construct(self):
        self.camera.background_color = CustomColors.LIGHT
        
        # Initial camera orientation for a good 3D view
        self.set_camera_orientation(phi=0 * DEGREES, theta=90 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.05) # Slow ambient rotation

        # Setup the 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=10,
            axis_config={"color": CustomColors.GREY_A},
            tips=True
        ).add_coordinates()
        self.add(axes)
        self.next_slide()

        self.introduce_subspace_concept()
        self.show_line_as_2d_subspace(axes)
        self.show_plane_as_3d_subspace(axes)
        self.conclude_subspaces()

        self.stop_ambient_camera_rotation() # Stop rotation at the end

    def introduce_subspace_concept(self):
        intro_title = Tex("¿Qué es un Subespacio Vectorial?", color=CustomColors.DARK).to_edge(UP).scale(1)
        self.play(Write(intro_title))
        self.next_slide()

        conditions_text = VGroup(
            Tex("Un subconjunto $W$ de un espacio vectorial $V$ es un subespacio si:", color=CustomColors.DARK).scale(0.7),
            Tex("1. El vector cero $\\vec{0}$ está en $W$.", color=CustomColors.DARK).scale(0.7),
            Tex("2. $W$ es cerrado bajo la suma de vectores (si $\\vec{u}, \\vec{v} \\in W$, entonces $\\vec{u} + \\vec{v} \\in W$).", color=CustomColors.DARK).scale(0.7),
            Tex("3. $W$ es cerrado bajo la multiplicación escalar (si $\\vec{u} \\in W$ y $c$ es un escalar, entonces $c\\vec{u} \\in W$).", color=CustomColors.DARK).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(intro_title, DOWN, buff=0.8)
        
        for i, text_mob in enumerate(conditions_text):
            self.play(FadeIn(text_mob, shift=UP), run_time=0.8)
            self.next_slide()

        self.play(FadeOut(conditions_text), FadeOut(intro_title))
        self.next_slide()

    def show_line_as_2d_subspace(self, axes):
        # Temporarily adjust camera to focus on 2D (XY plane)

        line_subspace_title = Tex("Una Línea a través del Origen como Subespacio 2D", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(line_subspace_title))
        self.next_slide()

        # Define a 2D vector (with z=0 for 3D context)
        v_line_coords = np.array([1.5, 1, 0])
        v_line = Vector(v_line_coords, color=CustomColors.BLUE)
        v_line_label = MathTex(r"\vec{v}", color=CustomColors.BLUE).next_to(v_line.get_end(), UP+RIGHT)
        self.play(Create(v_line), Write(v_line_label))
        self.next_slide()

        # Show the line (span of v_line)
        line_span = Line(v_line_coords * -3, v_line_coords * 3, color=CustomColors.TRANSPARENT_YELLOW, stroke_width=5)
        self.play(Create(line_span, run_time=2))
        self.next_slide()

        # --- Check Subspace Properties for the Line ---

        # 1. Contains zero vector
        zero_text = Tex("1. Contiene el vector cero (el origen).", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        zero_dot = Dot(ORIGIN, radius=0.1, color=CustomColors.GREEN)
        self.play(Write(zero_text), Flash(zero_dot, flash_radius=0.3, color=CustomColors.GREEN))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(zero_text))

        # 2. Closed under scalar multiplication
        scalar_mult_text = Tex("2. Cerrado bajo la multiplicación escalar.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        
        current_scalar = ValueTracker(1.0)
        scaled_v_temp = always_redraw(
            lambda: Vector(v_line_coords * current_scalar.get_value(), color=CustomColors.YELLOW)
        )
        scaled_v_label_temp = always_redraw(
            lambda: MathTex(r"a\vec{v}", color=CustomColors.YELLOW)
            .next_to(scaled_v_temp.get_end(), UP+RIGHT)
        )
        self.add(scaled_v_temp, scaled_v_label_temp)
        self.play(Write(scalar_mult_text))
        self.play(current_scalar.animate.set_value(2.5), run_time=1.5)
        self.play(current_scalar.animate.set_value(-2.0), run_time=1.5)
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(scaled_v_temp), FadeOut(scaled_v_label_temp), FadeOut(scalar_mult_text))

        # 3. Closed under vector addition
        add_text = Tex("3. Cerrado bajo la suma de vectores.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        u_coords = v_line_coords * 1.5
        w_coords = v_line_coords * -0.8
        u = Vector(u_coords, color=CustomColors.BLUE)
        w = Vector(w_coords, color=CustomColors.RED)
        u_label = MathTex(r"\vec{u}", color=CustomColors.BLUE).next_to(u.get_end(), LEFT)
        w_label = MathTex(r"\vec{w}", color=CustomColors.RED).next_to(w.get_end(), DOWN)
        self.play(Create(u), Write(u_label), Create(w), Write(w_label), Write(add_text))
        self.next_slide()

        w_shifted = w.copy().shift(u.get_end())
        sum_vector = Vector(u_coords + w_coords, color=CustomColors.YELLOW)
        sum_label = MathTex(r"\vec{u} + \vec{w}", color=CustomColors.YELLOW).next_to(sum_vector.get_end(), UP)

        self.play(w.animate.become(w_shifted))
        self.next_slide()
        self.play(Create(sum_vector), Write(sum_label))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(u), FadeOut(w), FadeOut(u_label), FadeOut(w_label), FadeOut(w_shifted), FadeOut(sum_vector), FadeOut(sum_label), FadeOut(add_text))
        self.next_slide()


        self.play(FadeOut(v_line), FadeOut(v_line_label), FadeOut(line_span), FadeOut(line_subspace_title))
        self.next_slide()

    def show_plane_as_3d_subspace(self, axes):
        # Reset camera to a good 3D view
        # self.play(self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES, zoom=1))
        # self.next_slide()

        plane_subspace_title = Tex("Un Plano a través del Origen como Subespacio 3D", color=CustomColors.DARK).to_edge(UP).scale(0.8)
        self.play(Write(plane_subspace_title))
        self.next_slide()

        # Define two linearly independent vectors in 3D (e.g., in the XY plane)
        v1_plane_coords = np.array([2, 1, 0])
        v2_plane_coords = np.array([-1, 2, 0])

        v1_plane = Vector(v1_plane_coords, color=CustomColors.BLUE)
        v2_plane = Vector(v2_plane_coords, color=CustomColors.RED)
        v1_plane_label = MathTex(r"\vec{v_1}", color=CustomColors.BLUE).next_to(v1_plane.get_end(), RIGHT+OUT)
        v2_plane_label = MathTex(r"\vec{v_2}", color=CustomColors.RED).next_to(v2_plane.get_end(), UP+OUT)

        self.play(Create(v1_plane), Write(v1_plane_label), Create(v2_plane), Write(v2_plane_label))
        self.next_slide()

        # Show the plane (span of v1_plane and v2_plane)
        plane_func = lambda u, v: u * v1_plane_coords + v * v2_plane_coords
        plane_span = Surface(
            plane_func,
            u_range=[-1.5, 1.5], v_range=[-1.5, 1.5],
            resolution=(15, 15),
            fill_opacity=0.6,
            checkerboard_colors=[CustomColors.BLUE, CustomColors.RED]
        )
        self.play(Create(plane_span, run_time=3))
        self.next_slide()

        # --- Check Subspace Properties for the Plane ---

        # 1. Contains zero vector
        zero_text_plane = Tex("1. Contiene el vector cero (el origen).", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        zero_dot_plane = Dot(ORIGIN, radius=0.1, color=CustomColors.GREEN)
        self.play(Write(zero_text_plane), Flash(zero_dot_plane, flash_radius=0.3, color=CustomColors.GREEN))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(zero_text_plane))

        # 2. Closed under scalar multiplication
        scalar_mult_text_plane = Tex("2. Cerrado bajo la multiplicación escalar.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        p_coords = v1_plane_coords * 0.8 + v2_plane_coords * 0.5
        p_vector = Vector(p_coords, color=CustomColors.YELLOW)
        p_label = MathTex(r"\vec{p}", color=CustomColors.YELLOW).next_to(p_vector.get_end(), UP+OUT)
        self.play(Create(p_vector), Write(p_label), Write(scalar_mult_text_plane))
        self.next_slide()

        current_scalar_plane = ValueTracker(1.0)
        scaled_p_temp = always_redraw(
            lambda: Vector(p_coords * current_scalar_plane.get_value(), color=CustomColors.GREEN)
        )
        scaled_p_label_temp = always_redraw(
            lambda: MathTex(r"c\\vec{p}", color=CustomColors.GREEN)
            .next_to(scaled_p_temp.get_end(), RIGHT+OUT)
        )
        self.add(scaled_p_temp, scaled_p_label_temp)
        self.play(current_scalar_plane.animate.set_value(1.8), run_time=1.5)
        self.play(current_scalar_plane.animate.set_value(-1.2), run_time=1.5)
        self.wait(0.5)
        self.next_slide()
        self.play(FadeOut(p_vector), FadeOut(p_label), FadeOut(scaled_p_temp), FadeOut(scaled_p_label_temp), FadeOut(scalar_mult_text_plane))

        # 3. Closed under vector addition
        add_text_plane = Tex("3. Cerrado bajo la suma de vectores.", color=CustomColors.DARK).scale(0.6).to_edge(DOWN)
        u_plane_coords = v1_plane_coords * 1.0 + v2_plane_coords * 0.5
        w_plane_coords = v1_plane_coords * 0.3 + v2_plane_coords * 1.0
        u_plane = Vector(u_plane_coords, color=CustomColors.BLUE)
        w_plane = Vector(w_plane_coords, color=CustomColors.RED)
        u_plane_label = MathTex(r"\vec{u}", color=CustomColors.BLUE).next_to(u_plane.get_end(), LEFT+OUT)
        w_plane_label = MathTex(r"\vec{w}", color=CustomColors.RED).next_to(w_plane.get_end(), DOWN+OUT)
        self.play(Create(u_plane), Write(u_plane_label), Create(w_plane), Write(w_plane_label), Write(add_text_plane))
        self.next_slide()

        w_plane_shifted = w_plane.copy().shift(u_plane.get_end())
        sum_plane_vector = Vector(u_plane_coords + w_plane_coords, color=CustomColors.YELLOW)
        sum_plane_label = MathTex(r"\vec{u} + \vec{w}", color=CustomColors.YELLOW).next_to(sum_plane_vector.get_end(), UP+OUT)

        self.play(w_plane.animate.become(w_plane_shifted))
        self.next_slide()
        self.play(Create(sum_plane_vector), Write(sum_plane_label))
        self.wait(1)
        self.next_slide()
        self.play(
            FadeOut(u_plane), FadeOut(w_plane), FadeOut(u_plane_label), FadeOut(w_plane_label),
            FadeOut(w_plane_shifted), FadeOut(sum_plane_vector), FadeOut(sum_plane_label), FadeOut(add_text_plane)
        )
        self.next_slide()

        self.play(FadeOut(v1_plane), FadeOut(v2_plane), FadeOut(v1_plane_label), FadeOut(v2_plane_label), FadeOut(plane_span), FadeOut(plane_subspace_title))
        self.next_slide()

    def conclude_subspaces(self):
        conclusion = Tex(
            "Los subespacios son \"mini-espacios vectoriales\" que respetan las operaciones del espacio original.",
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        self.play(Write(conclusion))
        self.next_slide()
        self.wait(1)
        self.play(FadeOut(conclusion))
        self.next_slide()