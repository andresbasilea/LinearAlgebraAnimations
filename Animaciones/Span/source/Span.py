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

        v1_coords = np.array([2,1,0])
        v2_coords = np.array([-1, 2,0])
        # Define two vectors
        v1 = Vector(v1_coords, color=BLUE)
        v2 = Vector(v2_coords, color=CustomColors.RED)

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

        transform_title = MarkupText(f'Imaginemos que escalamos el vector w, <span fgcolor="{CustomColors.TRANSPARENTRED}">generando una línea</span>', color=BLACK).scale(0.6)
        transform_title.move_to([0,3,0])
        self.play(
            Write(transform_title),
        )
        self.wait()
        self.next_slide()

        # Create a copy of v2 that will be animated to show scaling
        current_v2_animated = v2.copy().set_color(CustomColors.TRANSPARENTRED)

        # Attach a TracedPath to the end of the animating vector
        # The TracedPath will draw the path as the vector scales
        line_trace = TracedPath(
            current_v2_animated.get_end,
            stroke_color=CustomColors.TRANSPARENTRED,
            stroke_width=0.8 # Make the line a bit thicker
        )
        self.add(line_trace) # Add the trace to the scene

        # Animate the scaling of the vector from -3 to 3
        # Start the vector from the origin (scalar factor 0)
        # This makes the line grow outwards from the center
        self.play(
            Transform(current_v2_animated, Vector(v2.get_end() * 0.001, color=CustomColors.TRANSPARENTRED)),
            run_time=0.1 # Quick snap to origin
        )
        
        # Scale the vector smoothly from the origin to a positive and negative end
        # We'll animate it growing outwards from the center in two phases
        self.play(
            Transform(current_v2_animated, Vector(v2.get_end() * 3, color=CustomColors.TRANSPARENTRED)),
            run_time=2,
            rate_func=linear
        )
        self.play(
            Transform(current_v2_animated, Vector(v2.get_end() * -3, color=CustomColors.TRANSPARENTRED)),
            run_time=2,
            rate_func=linear
        )
        self.play(
            Transform(current_v2_animated, Vector(v2.get_end() * 0.001, color=CustomColors.TRANSPARENTRED)),
            run_time=1,
            rate_func=linear
        )

        self.wait(0.5)
        self.next_slide()

        # # After the animation, you might want to replace the TracedPath with a static Line
        # # for cleaner rendering if the traced path looks jaggy, or just keep it.
        # # Let's create a final Line object and transform the trace into it.
        # final_line_span = Line(v2.get_end() * -3, v2.get_end() * 3, color=CustomColors.TRANSPARENTRED, stroke_width=0.7)

        # self.play(
        #     FadeOut(current_v2_animated), # Remove the animating vector
        #     Transform(line_trace, final_line_span) # Transform the trace into a clean line
        # )
        # self.remove(line_trace) # Remove the old trace object
        # self.add(final_line_span) # Add the new clean line object

        # --- END OF MODIFIED SECTION ---

        # # Add a label for the span of w
        span_w_label = Tex("¡La línea sería el espacio generado por $\\vec{w}$!", color=CustomColors.TRANSPARENTRED, font_size=30).next_to(v2, LEFT, buff=0.3)
        self.play(Write(span_w_label))
        self.next_slide()

        # # Add an explanation about the span of a single vector
        explanation_text = Tex(
            "El espacio generado por un solo vector no nulo en 2D es una línea que pasa por el origen.",
            color=CustomColors.DARK
        ).to_edge(DOWN).scale(0.6)
        self.play(Write(explanation_text))
        self.next_slide()
        self.wait(2)

        # # Clean up for the next part of the animation (if any)
        self.play(
            FadeOut(current_v2_animated),
            FadeOut(span_w_label),
            FadeOut(transform_title),
            #FadeOut(line_trace),
            FadeOut(explanation_text),
            #FadeOut(v2_label), # Fade out the label for w
            #FadeOut(v2) # Fade out the original w vector
        )
        self.next_slide()



        # span del otro vector 
        # Show w span
        self.play(
            FadeIn(v1),
            FadeIn(v1_label),
        )
        self.next_slide()

        transform_title = Tex("Haciendo lo mismo con el vector $\\vec{v}$", color=BLACK).scale(0.6)
        transform_title.move_to([0,3,0])
        self.play(
            Write(transform_title),
        )
        self.wait()
        self.next_slide()

        # Create a copy of v2 that will be animated to show scaling
        current_v1_animated = v1.copy().set_color(BLUE)

        # Attach a TracedPath to the end of the animating vector
        # The TracedPath will draw the path as the vector scales
        line_trace = TracedPath(
            current_v1_animated.get_end,
            stroke_color=BLUE,
            stroke_width=0.8 # Make the line a bit thicker
        )
        self.add(line_trace) # Add the trace to the scene

        # Animate the scaling of the vector from -3 to 3
        # Start the vector from the origin (scalar factor 0)
        # This makes the line grow outwards from the center
        self.play(
            Transform(current_v1_animated, Vector(v1.get_end() * 0.001, color=BLUE)),
            run_time=0.1 # Quick snap to origin
        )
        
        # Scale the vector smoothly from the origin to a positive and negative end
        # We'll animate it growing outwards from the center in two phases
        self.play(
            Transform(current_v1_animated, Vector(v1.get_end() * 6, color=BLUE)),
            run_time=2,
            rate_func=linear
        )
        self.play(
            Transform(current_v1_animated, Vector(v1.get_end() * -6, color=BLUE)),
            run_time=2,
            rate_func=linear
        )
        self.play(
            Transform(current_v1_animated, Vector(v1.get_end() * 0.001, color=BLUE)),
            run_time=1,
            rate_func=linear
        )

        self.wait(0.5)
        self.next_slide()



        # # --- Placeholder for the rest of your original script ---
        # # This is where the code for showing the span of two vectors would resume.
        # Re-introduce v1 and v2 for the next part (span of two vectors)
        # self.play(FadeIn(v1), FadeIn(v1_label), FadeIn(v2), FadeIn(v2_label))
        # self.next_slide()







        self.play(
            FadeOut(transform_title),
        )
        self.next_slide()



        title_two_vectors = Tex("Y ahora, haciendo una combinación lineal: $a\\vec{v} + b\\vec{w}$", color=CustomColors.DARK).to_edge(UP).scale(0.7)
        self.play(Write(title_two_vectors)) # Write the title on the screen
        self.next_slide() # Advance to the next slide/step

        # Define different scalar pairs for linear combinations
        scalars = [(1.5, 0.5), (0.7, 1.3), (-1, -0.8), (2, -0.5)]
        
        # Store a reference to the original vector objects to reset them later
        # We need to ensure that 'v1' and 'v2' are the Mobjects that will be transformed.
        # We will use their original coordinate values for calculations.
        
        for a, b in scalars:
            # 1. Create the scaled version of vector v1, starting from the origin.
            # This is a new Mobject that 'v1' will transform into.
            scaled_v1_target = Vector(v1_coords * a, color=BLUE)

            # 2. Create the scaled version of vector v2, starting from the origin.
            # This is a new Mobject that 'v2' will transform into.
            scaled_v2_target = Vector(v2_coords * b, color=CustomColors.RED)

            # Animate the scaling of both original vectors (v1 and v2)
            # They transform into their scaled versions, both originating from (0,0).
            self.play(
                FadeOut(v1_label), # Fade out the original labels
                FadeOut(v2_label),
                Transform(v1, scaled_v1_target), # v1 becomes scaled_v1_target
                Transform(v2, scaled_v2_target),  # v2 becomes scaled_v2_target
                run_time=1.0 # Shorter run time for this step
            )
            self.next_slide() # Advance to the next slide/step

            # 3. Animate the shifting of the scaled v2.
            # The current 'v2' (which is now scaled_v2_target) moves so its tail
            # is at the head of the current 'v1' (which is scaled_v1_target).
            self.play(
                v2.animate.shift(v1.get_end()), # Shift v2 by the end point of v1
                run_time=1.0 # Shorter run time for this step
            )
            self.next_slide() # Advance to the next slide/step

            # 4. Create the resultant vector from the origin to the end of the shifted v2.
            resultant_vector = Vector(v2.get_end(), color=CustomColors.DOTS)
            self.play(Create(resultant_vector)) # Animate the creation of the resultant vector
            self.next_slide() # Advance to the next slide/step
            
            # 5. Fade out the current linear combination and bring back original vectors/labels.
            # We use .become() to reset the Mobject 'v1' and 'v2' to their original state
            # before fading them in for the next iteration.
            self.play(
                FadeOut(v1), # Fade out the scaled v1
                FadeOut(v2), # Fade out the shifted scaled v2
                FadeOut(resultant_vector), # Fade out the resultant vector
                FadeIn(v1.become(Vector(np.array(v1_coords), color=BLUE))), # Reset v1 to original and fade in
                FadeIn(v2.become(Vector(np.array(v2_coords), color=CustomColors.RED))),   # Reset v2 to original and fade in
                FadeIn(v1_label), # Fade in original labels
                FadeIn(v2_label),

                run_time=0.5 # Quick fade out/in
            )
            self.next_slide() # Advance to the next slide/step

            

        self.play(FadeOut(title_two_vectors)) # Fade out the linear combination title
        self.next_slide() # Advance to the next slide/step

        # --- Span Section ---
        # Define the concept of span
        span_text = Tex("El espacio generado por dos vectores $\\vec{v} \, , \\vec{w}$ es el conjunto de todas las posibles combinaciones lineales de esos dos vectores", color=CustomColors.DARK).to_edge(UP).scale(0.7)
        self.play(Write(span_text)) # Write the span definition
        self.next_slide() # Advance to the next slide/step

        # Show the span filling the plane
        dots = VGroup() # Create a VGroup to hold all the dots
        
        # Ensure v1 and v2 are back to their original state for span calculation
        # It's safer to use the original coordinate arrays for span calculation
        # to avoid any lingering transformations on the Mobjects.
        
        # Generate a grid of points that represent various linear combinations
        for i in range(-20, 20):
            for j in range(-20, 20):
                a_val = i * 0.2 # Scalar 'a'
                b_val = j * 0.2 # Scalar 'b'
                
                # Ensure v1_coords and v2_coords are consistently 1D numpy arrays for calculations
                # This defends against potential shape issues if they somehow became 2D arrays (e.g., [[x,y,z]])
                v1_coords_calc = np.asarray(v1_coords).squeeze()
                v2_coords_calc = np.asarray(v2_coords).squeeze()

                # Calculate the point as a linear combination of the original vector coordinates
                point = v1_coords_calc * a_val + v2_coords_calc * b_val
                dots.add(Dot(point, radius=0.05, color=CustomColors.DOTS))
        # Animate the creation of the dots to show the span
        self.play(
            FadeOut(span_text), # Fade out the span definition text
            Create(dots, run_time=5, lag_ratio=0.01) # Create dots with a slight delay between them
        )
        self.next_slide() # Advance to the next slide/step
        self.wait(2) # Wait for 2 seconds

        # Conclude the scene
        conclusion = Tex("Para dos vectores linealmente independientes en 2D, el espacio generado es todo el plano en 2D.", color=CustomColors.DARK).to_edge(DOWN).scale(0.7)
        self.play(Write(conclusion)) # Write the conclusion
        self.next_slide() # Advance to the next slide/step
        self.wait(2) # Wait for 2 seconds

