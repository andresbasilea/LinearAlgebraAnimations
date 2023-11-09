from manim import *
from manim_editor import PresentationSectionType

vec_a_color = RED
vec_b_color = YELLOW
vec_c_color = BLUE

x_color = PINK
y_color = ORANGE



class Intro(Scene):
	def construct(self):
		self.camera.background_color = "#F5F5DC"
		logo_green = "#35A29F"
		logo_blue = "#6528F7"
		logo_red = "#900C3F"
		logo_black = "#343434"
		ds_m = MathTex(r"\mathbb{ÁL}", fill_color=logo_black).scale(7)
		ds_m.shift(2.25 * LEFT + 1.5 * UP)
		circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
		square = Square(color=logo_blue, fill_opacity=1).shift(UP)
		triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
		logo = VGroup(triangle, square, circle, ds_m)  # order matters
		logo.move_to(ORIGIN)
		self.play(DrawBorderThenFill(logo))
		#self.add(logo)
		self.wait(2)

		text = Tex(r"Facultad de Ingeniería, UNAM \\\ ", "Ing. Andrés Basile Álvarez" )
		text.set_color(BLACK)
		text.shift(2.65 * DOWN)
		self.play(Write(text))
		


		facultadIngenieria = ImageMobject("presentationImages/escudo_fi_color.png")
		facultadIngenieria.scale(0.5)
		facultadIngenieria.to_edge(UP)
		self.play(FadeIn(facultadIngenieria))

		self.wait(5)


class Tema(Scene):
	def construct(self):
		self.camera.background_color = "#F5F5DC"
		text = Tex(r"\textbf{4. Espacios con producto interno}")
		text.shift(2 * UP)
		text2 = Tex(r"4.3 Conjuntos ortogonales y ortonormales.", " Independencia lineal de un conjunto ortogonal de vectores no nulos.", " Coordenadas de un vector respecto a una base ortogonal y respecto a una base ortonormal.", " Proceso de ortogonalización de Gram-Schmidt" )
		
		#text.shift(2.65 * DOWN)
		textgroup = VGroup(text, text2)
		textgroup.set_color(BLACK)
		textgroup.move_to(ORIGIN)
		textgroup.scale(0.8)
		self.play(FadeIn(textgroup))
		self.wait(5)


class DefinicionProductoInterno(Scene):
	def construct(self):

		title = Tex(r"Producto Interno: Definición")
		title.shift(2 * UP)
		text = Tex(r"\justifying {Sea \textit{V} un espacio vectorial sobre un campo de definición complejo. Un \textbf{producto interno} es una función de \textit{VxV} en $\mathbb{C}$ que asocia a cada pareja de vectores $\vec{u}$ y $\vec{v}$ de \textit{V} un escalar $(\vec{u} | \vec{v})$ $\in \mathbb{C}$, llamado el producto interno de  $\vec{u}$ y $\vec{v}$.}")
		text.scale(0.6)
		text[0].set_color(WHITE)
		textgroup = VGroup(title, text)
		self.play(Write(textgroup))

		# innerProductImage = ImageMobject("presentationImages/inner_product.png")
		# innerProductImage.scale(0.3)
		# innerProductImage.to_edge(DOWN)
		# self.add(innerProductImage)

		self.wait(5)




class ConjuntosOrtogonalesOrtonormales(Scene):
	def construct(self):


		self.next_section("B", PresentationSectionType.NORMAL)
		title = Tex(r"¿A qué nos referimos con conjuntos \textcolor{yellow}{ortogonales} y \textcolor{yellow}{ortonormales}?").scale(1)
		title[0][29:40].set_color(YELLOW)
		title[0][41:53].set_color(YELLOW)
		self.play(Write(title))	
		self.wait(5)
		self.next_section("B.0", PresentationSectionType.NORMAL)


		self.play(Uncreate(title))
		text0 = Tex(r"Conjuntos Ortogonales").scale(1)
		self.play(Write(title))	


		text1 = Tex(r"Sea \textit{V} un espacio vectorial con producto interno y sea $A = \{\vec{v_1}, \vec{v_2}, ..., \vec{v_n}\}$ un subconjunto de \textit{V}. Se dice que \textit{A} es un conjunto ortogonal cuando: \[ (\vec{v_i} | \vec{v_j}) = 0 \quad ; \quad \forall \quad i \neq j  \]" ).scale(0.6)
		text1.scale(0.9)
		text1.set_color(WHITE)

		# Animate the first text to move to the top
		self.play(
			text0.animate.shift(3 * UP),
			FadeIn(text1)
			
		)

		self.wait(5)
		

		self.next_section("B.1", PresentationSectionType.NORMAL)
		self.play(Uncreate(text0))
		self.play(Uncreate(text1))

		plane = NumberPlane(x_range=(-5,5), y_range=(-2.2,2.2), stroke_color= LIGHT_GREY, stroke_opacity=0.6)
		plane.add_coordinates()
		self.play(Create(plane, run_time=3))

		vector1 = Vector([0,2], color=RED)
		vector2 = Vector([2,0], color=BLUE)
		label1 = MathTex(r"\vec{v_1}", color=RED, stroke_width=2).next_to(vector1, UP)
		group1 = VGroup(vector1, label1)
		label2 = MathTex(r"\vec{v_2}", color=BLUE, stroke_width=2).next_to(vector2, RIGHT)
		group2 = VGroup(vector2, label2)

		self.play(Create(group1, run_time=2), Create(group2, run_time=2))
		# Demonstrate orthogonality
		self.wait(5)

		self.next_section("B.2", PresentationSectionType.NORMAL)
		text2 = Tex(r"Si además cada vector del conjunto \textit{A} tiene norma igual a uno, se le llama \textbf{conjunto ortonormal}. ")
		text2.scale(0.7)
		text2.set_color(WHITE)
		text3 = Tex(r"Conjuntos Ortonormales").scale(1)

		self.play(
			text3.animate.shift(3 * UP),
			FadeIn(text2),
			text2.animate.shift(3 * DOWN)
			)

		unit_vector1 = Vector([0,1], color=RED)
		unit_vector2 = Vector([1,0], color=BLUE)

		# Transform the vectors to unit vectors
		self.play(
			Transform(vector1, unit_vector1),
			Transform(vector2, unit_vector2),
		)

		# Change labels to represent unit vectors
		label1_new = MathTex(r"\frac{\vec{v_1}}{||\vec{v_1}||}", color=RED, stroke_width=2).next_to(unit_vector1, UP).shift(0.05*UP)
		label2_new = MathTex(r"\frac{\vec{v_2}}{||\vec{v_2}||}", color=BLUE, stroke_width=2).next_to(unit_vector2, RIGHT).shift(0.05*RIGHT)

		self.play(
			Transform(label1, label1_new),
			Transform(label2, label2_new),
		)

		self.wait(3)





class MostrarBaseOrtogonal(ThreeDScene):
	def construct(self):
		# Create a 3D coordinate system
		axes = ThreeDAxes()
		self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

		# Define the directions of the custom orthonormal basis vectors
		u_direction = [1, 1, 0]  # Replace with your desired direction
		v_direction = [-1, 1, 0]  # Replace with your desired direction
		w_direction = [0, 0, 1]  # Replace with your desired direction

		# Create the custom orthonormal basis vectors
		u_hat = Arrow3D(ORIGIN, u_direction, color=RED)
		v_hat = Arrow3D(ORIGIN, v_direction, color=GREEN)
		w_hat = Arrow3D(ORIGIN, w_direction, color=BLUE)

		# Add labels for the custom vectors and coordinates
		u_label = MathTex(r"\hat{u}", color=RED).next_to(u_hat, RIGHT)
		v_label = MathTex(r"\hat{v}", color=GREEN).next_to(v_hat, UP)
		w_label = MathTex(r"\hat{w}", color=BLUE).next_to(w_hat, OUT)

		u_coords = MathTex(r"\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}", color=RED).next_to(u_hat, DOWN)
		v_coords = MathTex(r"\begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}", color=GREEN).next_to(v_hat, DOWN)
		w_coords = MathTex(r"\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}", color=BLUE).next_to(w_hat, DOWN)

		# Display the custom orthonormal basis and coordinates
		self.play(Create(axes))
		self.play(Create(u_hat), Create(v_hat), Create(w_hat))
		self.play(Create(u_label), Create(v_label), Create(w_label))
		self.play(Create(u_coords), Create(v_coords), Create(w_coords))

		# Camera animation: Move around the z-axis
		self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
		self.begin_ambient_camera_rotation(rate=0.2)  # Rotate the camera
		self.wait(15)  # Wait for the camera animation
		self.stop_ambient_camera_rotation()  # Stop camera rotation
		self.wait(4)





