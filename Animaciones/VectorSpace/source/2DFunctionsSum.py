from manim import *
from manim_slides import Slide # Import Slide for presentation features
import numpy as np
import sys
sys.path.append("../../")
from CustomColors import CustomColors




class SumOfTwoFunctions(Slide):
    def construct(self):
        self.camera.background_color = CustomColors.LIGHT
        
        # Setup the coordinate axes for function plotting
        axes = Axes(
            x_range=[-PI*2, PI*2, 1], # X-axis for function domain
            y_range=[-8, 8, 1],       # Y-axis for function range
            x_length=12,
            y_length=8,
            axis_config={"color": CustomColors.GREY_A},
            tips=False # No tips on function axes
        ).add_coordinates()
        self.add(axes)
        self.next_slide()

        self.introduce_functions(axes)
        self.show_point_by_point_sum(axes)
        self.conclude_functions_sum()

    def introduce_functions(self, axes):
        # Define the two functions
        def f(x):
            return np.sin(x) * 2 # A sine wave
        
        def g(x):
            return 0.5 * x # A linear function

        # Create the graphs of the functions
        graph_f = axes.plot(f, color=CustomColors.BLUE)
        graph_g = axes.plot(g, color=CustomColors.RED)

        # Create labels for the functions
        label_f = MathTex(r"f(x) = 2\sin(x)", color=CustomColors.BLUE).next_to(graph_f, UP, buff=0.5).shift(RIGHT*2)
        label_g = MathTex(r"g(x) = 0.5x", color=CustomColors.RED).next_to(graph_g, DOWN, buff=0.5).shift(LEFT*2)

        # Title for function introduction
        intro_title = MarkupText(
            f'Sumando <span fgcolor="{CustomColors.BLUE}">funciones</span> punto por punto',
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        intro_title.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(Write(intro_title))
        self.next_slide()
        self.play(Create(graph_f), Write(label_f))
        self.next_slide()
        self.play(Create(graph_g), Write(label_g))
        self.next_slide()

        self.f_func = f
        self.g_func = g
        self.graph_f = graph_f
        self.graph_g = graph_g
        self.label_f = label_f
        self.label_g = label_g
        self.intro_title = intro_title
        self.axes = axes

    def show_point_by_point_sum(self, axes):
        f, g = self.f_func, self.g_func
        graph_f, graph_g = self.graph_f, self.graph_g
        label_f, label_g = self.label_f, self.label_g
        intro_title = self.intro_title

        # Define the sum function h(x)
        def h(x):
            return f(x) + g(x)
        self.h_func = h

        # Create a title for the summation process
        sum_process_title = MarkupText(
            f'Visualizando la <span fgcolor="{CustomColors.YELLOW}">Suma</span>',
            color=CustomColors.DARK
        ).to_edge(UP).scale(0.8)
        sum_process_title.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(Transform(intro_title, sum_process_title))
        self.next_slide()

        # The x-value that will be animated
        x_val = ValueTracker(-PI*2)

        # A vertical line (probe) to mark the current x-value
        x_line = always_redraw(
            lambda: axes.get_vertical_line(axes.input_to_graph_point(x_val.get_value(), graph_f), color=CustomColors.GREY_A, stroke_width=1)
        )

        # Dots on the graphs f(x) and g(x)
        dot_f = always_redraw(
            lambda: Dot(axes.input_to_graph_point(x_val.get_value(), graph_f), color=CustomColors.BLUE)
        )
        dot_g = always_redraw(
            lambda: Dot(axes.input_to_graph_point(x_val.get_value(), graph_g), color=CustomColors.RED)
        )

        # The vertical segment representing g(x) added to f(x)
        # This shows the "summing" action
        g_height_line = always_redraw(
            lambda: Line(
                axes.input_to_graph_point(x_val.get_value(), graph_f), # Start at f(x)
                axes.input_to_graph_point(x_val.get_value(), graph_f) + UP * axes.c2p(0,g(x_val.get_value()),0)[1], # Add g(x) height
                color=CustomColors.GREEN, stroke_width=2
            )
        )

        # The resulting point on the sum function h(x)
        dot_h = always_redraw(
            lambda: Dot(axes.input_to_graph_point(x_val.get_value(), graph_f) + UP * axes.c2p(0,g(x_val.get_value()),0)[1], color=CustomColors.YELLOW)
        )

        # Trace for the sum function
        # This will draw the graph of h(x) as the dots are created
        path_h = TracedPath(dot_h.get_center, stroke_color=CustomColors.YELLOW, stroke_width=4)

        self.add(x_line, dot_f, dot_g, g_height_line, dot_h, path_h)
        self.play(x_val.animate.set_value(PI*2), run_time=6, rate_func=linear)
        self.wait(0.5)
        self.next_slide()

        # Fully draw the sum function graph
        graph_h = axes.plot(h, color=CustomColors.YELLOW)
        label_h = MathTex(r"h(x) = f(x) + g(x)", color=CustomColors.YELLOW).next_to(graph_h, DOWN, buff=0.5).shift(RIGHT*2)

        self.play(
            FadeOut(x_line), FadeOut(dot_f), FadeOut(dot_g), FadeOut(g_height_line), FadeOut(dot_h),
            Create(graph_h), Write(label_h),
            run_time=1.5
        )
        self.next_slide()
        self.wait(1)

        self.graph_h = graph_h
        self.label_h = label_h

    def conclude_functions_sum(self):
        # Final conclusion text
        final_text = Tex(
            "Sumar funciones es añadir sus valores de salida (Y) para cada valor de entrada (X).",
            color=CustomColors.DARK
        ).scale(0.7).to_edge(DOWN)
        final_text.add_background_rectangle(color=CustomColors.LIGHT, opacity=0.8)

        self.play(FadeOut(self.intro_title)) # This is the transformed title
        self.play(Write(final_text))
        self.next_slide()
        self.wait(1)
        self.play(
            FadeOut(self.graph_f), FadeOut(self.label_f),
            FadeOut(self.graph_g), FadeOut(self.label_g),
            FadeOut(self.graph_h), FadeOut(self.label_h),
            FadeOut(final_text)
        )
        self.next_slide()
