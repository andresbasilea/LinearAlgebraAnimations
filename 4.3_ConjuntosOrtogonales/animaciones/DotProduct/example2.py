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
		


		self.next_section("A.3", PresentationSectionType.NORMAL)
		plane = NumberPlane(stroke_color=LIGHT_GREY, stroke_opacity=0.8)
		plane.add_coordinates()
		self.play(Create(plane))
		self.bring_to_front(text0)

		B_basis = [(0,1), (1,0)]
		a_vector = (2,3)

		coords = (2, 3)

		# Create the vector with the specified coordinates
		vector = Vector(coords, color=RED, stroke_width=4)

		# Define a label for "vector"
		# label_vector = MathTex("vector", color=WHITE, stroke_width=1)
		# label_vector.move_to(title, aligned_edge=DOWN)

		# Animate the word "vector" transforming into the vector
		self.play(ReplacementTransform(text0[1][3], vector))

		# Add the vector to the scene
		#self.play(Create(vector))

		# Add labels for the coordinates
		label_coords = MathTex(f"({coords[0]}, {coords[1]})", color=WHITE, stroke_width=1).next_to(vector, RIGHT).shift(0.15*RIGHT)
		self.play(Create(label_coords))

		self.wait(1)

		
		# Define the coordinates for the orthonormal basis vectors
		orthonormal_coords = (2, 0), (0, 3)

		# Create orthonormal basis vectors
		orthonormal_vector1 = Vector(orthonormal_coords[0], color=GREEN, stroke_width=4)
		orthonormal_vector2 = Vector(orthonormal_coords[1], color=BLUE, stroke_width=4)

		# Add orthonormal basis vectors to the scene
		self.play(Create(orthonormal_vector1), Create(orthonormal_vector2))

		# Add labels for the orthonormal basis vectors
		label_orthonormal1 = MathTex(r"\hat{i}", color=GREEN, stroke_width=1).next_to(orthonormal_vector1, UP).shift(0.15*UP, 0.5*LEFT)
		label_orthonormal2 = MathTex(r"\hat{j}", color=BLUE, stroke_width=1).next_to(orthonormal_vector2, RIGHT).shift(0.15*RIGHT, 0.5*DOWN)

		self.play(Create(label_orthonormal1), Create(label_orthonormal2))

		# Calculate the coordinates of the vector in the orthonormal basis
		dot_product_i = np.dot(coords, orthonormal_coords[0])
		dot_product_j = np.dot(coords, orthonormal_coords[1])

		# Create labels for the coordinates in the orthonormal basis
		label_coords_orthonormal = MathTex(f"({dot_product_i}, {dot_product_j})", color=WHITE, stroke_width=1).next_to(orthonormal_vector2, RIGHT).shift(0.15*RIGHT)

		self.play(Transform(label_coords, label_coords_orthonormal))
		self.wait(1)





class GramSchmidtOrthogonalization(Scene):
	def construct(self):
		# Define the initial vectors
		v1 = np.array([3, 1])
		v2 = np.array([1, 2])

		# Create vector representations
		vector1 = Vector(v1, color=RED, buff=0)
		vector2 = Vector(v2, color=BLUE, buff=0)

		# Display the initial vectors
		self.play(Create(vector1), Create(vector2))
		self.wait(1)

		# Step 1: Calculate the first orthogonal vector
		u1 = v1
		vector1_target = Vector(u1, color=GREEN, buff=0)
		self.play(Transform(vector1, vector1_target))
		self.wait(1)

		# Step 2: Calculate the second orthogonal vector
		v2_proj_v1 = (np.dot(v2, v1) / np.dot(v1, v1)) * v1
		u2 = v2 - v2_proj_v1
		vector2_target = Vector(u2, color=PURPLE, buff=0)
		self.play(Transform(vector2, vector2_target))
		self.wait(1)

		# Display the final result
		self.wait(2)










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