class CoordenadasBaseOrtogonal(Scene):
	def construct(self):
		self.next_section("A", PresentationSectionType.NORMAL)
		#title = Tex(r"Coordenadas de un vector con respecto a una base ortogonal/ortonormal").scale(1)

		# .set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color})
		# Title
		title = Tex("Coordenadas", " de un", " vector", " con respecto a una", " base ortogonal/ortonormal", color=WHITE).scale(0.8)\
			.set_color_by_tex_to_color_map({"Coordenadas": YELLOW, "base ortogonal/ortonormal": YELLOW})
		title.to_edge(UP)
		self.play(Write(title))


		#self.next_section("A.1", PresentationSectionType.NORMAL)
		text0 = Tex(r"\justifying {Sea \textit{V} un espacio vectorial con producto interno y sea} \\\ \\\ ",
			r"\justifying {$B = \{\vec{v_1}, \vec{v_2}, ..., \vec{v_n}\}$} \\\ \\\ ",
			r"\justifying {una base ortogonal de \textit{V}. Si $\vec{a} \in V$ y se tiene que:} \\\ \\\ ",
			r"\justifying {$\vec{a} = \{\alpha_1 \vec{v_1} + \alpha_2 \vec{v_2} + ... + \alpha_n \vec{v_n} \}$ }\\\ \\\ ",
			r"\justifying {entonces los escalares $\alpha_i$ vienen dados por la expresión: }\\\ \\\ ", 
			r"\justifying {$\alpha_i = \frac{(\vec{a} | \vec{v_i})}{(\vec{v_i} | \vec{v_i})} $ }"\
		).scale(0.7)
		self.play(Write(text0))
		self.wait(3)


		self.next_section("A.2", PresentationSectionType.NORMAL)

		textgroupvanish = VGroup(text0[0], text0[2], text0[4])
		self.play(Uncreate(textgroupvanish), run_time=1)

		text_stroke_width = 1.8
		self.play(text0[1].animate.shift(0.1*DOWN, 0.2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))
		self.play(text0[3].animate.shift(0.8*UP, 0.2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))
		self.play(text0[5].animate.shift(1.7*UP, 0.2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width= text_stroke_width))
		
		self.play(Uncreate(title), run_time=1)
		textgroup = VGroup(text0[1], text0[3], text0[5])
		self.play(textgroup.animate.to_corner(UL))
		textgroup.add_background_rectangle()
		
		self.next_section("A.3", PresentationSectionType.NORMAL)
		text1 = Tex(r"\justifying {Si los vectores de \textit{B} fueran vectores unitarios, } ",
					r"\justifying {es decir, si \textit{B} fuese una base ortonormal, entonces las coordenadas del vector $\vec{a}$ }"
					r"\justifying {respecto a la base \textit{B} vendrían dadas por: } \\\ ",
					r"\begin{center} $\alpha_i = (\vec{a} | \vec{v_i})$ \end{center} " 
					).scale(0.7)
		self.play(Write(text1))
		self.wait(5)


		self.next_section("A.4", PresentationSectionType.NORMAL)
		self.play(Uncreate(text1), run_time=1)
		plane = NumberPlane(stroke_color=LIGHT_GREY, stroke_opacity=0.8, axis_config={
									 "stroke_color": WHITE
										},)
		plane.add_coordinates()
		self.play(Create(plane))
		self.bring_to_front(text0)


		a_vector_coords = (2,3)
		# Create the vector with the specified coordinates
		vector = Vector(a_vector_coords, color=RED, stroke_width=4)
		self.play(Create(vector), run_time=2)
		label_vector = Tex(r"$\vec{a}$").next_to(vector, RIGHT).shift(LEFT*0.3)
		label_coords = MathTex(f"({a_vector_coords[0]}, {a_vector_coords[1]})", color=WHITE, stroke_width=1).next_to(vector, RIGHT).shift(0.2*RIGHT)
		# Add labels for the coordinates
		self.play(Create(label_coords))
		self.play(Create(label_vector))
		self.wait(1)

		
		# Define the coordinates for the orthonormal basis vectors
		B_basis = (1, -1), (1, 1)

		# Create orthonormal basis vectors
		orthogonal_vector1 = Vector(B_basis[0], color=GREEN, stroke_width=4)
		orthogonal_vector2 = Vector(B_basis[1], color=BLUE, stroke_width=4)

		# Add orthonormal basis vectors to the scene
		self.play(Create(orthogonal_vector1), Create(orthogonal_vector2))

		# Add labels for the orthonormal basis vectors
		label_orthogonal1 = Tex(r"$\vec{v_1}$", color=GREEN, stroke_width=1).next_to(orthogonal_vector1, LEFT).shift(RIGHT*2)
		label_orthogonal2 = Tex(r"$\vec{v_2}$", color=BLUE, stroke_width=1).next_to(orthogonal_vector2, RIGHT)

		self.play(Create(label_orthogonal1), Create(label_orthogonal2))


		v1_line = Line(plane.get_origin(), orthogonal_vector1.get_end(), color=GREEN)
		v2_line = Line(plane.get_origin(), orthogonal_vector2.get_end(), color=BLUE)
		v1_line.set_length(11)
		v2_line.set_length(11)
		self.play(Create(v1_line))
		self.play(Create(v2_line))
		dashed_a_v1 = DashedLine([2,3,0], [-1/2, 1/2,0])
		projection_a_v1 = Line([0,0,0], [-1/2, 1/2,0], color=RED, stroke_width=7)
		self.play(Create(dashed_a_v1), Create(projection_a_v1), run_time=2)
		

		self.next_section("A.5")
		stuff = VGroup(dashed_a_v1, projection_a_v1, plane, v1_line, v2_line, vector, label_orthogonal1, label_orthogonal2,orthogonal_vector1, orthogonal_vector2, label_vector, label_coords)
		stuff.generate_target()
		stuff.target.shift(3*RIGHT).scale(0.65)
		self.add(stuff)
		self.play(MoveToTarget(stuff), run_time=2)
		self.bring_to_front(projection_a_v1)



		self.next_section("A.6")
		text2 = Tex(r" \justifying{Coordenadas del vector $\vec{a}$ en la base B:} \\\ \newline ",
					r" \justifying{$(2,3) = \alpha_1 (1, -1) + \alpha_2 (1, 1)$ }\\\ \newline",
					r" \justifying{$\alpha_1 = \frac{(2,3)|(1,-1)}{(1, -1) | (1, -1)}$ }\\\ \newline",
					r" \justifying{$\alpha_1 = \frac{-1}{2}$ }\\\ \newline",
					r" \justifying{$\alpha_2 = \frac{5}{2}$ }\\\ \newline",
					r" \justifying{$[\vec{a}]_B =  [\frac{-1}{2}, \frac{5}{2}]$} \\\ \newline"

			).set_stroke(width=1.3)


		textgroup2 = VGroup(text2)
		textgroup2.scale(0.6)
		textgroup2.to_corner(UL)
		textgroup2.arrange(DOWN, center=False, aligned_edge=LEFT)
		textgroup2.shift(DOWN*2.5)
		self.play(Write(textgroup2))

		self.next_section("A.7")
		self.play(Indicate(text2[2]), Indicate(text2[3]))
		self.wait(1)
		self.play(Indicate(projection_a_v1))

		# textgroup2 = VGroup(text2[0], text2[1])
		# textgroup2.to_edge(LEFT)
		# #textgroup2.set_width(5)
		# textgroup2.next_to(textgroup, DOWN)
		# textgroup2.arrange(DOWN, aligned_edge=LEFT, center=False)
		# #textgroup2.shift(1*RIGHT)
		# textgroup2.scale(0.7)
		# # backgroundRectangle = BackgroundRectangle(textgroup2, color=BLACK)
		# #textgroup2.set_width(5)
		# #self.add(backgroundRectangle)
		# self.play(Write(textgroup2))

		# textgroup3 = VGroup(text2[2], text2[3])
		# textgroup3.next_to(textgroup2, DOWN)
		# textgroup3.to_edge(LEFT)
		# textgroup3.arrange(DOWN, aligned_edge=LEFT, center=False)
		# textgroup3.shift(1*DOWN)
		# textgroup3.scale(0.7)
		# # backgroundRectangle2 = BackgroundRectangle(textgroup3, color=BLACK)


		


		# #textgroup3.set_width(5)
		# #proj_label = Tex(r"$\frac{-1}{2}$")
		# #proj_label.next_to(projection_a_v1, LEFT)



		# self.play(Write(textgroup3))
		# self.wait(2)

		# self.next_section("A.6")
		# self.play(Indicate(textgroup3))
		# self.play(Indicate(projection_a_v1))
		# self.wait(1)
		# textgroup4 = VGroup(text2[4], text2[5])
		# textgroup4.next_to(textgroup3, DOWN)
		# textgroup4.to_edge(LEFT)
		# textgroup4.arrange(DOWN, aligned_edge=LEFT, center=False)
		# # textgroup4.shift()
		# textgroup4.scale(0.7)
		# # backgroundRectangle3 = BackgroundRectangle(textgroup4, color=BLACK)
		# #textgroup4.set_width(5)
		# self.play(Write(textgroup4))
		# self.wait(2)



		# # Calculate the coordinates of the vector in the orthonormal basis
		# dot_product_i = np.dot(coords, orthonormal_coords[0])
		# dot_product_j = np.dot(coords, orthonormal_coords[1])
		# # Create labels for the coordinates in the orthonormal basis
		# label_coords_orthonormal = MathTex(f"({dot_product_i}, {dot_product_j})", color=WHITE, stroke_width=1).next_to(orthonormal_vector2, RIGHT).shift(0.15*RIGHT)

		#self.play(Transform(label_coords, label_coords_orthonormal))

		self.wait(1)



# class OOP(Scene):
#     def construct(self):
#         # Create the original vector
#         vector = np.array([3, 2])
#         original_vector = Vector(vector, color=RED)

#         # Create the orthogonal basis vectors
#         orthogonal_basis = [np.array([1, 0]), np.array([0, 1])]
#         orthogonal_vectors = [Vector(v, color=BLUE) for v in orthogonal_basis]

#         # Create labels for the orthogonal basis
#         orthogonal_labels = [MathTex(r"\mathbf{v}_1"), MathTex(r"\mathbf{v}_2")]
#         for label, vector in zip(orthogonal_labels, orthogonal_vectors):
#             label.next_to(vector, RIGHT)
#             label.set_color(BLUE)

#         # Create the orthonormal basis vectors
#         orthonormal_basis = [v / np.linalg.norm(v) for v in orthogonal_basis]
#         orthonormal_vectors = [Vector(v, color=GREEN) for v in orthonormal_basis]

#         # Create labels for the orthonormal basis
#         orthonormal_labels = [MathTex(r"\mathbf{u}_1"), MathTex(r"\mathbf{u}_2")]
#         for label, vector in zip(orthonormal_labels, orthonormal_vectors):
#             label.next_to(vector, RIGHT)
#             label.set_color(GREEN)

#         # Display the original vector and the orthogonal basis
#         self.play(Create(original_vector))
#         self.wait(1)
#         self.play(Create(*orthogonal_vectors))
#         self.play(*[Write(label) for label in orthogonal_labels])
#         self.wait(1)

#         # Transition to the orthonormal basis
#         self.play(FadeOut(*orthogonal_labels))
#         self.play(Transform(original_vector, orthonormal_vectors[0]))
#         self.play(Create(orthonormal_vectors[1]))
#         self.play(*[Write(label) for label in orthonormal_labels])
#         self.wait(1)

#         # Show the coordinates in both bases
#         original_coordinates = MathTex(r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=RED)
#         orthogonal_coordinates = MathTex(r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=BLUE)
#         orthonormal_coordinates = MathTex(r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=GREEN)

