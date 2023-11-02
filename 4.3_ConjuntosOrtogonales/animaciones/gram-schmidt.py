from manimlib import *
from enum import Enum


class Action(Enum):
    UPDATE_MATRIX_REMOVE_Q = 1
    ADD_PROJECTION = 2
    REMOVE_PROJECTIONS_SET_Q = 3
    NORMALIZE_Q = 4


def gram_schmidt(A):
    
    (n, m) = A.shape
    
    for i in range(m):
        
        q = A[:, i] # i-th column of A
        
        for j in range(i):
            yield (Action.ADD_PROJECTION, np.dot(A[:, j], A[:, i]) * A[:, j])
            q = q - np.dot(A[:, j], A[:, i]) * A[:, j]
        
        if np.array_equal(q, np.zeros(q.shape)):
            raise np.linalg.LinAlgError("The column vectors are not linearly independent")
        
        yield (Action.REMOVE_PROJECTIONS_SET_Q, q)
        
        # normalize q
        q = q / np.sqrt(np.dot(q, q))

        yield (Action.NORMALIZE_Q, q)
        
        # write the vector back in the matrix
        A[:, i] = q

        yield (Action.UPDATE_MATRIX_REMOVE_Q, None)


class GramSchmidt(ThreeDScene):

    
    x_axis_label = "$x$",
    y_axis_label = "$y$",
    basis_i_color = GREEN,
    basis_j_color = RED,
    basis_k_color = GOLD,
    q_color = PURPLE,
    q_shifted_color = PINK,
    projection_color = BLUE


    def create_matrix(self, np_matrix):

        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(self.basis_i_color, self.basis_j_color, self.basis_k_color)

        m.to_corner(UP + LEFT)

        return m

    def construct(self):
        
        M = np.array([
            [1.0, 1.0, -3.0],
            [3.0, 2.0, 1.0],
            [-2.0, 0.5, 2.5]
        ])

        axes = ThreeDAxes()

        axes.set_color(WHITE)

        axes.add(axes.get_axis_labels())

        #self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

        basis_helper = TexText("$ a_1 $", ",", "$ a_2 $", ",", "$ a_3 $")
        basis_helper[0].set_color(self.basis_i_color)
        basis_helper[2].set_color(self.basis_j_color)
        basis_helper[4].set_color(self.basis_k_color)

        q_helper = TexText("Current $ q_i $ vector")
        q_helper[0].set_color(self.q_color)

        q_shifted_helper = TexText("Shifted $ q_i $ vector")
        q_shifted_helper[0].set_color(self.q_shifted_color)

        projection_helper = TexText("Projection vectors")
        projection_helper[0].set_color(self.projection_color)

        helper = VGroup(
            projection_helper,
            q_helper,
            q_shifted_helper,
            basis_helper
        )

        helper.arrange(
            DOWN,
            aligned_edge = RIGHT,
            buff=0.1
        )

        helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(helper)

        # matrix

        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera

        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.15)

        i_vec = Vector(M[:, 0], color=self.basis_i_color)
        j_vec = Vector(M[:, 1], color=self.basis_j_color)
        k_vec = Vector(M[:, 2], color=self.basis_k_color)

        self.play(
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(helper)
        )

        self.wait()

        projection_vectors = []

        q = None

        for (action, payload) in gram_schmidt(M):

            if action == Action.UPDATE_MATRIX_REMOVE_Q:

                assert not q is None

                M_rounded = np.round(M.copy(), 2)
                
                self.remove(matrix)

                matrix = self.create_matrix(M_rounded)

                self.add_fixed_in_frame_mobjects(matrix)

                i_vec_new = Vector(M[:, 0], color=self.basis_i_color)
                j_vec_new = Vector(M[:, 1], color=self.basis_j_color)
                k_vec_new = Vector(M[:, 2], color=self.basis_k_color)

                animation_time = 2.0

                self.play(
                    FadeOut(q, run_time=animation_time * 0.75),
                    ReplacementTransform(i_vec, i_vec_new, run_time=animation_time),
                    ReplacementTransform(j_vec, j_vec_new, run_time=animation_time),
                    ReplacementTransform(k_vec, k_vec_new, run_time=animation_time)
                )

                self.wait()

                i_vec, j_vec, k_vec = i_vec_new, j_vec_new, k_vec_new

            elif action == Action.ADD_PROJECTION:

                p = Vector(payload, color=self.projection_color)

                projection_vectors.append(p)

                self.play(GrowArrow(p))

                self.wait()

                if len(projection_vectors) == 2:

                    first_projection_end = projection_vectors[0].get_end()

                    p_shifted = Arrow(first_projection_end, first_projection_end + payload, buff=0, color=self.projection_color)

                    projection_vectors[1] = p_shifted

                    self.play(ReplacementTransform(p, p_shifted))

                    self.wait()

            elif action == Action.REMOVE_PROJECTIONS_SET_Q:

                if not projection_vectors:

                    q = Vector(payload, color=self.q_color)

                    self.play(GrowArrow(q))

                    self.wait()

                    continue

                last_projection_end = projection_vectors[len(projection_vectors) - 1].get_end()

                q_shifted = Arrow(last_projection_end, last_projection_end + payload, buff=0, color=self.q_shifted_color)

                self.play(GrowArrow(q_shifted))

                self.wait()

                q = Vector(payload, color=self.q_color)

                self.play(
                    ReplacementTransform(q_shifted, q),
                    *[FadeOut(p) for p in projection_vectors]
                )

                self.wait()

                projection_vectors = []

            elif action == Action.NORMALIZE_Q:

                q_normalized = Vector(payload, color=self.q_color)

                self.play(ReplacementTransform(q, q_normalized))

                self.wait()

                q = q_normalized

            else:
                assert False

            self.wait(1)

        assert np.allclose(M.T @ M, np.identity(3))

        self.wait(15)
