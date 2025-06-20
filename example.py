from manim import *  # or: from manimlib import *

from manim_slides import Slide, ThreeDSlide


class ThreeDExample(ThreeDSlide):
    def construct(self):

        LIGHT_GREEN = (255, 255, 255)
        manim_color_object_LIGHT_GREEN = ManimColor.from_rgb(LIGHT_GREEN)
        self.camera.background_color = manim_color_object_LIGHT_GREEN

        axes_defaults = {
               "color": BLACK,
               "include_numbers": True,
           }

        axes = ThreeDAxes(axis_config=axes_defaults)
        circle = Circle(radius=3, color=BLACK)
        dot = Dot(color=RED)

        self.add(axes)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(GrowFromCenter(circle))
        self.begin_ambient_camera_rotation(rate=75 * DEGREES / 4)

        self.next_slide()

        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=4, rate_func=linear)
        self.next_slide()

        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(dot.animate.move_to(ORIGIN))
        self.next_slide()

        self.play(dot.animate.move_to(RIGHT * 3))
        self.next_slide()

        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()

        self.play(dot.animate.move_to(ORIGIN))