#         original_coordinates.next_to(original_vector, UP)
#         orthogonal_coordinates.next_to(orthogonal_vectors[1], RIGHT)
#         orthonormal_coordinates.next_to(orthonormal_vectors[1], RIGHT)

#         self.play(Write(original_coordinates))
#         self.wait(1)
#         self.play(Write(orthogonal_coordinates))
#         self.wait(1)
#         self.play(Write(orthonormal_coordinates))
#         self.wait(2)



# class CoordenadasBaseOrtogonal(Scene):
# 	def construct(self):
		


# 		self.next_section("A.2", PresentationSectionType.NORMAL)

# 		textgroupvanish = VGroup(text0[0], text0[2], text0[4])
# 		self.play(Uncreate(textgroupvanish), run_time=1)

# 		text_stroke_width = 1.8
# 		self.play(text0[1].animate.shift(0.1*DOWN, 0.2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))
# 		self.play(text0[3].animate.shift(0.8*UP, 0.2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))
# 		self.play(text0[5].animate.shift(1.7*UP, 0.2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width= text_stroke_width))
		
# 		self.play(Uncreate(title), run_time=1)
# 		textgroup = VGroup(text0[1], text0[3], text0[5])
# 		self.play(textgroup.animate.to_corner(UL))
		


# 		self.next_section("A.3", PresentationSectionType.NORMAL)
# 		plane = NumberPlane(stroke_color=LIGHT_GREY, stroke_opacity=0.8, axis_config={
#                                      "stroke_color": WHITE
#                                         },)
# 		plane.add_coordinates()
# 		self.play(Create(plane))
# 		self.bring_to_front(text0)







class GramSchmidtOrthogonalization(Scene):
	def construct(self):

		self.next_section("ExplicacionProceso", PresentationSectionType.NORMAL)
		#title = Tex(r"Coordenadas de un vector con respecto a una base ortogonal/ortonormal").scale(1)

		# .set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color})
		# Title
		title = Tex("Proceso de", " ortogonalización", " de Gram-Schmidt", color=WHITE).scale(0.8)\
			.set_color_by_tex_to_color_map({"ortogonalización": YELLOW, "Gram-Schmidt": YELLOW})
		title.to_edge(UP)
		title.shift(0.05 * UP)
		self.play(Write(title))


		#self.next_section("A.1", PresentationSectionType.NORMAL)
		text0 = Tex(r"\justifying {Sea \textit{V} un espacio vectorial con producto interno y sea} \\\ \\\ ",
			r"\justifying {$B = \{\vec{v_1}, \vec{v_2}, \ldots, \vec{v_n}\}$ } ",
			r"\justifying {una base cualquiera de \textit{V}.} \\\ \\\ ",
			r"\justifying {Si ${B_{ort}} = \{ \vec{w_1}, \vec{w_2}, \ldots, \vec{w_n} \} $}\\\ \\\ ",
			r"\justifying {es una base ortogonal del espacio \textit{V}, entonces sus elementos vienen dados por: }\\\ \\\ ", 
			r"\justifying {$\vec{w_1} = \vec{v_1}$ }\\\ ",
			r"\justifying {$\vec{w_2} = \vec{v_2} - \frac{(\vec{v_2} | \vec{w_1})}{(\vec{w_1} | \vec{w_1})} \vec{w_1} $ } \\\ ",
			r"\justifying {.} \\\ ",
			r"\justifying {.} \\\ ",
			r"\justifying {.} \\\ ",
			r"\justifying {$ \vec{w_i} = \vec{v_2} - \Sigma_{k=1}^i-1 \frac{(\vec{v_i} | \vec{w_k})}{(\vec{w_k} | \vec{w_k})} \vec{w_k} $ } \\\ \\\ ",
			r"\justifying {para \textit{i} = 1, 2, ..., n } \\\ "
		).scale(0.5)
		self.play(Write(text0))
		self.wait(3)

		self.play(Indicate(text0[1]), Indicate(text0[3]), Indicate(text0[10]))
		self.wait(4)

		# self.next_section("ExplicacionProceso2", PresentationSectionType.NORMAL)
		# textgroupvanish = VGroup(text0[0], text0[2], text0[4], text0[5], text0[6], text0[7], text0[8], text0[9], text0[11])
		# self.play(Uncreate(textgroupvanish), run_time=1)

		# text_stroke_width = 1.3
		# self.play(text0[1].animate.shift(0.1*DOWN, 2*LEFT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))
		# self.play(text0[3].animate.next_to(text0[1], DOWN).shift(0.3*RIGHT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))
		# self.play(text0[10].animate.next_to(text0[3], DOWN).shift(0.1*RIGHT).set_color(YELLOW).set_weight(BOLD).set_stroke(width = text_stroke_width))

		# self.play(Uncreate(title), run_time=1)
		# textgroup = VGroup(text0[1], text0[3], text0[10])
		# self.play(textgroup.animate.to_corner(UL).scale(0.8))
		# textgroup.add_background_rectangle()




		# self.next_section("AnimacionProceso", PresentationSectionType.NORMAL)


		# plane_move = 4
		# plane = NumberPlane(x_range=(-4,4), y_range=(-5, 5), stroke_color=LIGHT_GREY, stroke_opacity=0.8, axis_config={
		# 							 "stroke_color": WHITE
		# 								}).move_to(RIGHT*plane_move)
		# plane.add_coordinates()
		# self.play(Create(plane))
		# self.bring_to_front(text0)

		# coords = (2, 3)

		# # Create the vector with the specified coordinates
		# vector = Vector(coords, color=RED, stroke_width=4).move_to(RIGHT*plane_move)

		# # Animate the vector "b1" transforming into the vector
		# self.play(ReplacementTransform(text0[1][3:6], vector))

		# # Display the final result
		# self.wait(2)




