from manim import *
from manim_slides import Slide


class NonLinear(Slide):
    def construct(self):
        self.camera.background_color = ManimColor("#FFFFFF")
        title = Tex(r"Un ejemplo de una transformación no lineal", color=BLACK)
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title),
        )
        self.wait()

        transform_title = Tex("Imaginemos que la transformación no lineal sucede en el plano", color=BLACK)
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
        )
        self.wait()

        grid = NumberPlane(background_line_style={
                "stroke_width": 5,
                "stroke_opacity": 0.6
            })
        grid_title = Tex("Y ahora...", font_size=68, color=BLACK)
        grid_title.move_to(transform_title)
        self.next_slide()

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()
        self.next_slide()
        

        grid_transform_title = Tex(
            r"Este fue el efecto de aplicar una \\ transformación no lineal al plano", color=BLACK
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()