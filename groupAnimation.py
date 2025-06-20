from manim import *
import numpy as np

class GroupAxiomsAnimation(Scene):
    def construct(self):
        # 0. Setup: Title and initial vector
        title = Text("Propiedades de los Grupos de Rotación", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Set up the coordinate system for visualizing vectors
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": GRAY, "stroke_width": 1},
        ).add_coordinates()
        self.play(Create(axes), run_time=1)
        self.wait(0.5)

        # Initial vector
        initial_vector_end = np.array([2, 1, 0])
        initial_vector = Arrow(
            ORIGIN, initial_vector_end, buff=0, color=BLUE, tip_length=0.2
        )
        vector_label = MathTex(r"\vec{v}").next_to(initial_vector.get_end(), RIGHT, buff=0.1)
        self.play(GrowArrow(initial_vector), Write(vector_label))
        self.wait(1)

        # Helper function to apply rotation and update vector/label
        def apply_rotation(vector_mobject, angle_rad, duration=1.5, label_text=None, label_pos=RIGHT):
            """Rotates a vector and updates its label."""
            current_angle = initial_vector.get_angle() # Angle relative to x-axis
            target_angle = current_angle + angle_rad

            # Create a copy to animate rotation
            rotated_vector = vector_mobject.copy()
            # Rotation around Z-axis (2D plane)
            self.play(
                rotated_vector.animate.rotate(angle_rad, about_point=ORIGIN),
                run_time=duration
            )
            # Update the original vector to its new state
            vector_mobject.become(rotated_vector)

            if label_text:
                new_label = MathTex(label_text).next_to(vector_mobject.get_end(), label_pos, buff=0.1)
                self.play(Transform(vector_label, new_label), run_time=0.5)
            self.wait(0.5)

        # 1. Closure Axiom
        self.next_section("Closure Axiom")
        closure_title = Text("1) Cerradura", font_size=36).to_edge(UL).shift(RIGHT * 2)
        self.play(Transform(title, closure_title))
        self.wait(0.5)

        closure_text = MathTex(r"\forall a, b \in G, (a \ast b) \in G").next_to(closure_title, DOWN, aligned_edge=LEFT)
        self.play(Write(closure_text))
        self.wait(1)

        # Reset vector for new axiom
        self.play(initial_vector.animate.put_start_and_end_on(ORIGIN, initial_vector_end),
                  Transform(vector_label, MathTex(r"\vec{v}").next_to(initial_vector.get_end(), RIGHT, buff=0.1)))
        self.wait(0.5)

        angle1 = PI / 3 # 60 degrees
        angle2 = PI / 4 # 45 degrees

        # Apply first rotation
        rotation1_text = Text("Rotación 'a' (60°)").next_to(closure_text, DOWN, aligned_edge=LEFT)
        self.play(Write(rotation1_text))
        apply_rotation(initial_vector, angle1, label_text=r"\vec{v}'")
        self.play(FadeOut(rotation1_text))

        # Apply second rotation
        rotation2_text = Text("Rotación 'b' (45°)").next_to(closure_text, DOWN, aligned_edge=LEFT)
        self.play(Write(rotation2_text))
        apply_rotation(initial_vector, angle2, label_text=r"\vec{v}''")
        self.play(FadeOut(rotation2_text))

        result_text = Text("El resultado es otra rotación", font_size=24).next_to(closure_text, DOWN, aligned_edge=LEFT)
        self.play(Write(result_text))
        self.wait(2)
        self.play(FadeOut(result_text, closure_text))


        # 2. Associativity Axiom
        self.next_section("Associativity Axiom")
        associativity_title = Text("2) Asociatividad", font_size=36).to_edge(UL).shift(RIGHT * 2)
        self.play(Transform(title, associativity_title))
        self.wait(0.5)

        associativity_text = MathTex(r"\forall a, b, c \in G, a \ast (b \ast c) = (a \ast b) \ast c").next_to(associativity_title, DOWN, aligned_edge=LEFT)
        self.play(Write(associativity_text))
        self.wait(1)

        # Reset vector
        self.play(initial_vector.animate.put_start_and_end_on(ORIGIN, initial_vector_end),
                  Transform(vector_label, MathTex(r"\vec{v}").next_to(initial_vector.get_end(), RIGHT, buff=0.1)))
        self.wait(0.5)

        angle_a = PI / 6  # 30 deg
        angle_b = PI / 4  # 45 deg
        angle_c = PI / 3  # 60 deg

        # First grouping: a * (b * c)
        group1_label = Text("a * (b * c)").next_to(associativity_text, DOWN, aligned_edge=LEFT)
        self.play(Write(group1_label))
        # Apply b then c
        v_b_copy = initial_vector.copy()
        apply_rotation(v_b_copy, angle_b, duration=1, label_text=r"b(\vec{v})")
        apply_rotation(v_b_copy, angle_c, duration=1, label_text=r"c(b(\vec{v}))")
        # Store final position
        final_pos1 = v_b_copy.get_end()
        # Apply a
        apply_rotation(v_b_copy, angle_a, duration=1, label_text=r"a(c(b(\vec{v})))")
        self.play(FadeOut(group1_label))
        self.wait(1)

        # Reset vector for second grouping
        self.play(initial_vector.animate.put_start_and_end_on(ORIGIN, initial_vector_end),
                  Transform(vector_label, MathTex(r"\vec{v}").next_to(initial_vector.get_end(), RIGHT, buff=0.1)))
        self.wait(0.5)

        # Second grouping: (a * b) * c
        group2_label = Text("(a * b) * c").next_to(associativity_text, DOWN, aligned_edge=LEFT)
        self.play(Write(group2_label))
        # Apply a then b
        v_ab_copy = initial_vector.copy()
        apply_rotation(v_ab_copy, angle_a, duration=1, label_text=r"a(\vec{v})")
        apply_rotation(v_ab_copy, angle_b, duration=1, label_text=r"b(a(\vec{v}))")
        # Apply c
        apply_rotation(v_ab_copy, angle_c, duration=1, label_text=r"c(b(a(\vec{v})))")
        self.play(FadeOut(group2_label))
        self.wait(1)

        # Show equivalence
        equivalence_text = Text("Ambos caminos llegan al mismo resultado", font_size=24).next_to(associativity_text, DOWN, aligned_edge=LEFT)
        self.play(Write(equivalence_text))
        self.wait(2)
        self.play(FadeOut(equivalence_text, associativity_text))


        # 3. Identity Axiom
        self.next_section("Identity Axiom")
        identity_title = Text("3) Existencia del elemento idéntico", font_size=36).to_edge(UL).shift(RIGHT * 2)
        self.play(Transform(title, identity_title))
        self.wait(0.5)

        identity_text = MathTex(r"\exists e \in G \mid a \ast e = e \ast a = a").next_to(identity_title, DOWN, aligned_edge=LEFT)
        self.play(Write(identity_text))
        self.wait(1)

        # Reset vector
        self.play(initial_vector.animate.put_start_and_end_on(ORIGIN, initial_vector_end),
                  Transform(vector_label, MathTex(r"\vec{v}").next_to(initial_vector.get_end(), RIGHT, buff=0.1)))
        self.wait(0.5)

        identity_op_text = Text("Aplicar 'e' (rotación de 0°)").next_to(identity_text, DOWN, aligned_edge=LEFT)
        self.play(Write(identity_op_text))
        apply_rotation(initial_vector, 0, duration=1, label_text=r"\vec{v}") # Rotate by 0
        self.play(FadeOut(identity_op_text))

        result_text = Text("El vector no cambia", font_size=24).next_to(identity_text, DOWN, aligned_edge=LEFT)
        self.play(Write(result_text))
        self.wait(2)
        self.play(FadeOut(result_text, identity_text))


        # 4. Inverse Axiom
        self.next_section("Inverse Axiom")
        inverse_title = Text("4) Existencia de elementos inversos", font_size=36).to_edge(UL).shift(RIGHT * 2)
        self.play(Transform(title, inverse_title))
        self.wait(0.5)

        inverse_text = MathTex(r"\forall a \in G, \exists a^{-1} \in G \mid a \ast a^{-1} = a^{-1} \ast a = e").next_to(inverse_title, DOWN, aligned_edge=LEFT)
        self.play(Write(inverse_text))
        self.wait(1)

        # Reset vector
        self.play(initial_vector.animate.put_start_and_end_on(ORIGIN, initial_vector_end),
                  Transform(vector_label, MathTex(r"\vec{v}").next_to(initial_vector.get_end(), RIGHT, buff=0.1)))
        self.wait(0.5)

        angle_val = PI / 2 # 90 degrees
        
        # Apply rotation 'a'
        op_a_text = Text("Aplicar 'a' (rotación de 90°)").next_to(inverse_text, DOWN, aligned_edge=LEFT)
        self.play(Write(op_a_text))
        apply_rotation(initial_vector, angle_val, label_text=r"\vec{v}'")
        self.play(FadeOut(op_a_text))

        # Apply inverse rotation 'a^-1'
        op_inv_text = Text("Aplicar 'a^{-1}' (rotación de -90°)").next_to(inverse_text, DOWN, aligned_edge=LEFT)
        self.play(Write(op_inv_text))
        apply_rotation(initial_vector, -angle_val, label_text=r"\vec{v}")
        self.play(FadeOut(op_inv_text))

        result_text = Text("El vector regresa a su posición original", font_size=24).next_to(inverse_text, DOWN, aligned_edge=LEFT)
        self.play(Write(result_text))
        self.wait(2)
        self.play(FadeOut(result_text, inverse_text, title, axes, initial_vector, vector_label))