class EjemploGramSchmidt(ThreeDScene):
	def construct(self):

		self.next_section("PlanteamientoProblema", PresentationSectionType.NORMAL)
		#title = Tex(r"Coordenadas de un vector con respecto a una base ortogonal/ortonormal").scale(1)


		#self.next_section("A.1", PresentationSectionType.NORMAL)
		text0 = Tex(r"\justifying {Obtener una base ortonormal del espacio V generado por los vectores: } \\\ ",
			r" $\vec{v_1} = (1, 0, -1)$  \newline",
			r" $\vec{v_2} = (-2, 1, 1)$  \newline",
			r" $\vec{v_3} = (-1, 1, 0)$  \newline",
			r"\justifying {con las operaciones usuales de adición, multiplicación por un escalar y producto interno en $R^3$} \\\ \\\ ",

		).scale(0.8)
		# .set_color_by_tex_to_color_map({"(1,0,-1)": YELLOW, "(-2,1,1)": YELLOW, "(-1,-1,0)": YELLOW}) 
		self.play(Write(text0))
		self.wait(3)


		self.next_section("ComienzaGramSchmidt")
		text_stroke_width = 1.3
		self.play(Uncreate(text0[0]), run_time=1)
		self.play(Uncreate(text0[4]), run_time=1)
		text0[1].set_color(RED)
		text0[2].set_color(BLUE)
		text0[3].set_color(GREEN)
		textgroup = VGroup(text0[1], text0[2], text0[3])
		#textgroup.arrange(aligned_edge=LEFT, center=False)
		textgroup.add_background_rectangle()


		text1 = Tex(r"\justifying {Primero obtendremos un generador ortogonal de dicho espacio, \newline mediante el proceso de Gram-Schmidt} \\\ ")
		text1_4 = Tex(r" $\vec{w_1} = \vec{v_1} = (1, 0, -1)$ ")
		text1_5 = Tex(r" $\vec{w_2} = \vec{v_2} - \frac{(\vec{v_2} | \vec{w_1})}{(\vec{w_1} | \vec{w_1})} \vec{w_1} $ \\\ ")
		text1_5_2=Tex(r" $= (-2, 1, 1) - \frac{-3}{2} (1, 0, -1)$ \newline $= (-\frac{1}{2}, 1, \frac{-1}{2})$")
		text1_6 = Tex(r" $\vec{w_3} = \vec{v_3} - \frac{(\vec{v_3} | \vec{w_1})}{(\vec{w_1} | \vec{w_1})} \vec{w_1} - \frac{(\vec{v_3} | \vec{w_2})}{(\vec{w_2} | \vec{w_2})} \vec{w_2} $\newline")
		text1_7 = Tex(r" $ = (-1, 1, 0) - \frac{-1}{2} (1, 0, -1) - \frac{\frac{-3}{2}}{\frac{-3}{2}} (\frac{-1}{2}, 1, \frac{-1}{2}) = (0, 0, 0) $")
		text1_8 = Tex(r"\justifying {entonces: $G_0 = \{ (-1, 0, -1), (\frac{-1}{2}, 1, \frac{-1}{2}), (0, 0, 0) \}$} \\\ \\\ ")
		text1_9	= Tex(r"\justifying {es un generador ortogonal de \textit{V} y el conjunto} \\\ ")
		text1_10= Tex(r"$ B = \{ (1, 0, -1), (\frac{-1}{2}, 1, \frac{-1}{2}) \} $")
		text1_11= Tex(r" es una base ortogonal de dicho espacio. ")


		text1_12 = Tex(r"\justifying {Para obtener una base ortonormal calculamos:} \\\ ")
		text1_13 = Tex(r" $||\vec{w_1}|| = \sqrt{(\vec{w_1}|\vec{w_1})} = \sqrt{2}$ \\\ ")
		text1_14 = Tex(r" $||\vec{w_2}|| = \sqrt{(\vec{w_2}|\vec{w_2})} = \sqrt{\frac{3}{2}} $ \\\ ")
		text1_15 = Tex(r" $B = \{ (\frac{1}{\sqrt{2}}, 0, \frac{-1}{\sqrt{2}}), (\frac{-1}{\sqrt{6}}, \sqrt{\frac{2}{3}}, \frac{-1}{\sqrt{6}}) \} $ \\\ ")
		text1_16 = Tex(r" es una base ortonormal de V")

		text_w1 = Tex(r"$\vec{w1} = (1, 0, -1)$")
		text_w2 = Tex(r"$\vec{w2} = (\frac{-1}{2}, 1, \frac{-1}{2})$")
		text_w3 = Tex(r"$\vec{w3} = (0, 0, 0)$")
		text_normw1 = Tex(r"$\vec{w1} = (\frac{1}{\sqrt{2}}, 0, \frac{-1}{\sqrt{2}})$")
		text_normw2 = Tex(r"$\vec{w2} = (\frac{-1}{\sqrt{6}}, \sqrt{\frac{2}{3}}, \frac{-1}{\sqrt{6}})$")


		axes = ThreeDAxes()
		self.play(textgroup.animate.to_corner(UL))
		self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
		labx = axes.get_x_axis_label(Tex("$x$"))
		laby = axes.get_y_axis_label(Tex("$y$"))
		self.add_fixed_in_frame_mobjects(textgroup)
		self.play(FadeIn(axes))
		self.add(labx, laby)

		###############
		#definitions#
		###############

		origin = [0,0,0]
		v1 = [1,0,-1]
		v2 = [-2,1,1]
		v3 = [-1,1,0]

		vec_v1 = Arrow3D(
			start=origin,
			end=v1,
			resolution=20, 
			thickness = 0.05, 
			color=RED
		)

		vec_v2 = Arrow3D(
			start=origin,
			end=v2,
			resolution=20,
			thickness = 0.05,
			color=BLUE
		)

		vec_v3 = Arrow3D(
			start=origin,
			end=v3,
			resolution=20,
			thickness = 0.05,
			color=GREEN
		)


		span_surface = ParametricSurface(
			lambda u, v: u * vec_v1.get_end() + v * vec_v2.get_end() + (1 - u - v) * vec_v3.get_end(),
			u_range=(-10, 10),
			v_range=(-10, 10),
			color=WHITE,
			checkerboard_colors=[WHITE, GREY_B],
			fill_opacity=0.3
		)

		START_TEXT = [-2,1.5,0]
		STROKE_WIDTH = 3.8
		TEXT_SCALE = 0.7
		MATH_TEXT_SCALE = 0.9


		# obtain w2
		direction_w1 = Line(origin, vec_v1.get_end(), color=RED)
		direction_w1.set_length(20)
		dashed_v2_w1 = DashedLine(vec_v2.get_end(), [-3/2, 0, 3/2])
		#rightangle_v2_w1 = RightAngle(dashed_v2_w1, direction_w1)
		vec_v2_minus_w1 = Arrow3D(
			start=[-3/2,0,3/2],
			end=vec_v2.get_end(),
			resolution=20,
			thickness = 0.04,
			color=PURPLE
		)
		vec_w2 = Arrow3D(
			start=origin,
			end=[-1/2, 1, -1/2],
			resolution=20,
			thickness = 0.04,
			color=PURPLE
			)


		# obtain w3
		direction_w2 = Line(origin, [-1/2, 1, -1/2], color=PURPLE)
		direction_w2.set_length(20)
		dashed_v3_w2 = DashedLine(vec_v3.get_end(), [-1/2, 1, -1/2])
		dashed_v3_w1 = DashedLine(vec_v3.get_end(), [-1/2, 0, 1/2])

		vec_v3_w2 = Arrow3D(
			start = origin,
			end = [-1/2, 1, -1/2],
			resolution=20,
			thickness=0.04,
			color=YELLOW
			)
		vec_v3_w1 = Arrow3D(
			start = origin,
			end = [-1/2, 0, 1/2],
			resolution=20,
			thickness=0.04,
			color=YELLOW
			)


		sum_vec_v3_w2_and_v3_w1 = Arrow3D(
			start = origin,
			end = [-1,1,0],
			resolution = 20,
			thickness = 0.04,
			color=YELLOW
			)


		vec_v3_minus_w1_w2 = Sphere(center=origin, radius=0.05, color=PURPLE)


		self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
		self.begin_ambient_camera_rotation(rate=0.08)  # Rotate the camera
		
		self.play(Create(vec_v1), Create(vec_v2), Create(vec_v3))

		self.next_section("MostrarEspacioGenerado")

		# self.play(Create(span_surface))
		# self.wait(8)

		# self.play(Uncreate(span_surface))


		stuff = VGroup(axes, labx, laby, vec_v1, vec_v2, vec_v3, span_surface, direction_w1, direction_w2, dashed_v2_w1, \
					   vec_v2_minus_w1, vec_w2, dashed_v3_w1, dashed_v3_w2, vec_v3_w2, vec_v3_w1, sum_vec_v3_w2_and_v3_w1,\
					   vec_v3_minus_w1_w2
			)

		stuff.generate_target()
		stuff.target.shift(3*RIGHT)
		self.add(stuff)
		self.play(MoveToTarget(stuff), run_time=2)
		self.wait(2)
	
		

		self.next_section("ResolucionEjercicio.1")
		text1.scale(TEXT_SCALE)
		text1.move_to(START_TEXT)
		text1.to_edge(LEFT)
		text1.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text1)
		#text1.arrange(center=False, aligned_edge=LEFT)
		self.play(Write(text1))
		self.wait(2)

		self.next_section("ResolucionEjercicio.2")
		self.play(Uncreate(text1), run_time=0.8)
		text1_4.scale(MATH_TEXT_SCALE)
		text1_4.move_to(START_TEXT)
		text1_4.to_edge(LEFT)
		text1_4.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text1_4)
		# text1_4.arrange(center=False, aligned_edge=LEFT)
		# text1_4.set_alignment(LEFT)
		self.play(Write(text1_4))
		self.wait(2)
		self.play(Indicate(text1_4))
		self.play(Indicate(text0[1]), Indicate(vec_v1))

		text_w1.scale(TEXT_SCALE)
		text_w1.to_corner(DL)
		text_w1.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text_w1)
		self.play(Write(text_w1))


		self.next_section("ResolucionEjercicio.3")
		self.play(Uncreate(text1_4), run_time=0.8)
		text1_5.scale(MATH_TEXT_SCALE)
		text1_5.move_to(START_TEXT)
		text1_5.to_edge(LEFT)
		text1_5.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text1_5)
		# text1_4.arrange(center=False, aligned_edge=LEFT)
		# text1_4.set_alignment(LEFT)
		self.play(Write(text1_5))
		self.wait(2)


		self.next_section("ResolucionEjercicio.4")
		text1_5_2.scale(MATH_TEXT_SCALE)
		text1_5_2.next_to(text1_5, DOWN)
		text1_5_2.to_edge(LEFT)
		text1_5_2.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text1_5_2)
		# text1_4.arrange(center=False, aligned_edge=LEFT)
		# text1_4.set_alignment(LEFT)
		self.play(Write(text1_5_2))
		self.wait(2)

		self.next_section("proyeccionYResta")
		# dot1 = Dot(point=[10,0,-1])
		# dot2 = Dot(point=[-10,0,10])
		
		self.play(Create(direction_w1))
		self.play(Create(dashed_v2_w1), run_time=2)
		#self.play(Create(rightangle_v2_w1))

		self.next_section("mostrarVectorResta")
		
		self.play(GrowFromPoint(vec_v2_minus_w1, [-3/2,0,3/2]), run_time=2)
		self.wait(1)
		self.play(Transform(vec_v2_minus_w1, vec_w2), run_time=3)
		self.wait(1)
		self.play(Uncreate(direction_w1))
		self.play(Uncreate(dashed_v2_w1))
		#self.play(Uncreate(rightangle_v2_w1))
		self.wait(1)
		self.play(Indicate(vec_w2))
		text_w2.scale(TEXT_SCALE)
		text_w2.to_corner(DL)
		text_w2.shift(1*UP)
		text_w2.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text_w2)
		self.play(Write(text_w2))
		self.play(Indicate(text_w2))


		self.next_section("ResolucionEjercicio.5")
		self.play(Uncreate(text1_5), run_time=0.8)
		self.play(Uncreate(text1_5_2), run_time=0.8)
		text1_6.scale(MATH_TEXT_SCALE)
		text1_6.move_to(START_TEXT)
		text1_6.to_edge(LEFT)
		text1_6.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text1_6)
		# text1_4.arrange(center=False, aligned_edge=LEFT)
		# text1_4.set_alignment(LEFT)
		self.play(Write(text1_6))
		self.wait(2)

		self.next_section("ResolucionEjercicio.6")
		text1_7.scale(MATH_TEXT_SCALE)
		text1_7.next_to(text1_6, DOWN)
		text1_7.to_edge(LEFT)
		text1_7.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text1_7)
		# text1_4.arrange(center=False, aligned_edge=LEFT)
		# text1_4.set_alignment(LEFT)
		self.play(Write(text1_7))
		self.wait(2)


		self.next_section("proyeccionYResta2")
		# dot1 = Dot(point=[10,0,-1])
		# dot2 = Dot(point=[-10,0,10])
		

		self.play(Create(direction_w1))
		self.play(Create(direction_w2))
		self.play(Create(dashed_v3_w1), run_time=2)

		#self.play(Create(rightangle_v2_w1))

		self.next_section("mostrarVectorResta2")
		
		#self.play(Uncreate(rightangle_v2_w1))
		self.wait(1)
		self.play(GrowFromPoint(vec_v3_w1, origin), run_time=2)
		self.wait(1)

		self.play(Create(dashed_v3_w2), run_time=2)
		self.play(GrowFromPoint(vec_v3_w2, origin), run_time=2)
		self.wait(1)

		self.play(Uncreate(direction_w1))
		self.play(Uncreate(direction_w2))
		self.play(Uncreate(dashed_v3_w1))
		self.play(Uncreate(dashed_v3_w2))
		self.wait(1)

		self.play(Indicate(vec_v3_w2), Indicate(vec_v3_w1))

		self.play(GrowFromPoint(sum_vec_v3_w2_and_v3_w1, origin), run_time=2)
		self.wait(1)

		self.play(Indicate(sum_vec_v3_w2_and_v3_w1), Indicate(vec_v3))

		self.play(Transform(sum_vec_v3_w2_and_v3_w1,vec_v3_minus_w1_w2), run_time=4)


		self.wait(1)


		

		self.play(Indicate(vec_v3_minus_w1_w2))
		text_w3.scale(TEXT_SCALE)
		text_w3.to_corner(DL)
		text_w3.shift(2*UP)
		text_w3.set_stroke(width = STROKE_WIDTH)
		self.add_fixed_in_frame_mobjects(text_w3)
		self.play(Write(text_w3))
		self.play(Indicate(text_w3))


		self.stop_ambient_camera_rotation()  # Stop camera rotation
		self.wait(1)


	
class Bibliografia(Scene):
	def construct(self):

		self.next_section("Referencias", PresentationSectionType.NORMAL)

		bibtitle = Tex("Referencias")
		bibtitle.scale(1.5)
		bibtitle.to_edge(UP)
		self.play(Write(bibtitle))

		bib1 = Tex(r"\justifying{1. Speziale, L., Solar E. (1985). \textit{Apuntes de Álgebra Lineal}. Universidad Nacional Autónoma de México}")
		bib2 = Tex(r"\justifying{2. Barrera, F. (2019). \textit{Fundamentos de Álgebra Lineal y Ejercicios}. Segunda edición. Universidad Nacional Autónoma de México}")	
		bib3 = Tex(r"\justifying{3. Sanderson, G. (2016). \textit{Essence of Linear Algebra}. https://www.3blue1brown.com/topics/linear-algebra}")

		bibgroup = VGroup(bib1, bib2, bib3)
		bibgroup.scale(0.6)
		bibgroup.arrange(DOWN, center=False, aligned_edge=LEFT)
		self.play(Write(bibgroup))

		self.wait(2)


# class textGS(ThreeDScene):
# 	def construct(self):
# 		text1 = Tex(r"\justifying {Primero obtendremos un generador ortogonal de dicho espacio, \\\ "
# 			r" mediante el proceso de Gram-Schmidt} \\\ ",
# 			r" Para ello hacemos: \\\ "
# 			r" $\vec{w_1} = \vec{v_1} = (1, 0, -1)$  \newline",
# 			r" $\vec{w_2} = \vec{v_2} - \frac{(\vec{v_2} | \vec{w_1})}{(\vec{w_1} | \vec{w_1})} \vec{w_1} = (-2, 1, 1) - \frac{-3}{2} (1, 0, -1) = (\frac{-1}{2}, 1, \frac{-1}{2} ) $ \newline",
# 			r" $\vec{w_3} = \vec{v_3} - \frac{(\vec{v_3} | \vec{w_1})}{(\vec{w_1} | \vec{w_1})} \vec{w_1} - \frac{(\vec{v_3} | \vec{w_2})}{(\vec{w_2} | \vec{w_2})} \vec{w_2} $\newline",
# 			r" $ = (-1, 1, 0) - \frac{-1}{2} (1, 0, -1) - \frac{\frac{-3}{2}}{\frac{-3}{2}} (\frac{-1}{2}, 1, \frac{-1}{2}) = (0, 0, 0) $"
# 			r"\justifying {entonces: $G_0 = \{ (-1, 0, -1), (\frac{-1}{2}, 1, \frac{-1}{2}), (0, 0, 0) \}$} \\\ \\\ ",
# 			r"\justifying {es un generador ortogonal de \textit{V} y el conjunto} \\\ ",
# 			r"$B = \{ (1, 0, -1), (\frac{-1}{2}, 1, \frac{-1}{2}) \} $",
# 			r" es una base ortogonal de dicho espacio."

# 		).scale(0.6)
# 		text1.set_width(5)
# 		text1.to_corner(UL)
# 		self.play(Write(text1))

# 		text2 = Tex(r"\justifying {Para obtener una base ortonormal calculamos:} \\\ ",
# 			r" $||\vec{w_1}|| = \sqrt{(\vec{w_1}|\vec{w_1})} = \sqrt{2}$ \\\ ",
# 			r" $||\vec{w_2}|| = \sqrt{(\vec{w_2}|\vec{w_2})} = \sqrt{\frac{3}{2}} $ \\\ ",
# 			r" y en consecuencia el conjunto: \\\ ",
# 			r" $B = \{ (\frac{1}{\sqrt{2}}, 0, \frac{-1}{\sqrt{2}}), (\frac{-1}{\sqrt{6}}, \sqrt{\frac{2}{3}}, \frac{-1}{\sqrt{6}}) \} $ \\\ ",
# 			r" es una base ortonormal de V"
# 		).scale(0.6)

	# textgroup1 = VGroup(text1, text1_4, text1_5, text1_6, text1_7, text1_8, text1_9, text1_10, text1_11)
		# textgroup1.arrange(DOWN, center=False, aligned_edge=LEFT)
		# textgroup1.next_to()



# axes = ThreeDAxes()
#         self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

#         # Define the directions of the custom orthonormal basis vectors
#         u_direction = [1, 1, 0]  # Replace with your desired direction
#         v_direction = [-1, 1, 0]  # Replace with your desired direction
#         w_direction = [0, 0, 1]  # Replace with your desired direction

#         # Create the custom orthonormal basis vectors
#         u_hat = Arrow3D(ORIGIN, u_direction, color=RED)
#         v_hat = Arrow3D(ORIGIN, v_direction, color=GREEN)
#         w_hat = Arrow3D(ORIGIN, w_direction, color=BLUE)

#         # Add labels for the custom vectors and coordinates
#         u_label = MathTex(r"\hat{u}", color=RED).next_to(u_hat, RIGHT)
#         v_label = MathTex(r"\hat{v}", color=GREEN).next_to(v_hat, UP)
#         w_label = MathTex(r"\hat{w}", color=BLUE).next_to(w_hat, OUT)

#         u_coords = MathTex(r"\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}", color=RED).next_to(u_hat, DOWN)
#         v_coords = MathTex(r"\begin{bmatrix} -1 \\ 1 \\ 0 \end{bmatrix}", color=GREEN).next_to(v_hat, DOWN)
#         w_coords = MathTex(r"\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}", color=BLUE).next_to(w_hat, DOWN)

#         # Display the custom orthonormal basis and coordinates
#         self.play(Create(axes))
#         self.play(Create(u_hat), Create(v_hat), Create(w_hat))
#         self.play(Create(u_label), Create(v_label), Create(w_label))
#         self.play(Create(u_coords), Create(v_coords), Create(w_coords))

#         # Camera animation: Move around the z-axis
#         self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES)
#         self.begin_ambient_camera_rotation(rate=0.2)  # Rotate the camera
#         self.wait(10)  # Wait for the camera animation
#         self.stop_ambient_camera_rotation()  # Stop camera rotation
#         self.wait(3)












########################################################################################
# Comienza animación de producto interno
########################################################################################
class ProjectionVectorScene(VectorScene):
	def construct(self):
		pass

	def get_plane(self, **kwargs):
		plane = NumberPlane(**kwargs)
		origin = plane.coords_to_point(0,0)

		self.plane, self.origin = plane, origin

		return plane

	def get_vectors_ab(self):
		xval = ValueTracker(self.x_value)
		yval = ValueTracker(self.y_value)
		zval = ValueTracker(self.z_value)

		veca = self.get_vector(self.vector_stat, color = vec_a_color)
		vecb = self.get_vector([xval.get_value(), yval.get_value(), zval.get_value()], color = vec_b_color)

		self.veca, self.vecb = veca, vecb
		self.xval, self.yval, self.zval = xval, yval, zval

		return veca, vecb


	# functions
	def get_pro_vector(self, v1, **kwargs):
		vec1 = v1.get_vector()

		return Arrow(
			np.array([0,0,0]),
			np.dot(np.array([self.xval.get_value(), self.yval.get_value(), self.zval.get_value()]), vec1)/np.linalg.norm(vec1)**2 * vec1, 
			buff = 0, 
			**kwargs
		)

	def get_pro_line(self, v1, **kwargs):
		vec1 = v1.get_vector()
		start = np.array([self.xval.get_value(), self.yval.get_value(), self.zval.get_value()])
		end = np.dot(np.array([self.xval.get_value(), self.yval.get_value(), self.zval.get_value()]), vec1)/np.linalg.norm(vec1)**2 * vec1

		return DashedLine(start, end, **kwargs)

	def get_pro_vector_rotate(self, v1, **kwargs):
		vec1 = np.array([self.xval.get_value(), self.yval.get_value(), 0])
		vec2 = v1.get_vector()

		if angle_between_vectors(vec1, vec2) < PI/2:
			normal_vec = np.array([vec2[1], -vec2[0], 0])
		else:
			normal_vec = np.array([-vec2[1], vec2[0], 0])

		start = self.origin
		end = np.dot(vec1, vec2)/np.linalg.norm(vec2)**2 * normal_vec

		return Arrow(start, end, buff = 0, **kwargs)

	def get_dot_prod_rectangle(self, v1, **kwargs):

		vec1 = v1.get_vector()
		normal_vec = np.array([vec1[1], -vec1[0], 0])

		rect = Rectangle(
			width = np.linalg.norm(vec1), 
			height = np.linalg.norm(np.dot(np.array([self.xval.get_value(), self.yval.get_value(), 0]), vec1)/np.linalg.norm(vec1)**2 * normal_vec), 
			stroke_width = 1
		)
		rect.set_fill(**kwargs)
		rect.next_to(self.origin, RIGHT, buff = 0, aligned_edge = UL)
		rect.rotate(v1.get_angle(), about_point = self.origin)

		return rect


class Calculations(Scene):

	def construct(self):
		pass


	def group_vecs_with_symbol(self, mat_a, mat_b, type = "dot"):
		if type is "dot":
			mult = MathTex("\\cdot").set_color(self.dot_color)
		elif type is "bullet":
			mult = MathTex("\\bullet").set_color(self.dot_color)
		elif type is "cdot":
			mult = MathTex("\\cdot").set_color(self.dot_color)
		else:
			mult = MathTex("\\times").set_color(self.cross_color)

		group = VGroup(mat_a, mult, mat_b)
		group.arrange_submobjects(RIGHT)

		return group

	def get_dotproduct_path(self, vec_group, dimension = 3, color = ORANGE, stroke_width = 5):
		path = VMobject()
		if dimension == 3:
			path.set_points_smoothly([
				vec_group[0][0][0].get_center(),     # x Kompenente vec1 und vec2
				vec_group[2][0][0].get_center(),
				vec_group[0][0][1].get_center(),     # y Kompenente vec1 und vec2
				vec_group[2][0][1].get_center(),
				vec_group[0][0][2].get_center(),     # z Kompenente vec1 und vec2
				vec_group[2][0][2].get_center(),
			])
		elif dimension == 2:
			path.set_points_smoothly([
				vec_group[0][0][0].get_center(),     # x Kompenente vec1 und vec2
				vec_group[2][0][0].get_center(),
				vec_group[0][0][1].get_center(),     # y Kompenente vec1 und vec2
				vec_group[2][0][1].get_center(),
			])

		path.set_color(color = color)
		path.set_stroke(width = stroke_width)

		return path

	def get_dotproduct_surrects(self, vec_group, color = ORANGE):
		rects = VGroup(*[
			SurroundingRectangle(matrix_element).set_color(color = color)
			for matrix_element in [
				vec_group[0][0][0],     # x Kompenente vec1 und vec2
				vec_group[2][0][0],
				vec_group[0][0][1],     # y Kompenente vec1 und vec2
				vec_group[2][0][1],
				vec_group[0][0][2],     # z Kompenente vec1 und vec2
				vec_group[2][0][2],
			]
		])
		return rects

	def get_crossproduct_path_xyz(self, vec_group, color = ORANGE, stroke_width = 5):
		path_x, path_y, path_z = VMobject(), VMobject(), VMobject()

		# vec_group[0] --> erster Vektor, maths[1][1] Mal zeichen, maths[1][2] zweiter Vektor
		# vec_group[i][0] --> Vektoreinträge
		# vec_group[i][0][j] --> x,y,z Komponente

		path_x.set_points_smoothly([
			vec_group[0][0][1].get_center(),     # y Komponente vec1
			vec_group[2][0][2].get_center(),     # z Komponente vec2
			vec_group[0][0][2].get_center(),     # y Komponente vec1
			vec_group[2][0][1].get_center(),     # z Komponente vec2
		])

		path_y.set_points_smoothly([
			vec_group[0][0][2].get_center(),     # z Komponente vec1
			vec_group[2][0][0].get_center(),     # x Komponente vec2
			vec_group[0][0][0].get_center(),     # x Komponente vec1
			vec_group[2][0][2].get_center(),     # z Komponente vec2
		])

		path_z.set_points_smoothly([
			vec_group[0][0][0].get_center(),     # x Komponente vec1
			vec_group[2][0][1].get_center(),     # y Komponente vec2
			vec_group[0][0][1].get_center(),     # y Komponente vec1
			vec_group[2][0][0].get_center(),     # x Komponente vec2
		])

		for path in path_x, path_y, path_z:
			path.set_color(ORANGE).set_stroke(width = 7)

		return path_x, path_y, path_z

	# ToDo: elemente im Skalarprodukt anordnen & Klammern für negative Zahlen
	def get_dotproduct(self, vec_group):
		# vec_group_elements = VGroup(*[
		#     TexMobject(element.get_tex_string())
		#     for element in [
		#         vec_group[0][0][0],     # x Kompenente vec1 und vec2
		#         vec_group[2][0][0],
		#         vec_group[0][0][1],     # y Kompenente vec1 und vec2
		#         vec_group[2][0][1],
		#         vec_group[0][0][2],     # z Kompenente vec1 und vec2
		#         vec_group[2][0][2],
		#     ]
		# ])
		dot_product = MathTex(
			vec_group[0][0][0].get_tex_string(),     # x Kompenente vec1 und vec2
			"\\cdot",
			vec_group[2][0][0].get_tex_string(),
			"+",
			vec_group[0][0][1].get_tex_string(),     # y Kompenente vec1 und vec2
			"\\cdot",
			vec_group[2][0][1].get_tex_string(),
			"+",
			vec_group[0][0][2].get_tex_string(),     # z Kompenente vec1 und vec2
			"\\cdot",
			vec_group[2][0][2].get_tex_string()
		)
		return dot_product




class DotProdRectangleShowVectors(MovingCameraScene, ProjectionVectorScene):
	def construct(self):

		self.plane_config = {
			"axis_config": {"stroke_color": GREY}, "background_line_style": {"stroke_opacity": 0.6, "stroke_color": GREY}
		}
		self.pro_color = GREEN
		self.rect_color = BLUE_E
		self.x_value = 1
		self.y_value = 2
		self.z_value = 0
		self.vector_stat = [4,3,0]
		self.mat_kwargs = {
			"v_buff": 0.6, 
			"left_bracket": "(",
			"right_bracket": ")",
			"bracket_v_buff": 0.1,
		}


		self.next_section("A", PresentationSectionType.NORMAL)
		self.setup_scene()
		

		self.next_section("A.1", PresentationSectionType.NORMAL)
		self.calc_dot_product()

		self.next_section("A.2", PresentationSectionType.NORMAL)
		self.zoom_camera()

		self.next_section("A.3", PresentationSectionType.NORMAL)
		self.second_formula()

		self.next_section("A.4", PresentationSectionType.NORMAL)
		self.projection_vectors()

		self.next_section("A.5", PresentationSectionType.NORMAL)
		self.length_of_projection_vector()

		self.next_section("A.6", PresentationSectionType.NORMAL)
		self.projection_rectangle()

		self.next_section("A.7", PresentationSectionType.NORMAL)
		self.varying_rectangles()

		self.next_section("A.8", PresentationSectionType.NORMAL)
		self.varying_vectors()


	def setup_scene(self):
		plane = self.get_plane(**self.plane_config)
		plane.add_coordinates()

		self.camera.frame.save_state()
		self.camera.frame.set(width = config["frame_width"] * 0.33),
		start_vec_a = plane.get_vector([np.cos(30*DEGREES), np.sin(30*DEGREES), 0], color = vec_a_color)
		start_vec_b = plane.get_vector([np.cos(90*DEGREES), np.sin(90*DEGREES), 0], color = vec_b_color)
		circle = Circle(arc_center = self.origin, radius = plane.get_x_unit_size(), color = GREY)

		self.add(plane)
		self.wait(2)

		self.play(
			LaggedStartMap(GrowArrow, VGroup(start_vec_a, start_vec_b)), 
			Create(circle), 
			run_time = 1.5
		)
		self.wait()


		veca, vecb = self.get_vectors_ab()

		a_matrix = Matrix([[str(self.vector_stat[0])], [str(self.vector_stat[1])]], **self.mat_kwargs)
		b_matrix = Matrix([["1"], ["2"]], **self.mat_kwargs)
		a_matrix_label = MathTex("\\vec{a}", "=").set_color(veca.get_color())
		b_matrix_label = MathTex("\\vec{b}", "=").set_color(vecb.get_color())
		
		for label, matrix in zip([a_matrix_label, b_matrix_label], [a_matrix, b_matrix]):
			label.next_to(matrix, LEFT)

		a_texs = VGroup(a_matrix_label, a_matrix).to_corner(UL)
		b_texs = VGroup(b_matrix_label, b_matrix).next_to(a_texs, RIGHT, buff = 0.5)

		self.matrix_group = VGroup(a_texs, b_texs)


		bg_rect1 = Rectangle(
			width = self.matrix_group.width + 0.1,
			height = self.matrix_group.height + 0.1,
			stroke_width = 0,
		)
		bg_rect1.set_fill(color = BLACK, opacity=0.7)
		bg_rect1.move_to(self.matrix_group)
		self.play(
			AnimationGroup(
				FadeIn(bg_rect1), 
				Write(a_texs),
				Uncreate(circle),
				Restore(self.camera.frame),
				ReplacementTransform(start_vec_a, veca),
				Write(b_texs),
				ReplacementTransform(start_vec_b, vecb),
				lag_ratio = 0.05
			), 
			run_time = 3
		)
		self.wait()


		self.a_matrix, self.b_matrix = a_matrix, b_matrix
		self.a_matrix_label, self.b_matrix_label = a_matrix_label, b_matrix_label


	def calc_dot_product(self):
		a_matrix, b_matrix = self.a_matrix, self.b_matrix
		a_matrix_label, b_matrix_label = self.a_matrix_label, self.b_matrix_label


		dot_prod1 = MathTex("\\vec{a}", "\\cdot", "\\vec{b}", "=", "4", "\\cdot", "1", "+", "3", "\\cdot", "2")\
			.next_to(self.matrix_group, DOWN, buff = 0.5)\
			.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color})\
			.add_background_rectangle()
		dot_prod2 = MathTex("\\vec{a}", "\\cdot", "\\vec{b}", "=", "10")\
			.move_to(dot_prod1, aligned_edge = LEFT)\
			.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color})\
			.add_background_rectangle()

		a_copy = a_matrix_label[0].copy()
		b_copy = b_matrix_label[0].copy()
		for copy in a_copy, b_copy:
			copy.generate_target()
		a_copy.target.move_to(dot_prod1[1])
		b_copy.target.move_to(dot_prod1[3])

		# bg, a * b = schreiben
		self.play(
			FadeIn(dot_prod1[0]),
			Write(dot_prod1[2]),
			*[MoveToTarget(vec) for vec in [a_copy, b_copy]],
			Write(dot_prod1[4]),
			run_time = 2
		)
		self.remove(a_copy, b_copy)
		self.add(dot_prod1[1], dot_prod1[3])

		# Path für Skalarprodukt
		path = VMobject()
		path.set_points_smoothly([
			a_matrix[0][0].get_center(), b_matrix[0][0].get_center(), a_matrix[0][1].get_center(), b_matrix[0][1].get_center()
		])
		path.set_color(vec_c_color)
		path.set_stroke(width = 5)

		self.play(
			ShowPassingFlash(path, rate_func = smooth),
			ShowIncreasingSubsets(dot_prod1[5:], rate_func = linear), 
			run_time = 2
		)
		self.wait(0.5)

		# Transforming into result
		self.play(
			Transform(dot_prod1[0], dot_prod2[0]),
			Transform(dot_prod1[5:], dot_prod2[5]),
		)
		self.wait(2)

	def zoom_camera(self):
		self.camera.frame.save_state()

		self.play(
			self.camera.frame.animate.set(width = config.frame_width * 0.77).move_to(1.7*RIGHT + 0.95*UP),
			run_time = 2
		)
		self.wait()

	def second_formula(self):

		angle = Arc(
			angle = angle_between_vectors(self.veca.get_vector(), self.vecb.get_vector()), start_angle = self.veca.get_angle(), 
			radius = 1, color = self.pro_color
		)

		tex_phi = MathTex("\\varphi")\
			.move_to(1*RIGHT + 1.25*UP)\
			.set_color(angle.get_color())\
			.add_background_rectangle()

		new_formula = MathTex(
			"\\vec{a}", "\\cdot", "\\vec{b}", "=", "\\lvert", "\\vec{a}", "\\rvert", "\\cdot", 
			"\\lvert", "\\vec{b}", "\\rvert", "\\cdot", 
			"\\cos", "(", "\\varphi", ")"
		)\
			.next_to(self.veca.get_end(), UP)\
			.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color, "\\varphi": self.pro_color})\
			.add_background_rectangle()


		self.play(
			LaggedStartMap(Create, VGroup(angle, tex_phi), lag_ratio = 0.25), 
			FadeIn(new_formula[0]),
			ShowIncreasingSubsets(VGroup(*new_formula[1:])), 
			run_time = 2
		)
		self.wait()

		self.play(Uncreate(angle), FadeOut(tex_phi))
		self.wait()

		self.new_formula = new_formula

	def projection_vectors(self):
		veca, vecb = self.veca, self.vecb

		pro_vec = self.pro_vec = self.get_pro_vector(veca, color = vec_c_color)
		pro_line = self.pro_line = self.get_pro_line(veca, color = WHITE)

		self.play(
			Create(pro_line),
			ReplacementTransform(vecb.copy(), pro_vec), 
			run_time = 2
		)
		self.wait()

		brace = Brace(Line(ORIGIN, 2*RIGHT), DOWN, buff = 0.6, color = GREY)
		brace.next_to(self.origin, RIGHT, buff = 0, aligned_edge = UL)
		brace.rotate(veca.get_angle(), about_point = self.origin)

		self.play(Create(brace))

		ba = brace.get_tex("\\vec{b}_", "{\\vec{a}}", buff = 0.1)\
			.set_color(vec_c_color)\
			.add_background_rectangle()

		ba_text = Tex("Proyección del vector \\\\", "$\\vec{b}$", " sobre ", "$\\vec{a}$")\
			.next_to(ba, RIGHT)\
			.shift(0.75*DOWN)\
			.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color})\
			.add_background_rectangle()

		self.play(Create(ba))
		self.play(
			FadeIn(ba_text[0], run_time = 1), 
			Write(ba_text[1:], run_time = 2), 
		)
		self.wait()

		# Ausfaden von Projektionsgedöns
		self.play(
			LaggedStartMap(FadeOut, VGroup(ba_text[0], ba_text[1:], ba[0], ba[1:], brace), shift = DOWN, lag_ratio = 0.25), 
			run_time = 2
		)
		self.wait()

	def length_of_projection_vector(self):
		angle = Arc(angle = angle_between_vectors(self.veca.get_vector(), self.vecb.get_vector()), start_angle = self.veca.get_angle(), radius = 1)
		angle.set_color(GREEN)
		self.play(Create(angle))
		self.wait(0.5)

		for vec in self.pro_vec, self.vecb:
			self.play(ApplyWave(vec), run_time = 1.5)
			self.wait(0.5)

		#                     0     1       2        3    4    5       6          7         8        9      10      11         12         13           14        15     16
		length1 = MathTex("\\cos", "(", "\\varphi", ")", "=", "{", "\\lvert", "\\vec{b}_", "{", "\\vec{a}", "}", "\\rvert", "\\over", "\\lvert", "\\vec{b}", "\\rvert", "}")\
			.move_to(4*RIGHT + UP)
		length1[2].set_color(self.pro_color)
		length1[7:10].set_color(vec_c_color)
		length1[14].set_color(vec_b_color)

		self.play(FadeIn(length1[:4]), run_time = 1)
		self.play(LaggedStartMap(FadeIn, VGroup(length1[4], length1[5:12], length1[12], length1[13:]), lag_ratio = 0.4), run_time = 3)
		self.wait()


		#                     0                1                2       3       4           5          6         7         8      9       10      11
		length2 = MathTex("\\lvert", "\\vec{b}_{\\vec{a}}", "\\rvert", "=", "\\lvert", "\\vec{b}", "\\rvert", "\\cdot", "\\cos", "(", "\\varphi", ")")\
			.move_to(4*RIGHT + DOWN)
		length2[1].set_color(vec_c_color)
		length2[5].set_color(vec_b_color)
		length2[10].set_color(self.pro_color)


		phi_copy, b_copy, ba_copy = length1[:4].copy(), length1[13:16].copy(), length1[6:12].copy()
		targets = [length2[8:], length2[4:7], length2[:3]]
		for element, target in zip([phi_copy, b_copy, ba_copy], targets):
			element.generate_target()
			element.target.move_to(target)

		self.play(
			LaggedStartMap(MoveToTarget, VGroup(phi_copy, b_copy, ba_copy), lag_ratio = 0.5, run_time = 5),
			LaggedStartMap(Create, VGroup(length2[3], length2[7]), lag_ratio = 0.75, run_time = 3),
		)
		self.wait()


		sur_rects = VGroup(*[
			SurroundingRectangle(mob).set_color(vec_c_color)
			for mob in [self.new_formula[9:], length2[4:]]
		])

		self.play(Create(sur_rects), lag_ratio = 0.15, run_time = 2)
		self.wait()

		vector_texs = VGroup(*[
			Tex(tex)\
				.scale(0.5)\
				.rotate(self.veca.get_angle())\
				.set_color(color = color)\
				.next_to(vec.get_end(), direction = DL)\
				.shift(0.25*DOWN)
			for tex, color, vec in zip(
				["Vector $\\vec{a}$", "Proyección $\\vec{b}_{\\vec{a}}$"], 
				[vec_a_color, vec_c_color], 
				[self.veca, self.pro_vec]
			)
		])

		self.bring_to_front(
			self.veca, self.vecb, self.pro_vec, self.pro_line,
			self.new_formula, sur_rects
		)

		self.curr_mobs = Group(*self.mobjects[:-11])
		self.play(
			FadeOut(self.curr_mobs, run_time = 4), 
			*[Write(text, rate_func = squish_rate_func(smooth, 0.5, 0.8)) for text in vector_texs]
		)
		self.wait()


		self.play(FadeOut(vector_texs[0], target_position = self.new_formula[5]), run_time = 1.5)
		self.play(FadeOut(vector_texs[1], target_position = self.new_formula[7:]), run_time = 2)
		self.wait()

		self.remove(length2[0])
		self.play(
			FadeIn(self.plane), 
			FadeOut(sur_rects, length2[3], length2[7], length2[11], phi_copy, b_copy, ba_copy),
			run_time = 2
		)

		self.bring_to_back(self.plane)
		self.wait()

	def projection_rectangle(self):
		# rotate pro_vec 90 Degrees + Rectangle
		pro_vec_rot = self.pro_vec_rot = self.get_pro_vector_rotate(self.veca, color = self.pro_vec.get_color())

		self.play(ReplacementTransform(self.pro_vec.copy(), pro_vec_rot, path_arc = -PI/2), run_time = 5)
		self.wait()

		square = Square(stroke_color = BLACK, stroke_width = 1, fill_color = self.rect_color, fill_opacity = 0.4)
		square.replace(
			VGroup(*[
				VectorizedPoint(self.plane.coords_to_point(i, i))
				for i in (0, 1)
			]),
			stretch = True
		)

		unit_areas = VGroup(*[
			square.copy().move_to(
				self.plane.coords_to_point(x, y),
				DOWN+LEFT
			)
			for x in range(int(np.linalg.norm(self.veca.get_vector())))
			for y in range(int(np.linalg.norm(self.pro_vec.get_vector())))
		])\
			.set_color(self.rect_color)\
			.set_stroke(opacity = 0.75)\
			.next_to(self.origin, RIGHT, buff = 0, aligned_edge = UL)\
			.rotate(angle = self.veca.get_angle(), about_point = self.origin)

		self.play(LaggedStartMap(DrawBorderThenFill, unit_areas, lag_ratio = 0.05), run_time = 3)
		self.bring_to_front(self.veca, self.pro_line, self.pro_vec, pro_vec_rot)
		self.wait()


		# Rotate pro_vec und veca --> show their length
		for vec in self.pro_line, self.pro_vec:
			vec.suspend_updating()

		# rate_func = there_and_back_with_pause doesn't work
		for angle in [-36.87*DEGREES, 36.87*DEGREES]:
			self.play(*[
				Rotating(vec, radians = angle, about_point = self.origin, rate_func = there_and_back_with_pause, run_time = 1.75)
				for vec in [self.pro_vec, self.veca]
			])
			self.wait()


		for vec in self.pro_line, self.pro_vec:
			vec.resume_updating()


		pro_rect = self.pro_rect = self.get_dot_prod_rectangle(self.veca, color = BLUE_E, opacity = 0.4)
		self.play(
			LaggedStartMap(FadeOut, unit_areas), 
			FadeIn(pro_rect),
			run_time = 3
		)
		self.bring_to_front(self.veca, self.pro_line, self.pro_vec, pro_vec_rot)
		self.wait()


		# updaters
		pro_vec, pro_line = self.pro_vec, self.pro_line
		veca, vecb = self.veca, self.vecb
		xval, yval = self.xval, self.yval

		vecb.add_updater(lambda v: v.become(
			self.get_vector([xval.get_value(),yval.get_value(),0], color = vec_b_color)
		))
		pro_vec.add_updater(lambda v: v.become(
			self.get_pro_vector(veca, color = vec_c_color)
		))
		pro_line.add_updater(lambda v: v.become(
			self.get_pro_line(veca, color = WHITE)
		))

		pro_vec_rot.add_updater(lambda r: r.become(
			self.get_pro_vector_rotate(self.veca, color = self.pro_vec.get_color())
		))
		pro_rect.add_updater(lambda r: r.become(
			self.get_dot_prod_rectangle(self.veca, color = BLUE_E, opacity = 0.4)
		))

		# self.bring_to_front(self.vecb)

	def varying_rectangles(self):

		bg_rect = Rectangle(width = 5, height = 1.75, color=BLACK, stroke_width=0, stroke_opacity=0, fill_opacity=0.75)
		bg_rect.move_to(self.a_matrix, aligned_edge=LEFT)
		self.a_matrix[0].set_color(vec_a_color)

		self.play(
			Restore(self.camera.frame), 
			self.xval.animate.set_value(-2), 
			self.yval.animate.set_value(1),
			Create(bg_rect, rate_func = squish_rate_func(smooth, 0, 0.3)), 
			Write(self.a_matrix, rate_func = squish_rate_func(smooth, 0, 0.3)),
			run_time = 4
		)
		self.wait()


		x_values = [-2, -5, 1.5,  3, 4]
		y_values = [ 1,  0,  -2, -1, 3]

		cdot = MathTex("\\cdot").set_color(self.pro_color).next_to(self.a_matrix, RIGHT)
		b_matrizes = VGroup(*[
			Matrix([[str(x_value)], [str(y_value)]], **self.mat_kwargs).next_to(cdot, RIGHT)
			for x_value, y_value in zip(x_values, y_values)
		])
		for matrix in b_matrizes:
			matrix[0].set_color(vec_b_color)
		equals = MathTex("=").next_to(b_matrizes, RIGHT)


		self.play(
			FadeIn(cdot, shift = UP), 
			TransformFromCopy(self.vecb, b_matrizes[0]),
			run_time = 2
		)
		self.wait()
		self.play(Write(equals))
		self.wait()


		results_list = [round(4*x_value + 3*y_value, 0) for x_value, y_value in zip(x_values, y_values)]
		results = VGroup(*[
			MathTex(str(result)).next_to(equals, RIGHT).set_color(vec_c_color)
			for result in results_list
		])
		self.play(Write(results[0]))
		self.wait()


		# for obj in self.pro_line, self.pro_vec, self.pro_vec_rot, self.pro_rect:
		#     obj.suspend_updating()

		self.pro_rect.clear_updaters()

		self.play(Rotating(self.pro_rect, radians = -1 * self.veca.get_angle(), about_point = self.origin, rate_func = smooth, run_time = 3))
		self.wait()
		self.play(Rotating(self.pro_rect, radians = self.veca.get_angle(), about_point = self.origin, rate_func = smooth, run_time = 3))
		self.wait()

		self.pro_rect.add_updater(lambda r: r.become(
			self.get_dot_prod_rectangle(self.veca, color = BLUE_E, opacity = 0.4)
		))

		# for obj in self.pro_line, self.pro_vec, self.pro_vec_rot, self.pro_rect:
		#     obj.resume_updating()

		for x, y, index in zip(x_values[1:], y_values[1:], range(len(b_matrizes))):
			self.play(
				self.xval.animate.set_value(x),
				self.yval.animate.set_value(y),
				Transform(b_matrizes[0], b_matrizes[index + 1], rate_func = squish_rate_func(smooth, 0.5, 1)),
				run_time = 4
			)
			self.wait()
			self.play(Transform(results[0], results[index + 1]))
			self.wait()
		self.wait(3)

	def varying_vectors(self):
		xval, yval = self.xval, self.yval

		# verschiedene Projektionen zeigen
		xval_list = [0.5, 4, 4, 1.5, -1,-3, 1]
		yval_list = [3.5, 3, 1,  -2, -2, 1, 2]
		runtime_list = [3,4,3,5,3,3,3]
		for xvalue, yvalue, runtime in zip(xval_list, yval_list, runtime_list):
			self.play(
				xval.animate.set_value(xvalue), 
				yval.animate.set_value(yvalue), 
				run_time = runtime
			)
			self.wait()





########################################################################################
# Finaliza animación de producto interno
########################################################################################
















#######################################################################################
# Animacion Gram Schmidt no usada
#######################################################################################


# from manimlib.imports import *
# from enum import Enum


# class Action(Enum):
#     UPDATE_MATRIX_REMOVE_Q = 1
#     ADD_PROJECTION = 2
#     REMOVE_PROJECTIONS_SET_Q = 3
#     NORMALIZE_Q = 4


# def gram_schmidt(A):
	
#     (n, m) = A.shape
	
#     for i in range(m):
		
#         q = A[:, i] # i-th column of A
		
#         for j in range(i):
#             yield (Action.ADD_PROJECTION, np.dot(A[:, j], A[:, i]) * A[:, j])
#             q = q - np.dot(A[:, j], A[:, i]) * A[:, j]
		
#         if np.array_equal(q, np.zeros(q.shape)):
#             raise np.linalg.LinAlgError("The column vectors are not linearly independent")
		
#         yield (Action.REMOVE_PROJECTIONS_SET_Q, q)
		
#         # normalize q
#         q = q / np.sqrt(np.dot(q, q))

#         yield (Action.NORMALIZE_Q, q)
		
#         # write the vector back in the matrix
#         A[:, i] = q

#         yield (Action.UPDATE_MATRIX_REMOVE_Q, None)


# class GramSchmidt(ThreeDScene):

#     CONFIG = {
#         "x_axis_label": "$x$",
#         "y_axis_label": "$y$",
#         "basis_i_color": GREEN,
#         "basis_j_color": RED,
#         "basis_k_color": GOLD,
#         "q_color": PURPLE,
#         "q_shifted_color": PINK,
#         "projection_color": BLUE
#     }

#     def create_matrix(self, np_matrix):

#         m = Matrix(np_matrix)

#         m.scale(0.5)
#         m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

#         m.to_corner(UP + LEFT)

#         return m

#     def construct(self):
		
#         M = np.array([
#             [1.0, 1.0, -3.0],
#             [3.0, 2.0, 1.0],
#             [-2.0, 0.5, 2.5]
#         ])

#         axes = ThreeDAxes()

#         axes.set_color(GRAY)

#         axes.add(axes.get_axis_labels())

#         self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

#         basis_helper = TextMobject("$ a_1 $", ",", "$ a_2 $", ",", "$ a_3 $")
#         basis_helper[0].set_color(self.basis_i_color)
#         basis_helper[2].set_color(self.basis_j_color)
#         basis_helper[4].set_color(self.basis_k_color)

#         q_helper = TextMobject("Current $ q_i $ vector")
#         q_helper[0].set_color(self.q_color)

#         q_shifted_helper = TextMobject("Shifted $ q_i $ vector")
#         q_shifted_helper[0].set_color(self.q_shifted_color)

#         projection_helper = TextMobject("Projection vectors")
#         projection_helper[0].set_color(self.projection_color)

#         helper = VGroup(
#             projection_helper,
#             q_helper,
#             q_shifted_helper,
#             basis_helper
#         )

#         helper.arrange(
#             DOWN,
#             aligned_edge = RIGHT,
#             buff=0.1
#         )

#         helper.to_corner(UP + RIGHT)

#         self.add_fixed_in_frame_mobjects(helper)

#         # matrix

#         matrix = self.create_matrix(M)

#         self.add_fixed_in_frame_mobjects(matrix)

#         # axes & camera

#         self.add(axes)

#         self.begin_ambient_camera_rotation(rate=0.15)

#         i_vec = Vector(M[:, 0], color=self.basis_i_color)
#         j_vec = Vector(M[:, 1], color=self.basis_j_color)
#         k_vec = Vector(M[:, 2], color=self.basis_k_color)

#         self.play(
#             GrowArrow(i_vec),
#             GrowArrow(j_vec),
#             GrowArrow(k_vec),
#             Write(helper)
#         )

#         self.wait()

#         projection_vectors = []

#         q = None

#         for (action, payload) in gram_schmidt(M):

#             if action == Action.UPDATE_MATRIX_REMOVE_Q:

#                 assert not q is None

#                 M_rounded = np.round(M.copy(), 2)
				
#                 self.remove(matrix)

#                 matrix = self.create_matrix(M_rounded)

#                 self.add_fixed_in_frame_mobjects(matrix)

#                 i_vec_new = Vector(M[:, 0], color=self.basis_i_color)
#                 j_vec_new = Vector(M[:, 1], color=self.basis_j_color)
#                 k_vec_new = Vector(M[:, 2], color=self.basis_k_color)

#                 animation_time = 2.0

#                 self.play(
#                     FadeOut(q, run_time=animation_time * 0.75),
#                     ReplacementTransform(i_vec, i_vec_new, run_time=animation_time),
#                     ReplacementTransform(j_vec, j_vec_new, run_time=animation_time),
#                     ReplacementTransform(k_vec, k_vec_new, run_time=animation_time)
#                 )

#                 self.wait()

#                 i_vec, j_vec, k_vec = i_vec_new, j_vec_new, k_vec_new

#             elif action == Action.ADD_PROJECTION:

#                 p = Vector(payload, color=self.projection_color)

#                 projection_vectors.append(p)

#                 self.play(GrowArrow(p))

#                 self.wait()

#                 if len(projection_vectors) == 2:

#                     first_projection_end = projection_vectors[0].get_end()

#                     p_shifted = Arrow(first_projection_end, first_projection_end + payload, buff=0, color=self.projection_color)

#                     projection_vectors[1] = p_shifted

#                     self.play(ReplacementTransform(p, p_shifted))

#                     self.wait()

#             elif action == Action.REMOVE_PROJECTIONS_SET_Q:

#                 if not projection_vectors:

#                     q = Vector(payload, color=self.q_color)

#                     self.play(GrowArrow(q))

#                     self.wait()

#                     continue

#                 last_projection_end = projection_vectors[len(projection_vectors) - 1].get_end()

#                 q_shifted = Arrow(last_projection_end, last_projection_end + payload, buff=0, color=self.q_shifted_color)

#                 self.play(GrowArrow(q_shifted))

#                 self.wait()

#                 q = Vector(payload, color=self.q_color)

#                 self.play(
#                     ReplacementTransform(q_shifted, q),
#                     *[FadeOut(p) for p in projection_vectors]
#                 )

#                 self.wait()

#                 projection_vectors = []

#             elif action == Action.NORMALIZE_Q:

#                 q_normalized = Vector(payload, color=self.q_color)

#                 self.play(ReplacementTransform(q, q_normalized))

#                 self.wait()

#                 q = q_normalized

#             else:
#                 assert False

#             self.wait(1)

#         assert np.allclose(M.T @ M, np.identity(3))

#         self.wait(15)



