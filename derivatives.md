---
layout: page
text: Derivatives cheat sheet
---

This document includes an overview of derivatives of functions I will need to use. Kind of like a personal, very specific, math cheat sheet.

Some derivatives will be available in a "general representation", and as a "matrix representation".  With a general representation, I intend the notational representation of a function as other functions would be notated in that domain.  For its matrix representation, the partial derivative $$\partial_\mathbf{x} f = \frac{\partial f}{\partial \mathbf{x}}$$ of a function $$f(\mathbf{x}, \ldots)$$ with $$n$$-dimensional result and an $$m$$-dimensional vector $$\mathbf{x}$$, is decomposed to a linear mapping of its partial derivatives $$\frac{\partial f_i}{\partial x_j}$$ with $$0 \leq i < n$$ and $$0 \leq j < m$$.  This is equivalent to an $$n \times m$$ matrix $$F$$ with partial derivative $$\frac{\partial f_i}{\partial x_j}$$ at the $$i$$th row and $$j$$th column. For an example, please see the quaternion product.

## Basic/helper derivatives

### Vector norm

$$ \begin{align}
\partial_\mathbf{v} \|\mathbf{v}\|
    &= \frac{\mathbf{v}^\intercal}{\|\mathbf{v}\|}
\end{align}
$$

### Quaternion product

$$
\begin{align}
\mathbf{p} \odot \mathbf{q}
  &= \phantom{+} (q_0 p_0 - q_1 p_1 - q_2 p_2 - q_3 p_3)            \\
  &\phantom{=} + (q_0 p_1 + q_1 p_0 - q_2 p_3 + q_3 p_2) \mathbf{i} \\
  &\phantom{=} + (q_0 p_2 + q_1 p_3 + q_2 p_0 - q_3 p_1) \mathbf{j} \\
  &\phantom{=} + (q_0 p_3 - q_1 p_2 + q_2 p_1 + q_3 p_0) \mathbf{k} \\
\end{align}
$$
$$
\begin{align}
\begin{split}
\partial_\mathbf{p} (\mathbf{p} \odot \mathbf{q})
  &= \phantom{+} (q_0 - q_1 - q_2 - q_3) \\
  &\phantom{=} + (q_1 + q_0 + q_3 - q_2) \mathbf{i} \\
  &\phantom{=} + (q_2 - q_3 + q_0 + q_1) \mathbf{j} \\
  &\phantom{=} + (q_3 + q_2 - q_1 + q_0) \mathbf{k} \\
  &= \phantom{+} (q_0 - q_1 - q_2 - q_3) \\
  &\phantom{=} + (q_0 + q_1 - q_2 + q_3) \mathbf{i} \\
  &\phantom{=} + (q_0 + q_1 + q_2 - q_3) \mathbf{j} \\
  &\phantom{=} + (q_0 - q_1 + q_2 + q_3) \mathbf{k} \\
\end{split}
\begin{split}
\partial_\mathbf{q} (\mathbf{p} \odot \mathbf{q})
  &= \phantom{+} (p_0 - p_1 - p_2 - p_3) \\
  &\phantom{=} + (p_1 + p_0 - p_3 + p_2) \mathbf{i} \\
  &\phantom{=} + (p_2 + p_3 + p_0 - p_1) \mathbf{j} \\
  &\phantom{=} + (p_3 - p_2 + p_1 + p_0) \mathbf{k} \\
  &= \phantom{+} (p_0 - p_1 - p_2 - p_3) \\
  &\phantom{=} + (p_0 + p_1 + p_2 - p_3) \mathbf{i} \\
  &\phantom{=} + (p_0 - p_1 + p_2 + p_3) \mathbf{j} \\
  &\phantom{=} + (p_0 + p_1 - p_2 + p_3) \mathbf{k} \\
\end{split}
\end{align}
$$

In matrix representation (smallest element partial derivatives), with $$f(\mathbf{p}, \mathbf{q}) = \mathbf{p} \odot \mathbf{q}$$:

$$
\begin{align}
\begin{split}
\partial_\mathbf{p} f
  &= \begin{bmatrix} 
         \frac{\partial f}{\partial p_0} 
       & \frac{\partial f}{\partial p_1} 
       & \frac{\partial f}{\partial p_2}
       & \frac{\partial f}{\partial p_3}
     \end{bmatrix} \\
  &= \begin{bmatrix}
         \frac{\partial f_0}{\partial p_0} 
       & \frac{\partial f_0}{\partial p_1} 
       & \frac{\partial f_0}{\partial p_2}
       & \frac{\partial f_0}{\partial p_3} \\
         \frac{\partial f_1}{\partial p_0} 
       & \frac{\partial f_1}{\partial p_1} 
       & \frac{\partial f_1}{\partial p_2}
       & \frac{\partial f_1}{\partial p_3} \\
         \frac{\partial f_2}{\partial p_0} 
       & \frac{\partial f_2}{\partial p_1} 
       & \frac{\partial f_2}{\partial p_2}
       & \frac{\partial f_2}{\partial p_3} \\
         \frac{\partial f_3}{\partial p_0} 
       & \frac{\partial f_3}{\partial p_1} 
       & \frac{\partial f_3}{\partial p_2}
       & \frac{\partial f_3}{\partial p_3}
     \end{bmatrix} \\
  &= \begin{bmatrix}
       q_0 & -q_1 & -q_2 & -q_3 \\
       q_1 &  q_0 &  q_3 & -q_2 \\
       q_2 & -q_3 &  q_0 &  q_1 \\
       q_3 &  q_2 & -q_1 &  q_0
    \end{bmatrix}
\end{split}
%
\begin{split}
\partial_\mathbf{q} f
  &= \begin{bmatrix} 
         \frac{\partial f}{\partial q_0} 
       & \frac{\partial f}{\partial q_1} 
       & \frac{\partial f}{\partial q_2}
       & \frac{\partial f}{\partial q_3}
     \end{bmatrix} \\
  &= \begin{bmatrix}
         \frac{\partial f_0}{\partial q_0} 
       & \frac{\partial f_0}{\partial q_1} 
       & \frac{\partial f_0}{\partial q_2}
       & \frac{\partial f_0}{\partial q_3} \\
         \frac{\partial f_1}{\partial q_0} 
       & \frac{\partial f_1}{\partial q_1} 
       & \frac{\partial f_1}{\partial q_2}
       & \frac{\partial f_1}{\partial q_3} \\
         \frac{\partial f_2}{\partial q_0} 
       & \frac{\partial f_2}{\partial q_1} 
       & \frac{\partial f_2}{\partial q_2}
       & \frac{\partial f_2}{\partial q_3} \\
         \frac{\partial f_3}{\partial q_0} 
       & \frac{\partial f_3}{\partial q_1} 
       & \frac{\partial f_3}{\partial q_2}
       & \frac{\partial f_3}{\partial q_3}
     \end{bmatrix} \\
  &= \begin{bmatrix}
       p_0 & -p_1 & -p_2 & -p_3 \\
       p_1 &  p_0 & -p_3 &  p_2 \\
       p_2 &  p_3 &  p_0 & -p_1 \\
       p_3 & -p_2 &  p_1 &  p_0
    \end{bmatrix} \\
\end{split}
\end{align}
$$

### Quaternion exponential
Let $$\mathbf{v}_\Sigma = v_0 + \ldots + v_n$$ for an $$n$$-dimensional vector $$\mathbf{v}$$.

$$
\begin{align}
\partial_\mathbf{v} \exp(\mathbf{v}) 
  &= \begin{bmatrix}
       -\mathbf{v}_\Sigma \frac{\sin\|\mathbf{v}\|}{\|\mathbf{v}\|} \\
       \mathbf{v} \mathbf{v}_\Sigma \frac{\|\mathbf{v}\| \cos\|\mathbf{v}\| - \frac{\sin\|\mathbf{v}\|}{\|\mathbf{v}\|}}{\mathbf{v} \cdot \mathbf{v}} + \frac{\sin\|\mathbf{v}\|}{\|\mathbf{v}\|}
    \end{bmatrix} \\
  &= \begin{bmatrix}
       -\mathbf{v}_\Sigma s \\
       \mathbf{v} \mathbf{v}_\Sigma \frac{\|\mathbf{v}\| c - s}{\mathbf{v} \cdot \mathbf{v}} + s
     \end{bmatrix} \\
  &= -\mathbf{v}_\Sigma s + \left(v_0\mathbf{i} + v_1\mathbf{j} + v_2\mathbf{k}\right)\left(\mathbf{v}_\Sigma \frac{\|\mathbf{v}\| c - s}{\mathbf{v} \cdot \mathbf{v}} + s\right)\\
  &\phantom{=}\mbox{ with } c = \cos\|\mathbf{v}\|\\
  &\phantom{=\mbox{ with }} s = \frac{\sin\|\mathbf{v}\|}{\|\mathbf{v}\|}
\end{align}
$$

In matrix representation (smallest element partial derivatives), with $$f(\mathbf{v}) = \exp(\mathbf{v})$$:

$$
\begin{align}
\partial_\mathbf{v} f
  &= \begin{bmatrix}
         \frac{\partial f}{\partial v_0} 
       & \frac{\partial f}{\partial v_1} 
       & \frac{\partial f}{\partial v_2}
     \end{bmatrix} \\
  &= \begin{bmatrix}
         \frac{\partial f_0}{\partial v_0} 
       & \frac{\partial f_0}{\partial v_1} 
       & \frac{\partial f_0}{\partial v_2} \\
         \frac{\partial f_1}{\partial v_0} 
       & \frac{\partial f_1}{\partial v_1} 
       & \frac{\partial f_1}{\partial v_2} \\
         \frac{\partial f_2}{\partial v_0} 
       & \frac{\partial f_2}{\partial v_1} 
       & \frac{\partial f_2}{\partial v_2} \\
         \frac{\partial f_3}{\partial v_0} 
       & \frac{\partial f_3}{\partial v_1} 
       & \frac{\partial f_3}{\partial v_2} \\
     \end{bmatrix} \\
  &= \begin{bmatrix}
       -v_0 s & -v_1 s & -v_2 s \\
       \frac{v_0^2}{\mathbf{v}\cdot\mathbf{v}} c - \frac{v_0^2}{\|\mathbf{v}\|^3} + s
         & \frac{v_0 v_1}{\mathbf{v}\cdot\mathbf{v}} \left(c - s\right)
         & \frac{v_0 v_2}{\mathbf{v}\cdot\mathbf{v}} \left(c - s\right) \\
       \frac{v_0 v_1}{\mathbf{v}\cdot\mathbf{v}} \left(c - s\right)
         & \frac{v_1^2}{\mathbf{v}\cdot\mathbf{v}} c - \frac{v_1^2}{\|\mathbf{v}\|^3} + s
         & \frac{v_1 v_2}{\mathbf{v}\cdot\mathbf{v}} \left(c - s\right) \\
       \frac{v_0 v_2}{\mathbf{v}\cdot\mathbf{v}} \left(c - s\right)
         & \frac{v_1 v_2}{\mathbf{v}\cdot\mathbf{v}} \left(c - s\right)
         & \frac{v_2^2}{\mathbf{v}\cdot\mathbf{v}} c - \frac{v_2^2}{\|\mathbf{v}\|^3} + s
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } c = \cos\|\mathbf{v}\|\\
  &\phantom{=\mbox{ with }} s = \frac{\sin\|\mathbf{v}\|}{\|\mathbf{v}\|}
\end{align}
$$

### Rotation

Let $$Q = \begin{bmatrix}1 - 2(q_2^2 + q_3^2) & 2(q_1q_2 - q_3q_0) & 2(q_1q_3 + q_2q_0) \\ 2(q_1q_2 + q_3q_0) & 1 - 2(q_1^2+q_3^2) & 2(q_2q_3 - q_1q_0) \\ 2(q_1 q_3 - q_2 q_0) & 2(q_2q_3 + q_1q_0) & 1 - 2(q_1^2 + q_2^2)\end{bmatrix}$$ be the rotation matrix corresponding to the same rotation as unit quaternion $$\mathbf{q}$$, and let $$Q^*$$ correspond to the rotation of $$\mathbf{q}^*$$.  The derivatives $$\partial_\mathbf{q} Q$$ and $$\partial_\mathbf{q} Q^*$$ are both third-rank tensors (mappings of mappings; see also [Wikipedia](https://en.wikipedia.org/wiki/Matrix_calculus#Other_matrix_derivatives)).

$$
\begin{align}
\partial_\mathbf{q} Q 
    &= \begin{bmatrix}
        \frac{\partial Q}{\partial q_0} & \frac{\partial Q}{\partial q_1} & \frac{\partial Q}{\partial q_2} & \frac{\partial Q}{q_3}
    \end{bmatrix}
\end{align}
$$

Each element $$\frac{\partial Q}{\partial q_i}$$ is a second-rank tensor, and can be represented by $$3 \times 3$$ matrices:

$$
\begin{align}
\begin{split}
\frac{\partial Q}{\partial q_0}
    &= \begin{bmatrix}
            0 &  2q_3 & -2q_2 \\
        -2q_3 &     0 &  2q_1 \\
         2q_2 & -2q_1 &     0 \\
    \end{bmatrix} \\
\frac{\partial Q}{\partial q_1}
    &= \begin{bmatrix}
            0 &  2q_2 &  2q_3 \\
         2q_2 & -4q_1 &  2q_0 \\
         2q_3 & -2q_0 & -4q_1 \\
    \end{bmatrix} \\
\frac{\partial Q}{\partial q_2}
    &= \begin{bmatrix}
        -4q_2 &  2q_1 & -2q_0 \\
         2q_1 &     0 &  2q_3 \\
         2q_0 &  2q_3 & -4q_2 \\
    \end{bmatrix} \\
\frac{\partial Q}{\partial q_3}
    &= \begin{bmatrix}
        -4q_3 &  2q_0 &  2q_1 \\
        -2q_0 & -4q_3 &  2q_2 \\
         2q_1 &  2q_2 &     0 \\
    \end{bmatrix} \\
\end{split}
\begin{split}
\frac{\partial Q^*}{\partial q_0}
    &= \begin{bmatrix}
            0 & -2q_3 &  2q_2 \\
         2q_3 &     0 & -2q_1 \\
        -2q_2 &  2q_1 &     0 \\
    \end{bmatrix} \\
\frac{\partial Q^*}{\partial q_1}
    &= \begin{bmatrix}
            0 &  2q_2 &  2q_3 \\
         2q_2 & -4q_1 & -2q_0 \\
         2q_3 &  2q_0 & -4q_1 \\
    \end{bmatrix} \\
\frac{\partial Q^*}{\partial q_2}
    &= \begin{bmatrix}
        -4q_2 &  2q_1 &  2q_0 \\
         2q_1 &     0 &  2q_3 \\
        -2q_0 &  2q_3 & -4q_2 \\
    \end{bmatrix} \\
\frac{\partial Q^*}{\partial q_3}
    &= \begin{bmatrix}
        -4q_3 & -2q_0 &  2q_1 \\
         2q_0 & -4q_3 &  2q_2 \\
         2q_1 &  2q_2 &     0 \\
    \end{bmatrix} \\
\end{split}
\end{align}
$$

When applied to a vector $$\mathbf{v}$$, both rotation derivatives will produce a regular vector.

-----------

## Bleser Model 1 (gyro)

Given are state, process noise, observation and observation noise:

$$
\begin{align}
\mathbf{x}_t &= \begin{bmatrix} \mathbf{s}_{w,t} \\
                                \dot{\mathbf{s}}_{w,t} \\
                                \mathbf{q}_{sw,t} \\
                                \mathbf{\omega}_{s,t} \\
                                \mathbf{b}^\omega_{s,t}
                \end{bmatrix} &
\mathbf{v}_t &= \begin{bmatrix}\mathbf{v}^\ddot{s}_{w,t} \\
                               \mathbf{v}^\omega_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^\omega}_{s,t}
                \end{bmatrix} &
\mathbf{y}_t &= \begin{bmatrix} \mathbf{y}^c_t \\
                                \mathbf{y}^\omega_t
                \end{bmatrix} &
\mathbf{e}_t &= \begin{bmatrix} \mathbf{e}^c_t \\
                                \mathbf{e}^\omega_t \\
                \end{bmatrix}
              = \begin{bmatrix} \mathbf{e}^c_{n,t} \\
                                \mathbf{e}^c_{w,t} \\
                                \mathbf{e}^\omega_t \\
                \end{bmatrix}
\end{align}
$$

### State transition function

$$
\begin{align}
f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
  &= \begin{bmatrix} \mathbf{s}_{w,t-T} + T \dot{\mathbf{s}}_{w,t-T} + \frac{T^2}{2} \mathbf{v}^\ddot{s}_{w,t} \\
                     \dot{\mathbf{s}}_{w,t-T} + T \mathbf{v}^\ddot{s}_{w,t} \\
                     \exp\left( -\frac{T}{2} (\omega_{s,t-T} + \mathbf{v}^\omega_{s,t}) \right) \odot \mathbf{q}_{sw,t-T} \\
                     \mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t} \\
                     \mathbf{b}^\omega_{s,t-T} + \mathbf{v}^{\mathbf{b}^\omega}_{s,t}
     \end{bmatrix} \\
\partial_\mathbf{x} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
  &= \begin{bmatrix} I_3 & T I_3 & 0 & 0   & 0 \\
                     0   & I_3   & 0 & 0   & 0 \\
                     0   & 0     & \partial_{\mathbf{q}_{sw}} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw} \right) & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}_{s,t-T}\right) & 0 \\
                     0   & 0     & 0 & I_3 & 0 \\
                     0   & 0     & 0 & 0   & I_3
     \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
  &= \begin{bmatrix} \frac{T^2}{2} I_3 & 0                                                 & 0 \\
                     T I_3             & 0                                                 & 0 \\
                     0                 & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{v}^{\omega_{s,t-T}}\right) & 0 \\
                     0                 & I_3                                                                      & 0 \\
                     0                 & 0                                                                        & I_3
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } \mathbf{a} = \frac{T}{2}(\mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t})\\
  &\phantom{=\mbox{ with }} \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}\right) = \frac{\partial \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}}{\partial \exp(\mathbf{a})} \frac{\partial \exp(\mathbf{a})}{\partial \mathbf{a}} \frac{\partial \mathbf{a}}{\partial \mathbf{\omega}} \\
  &\phantom{=\mbox{ with } \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}\right)} = \left(\partial_{\exp(\mathbf{a})} \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \left(\partial_\mathbf{a} \exp(\mathbf{a})\right) \frac{T}{2} I_3
\end{align}
$$

Use matrix representations in $$\mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}}$$!

### Measurement model

$$
\begin{align}
\mathbf{y}^\omega_{s,t}
  &= h^\omega(\mathbf{x}_t, \mathbf{e}^\omega_{s,t}) \\
  &= \mathbf{\omega}_{s,t} + \mathbf{b}^\omega_{s,t} + \mathbf{e}^\omega_{s,t} \\
%
\partial_\mathbf{x} h^\omega(\mathbf{x}_t, \mathbf{e}^\omega_{s,t})
  &= \begin{bmatrix} 0 & 0 & 0 & I_3 & I_3 \end{bmatrix} \\

\partial_\mathbf{e} h^\omega(\mathbf{x}_t, \mathbf{e}^\omega_{s,t})
  &= \begin{bmatrix} I_3 & 0 \end{bmatrix} \\
%
h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(Q_{sw,t} \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right) - \mathbf{c}_s\right) + \mathbf{e}^c_t \\
%
\partial_\mathbf{x} h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \begin{bmatrix} \partial_\mathbf{s} h^c & 0 & \partial_\mathbf{q} h^c & 0  & 0 \end{bmatrix}(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t) \\
%
\partial_\mathbf{s} h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(Q_{sw,t} \left(\partial_\mathbf{s} \mathbf{m}_{w,t} - \partial_\mathbf{s} \mathbf{s}_{w,t}\right) - \partial_\mathbf{s} \mathbf{c}_s\right) + \partial_\mathbf{s} \mathbf{e}^c_t \\
  &= \begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} Q_{sw,t} \left(-I_3\right) \\
  &= -\begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} Q_{sw,t}  \\
%
\partial_\mathbf{q} h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \begin{bmatrix}I_2 & \mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(\left(\partial_\mathbf{q} Q_{sw,t} \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right)\right) - \partial_\mathbf{q} \mathbf{c}_s\right) + \partial_\mathbf{q} \mathbf{e}^c_t \\
  &= \begin{bmatrix}I_2 & \mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(\left(\partial_\mathbf{q} Q_{sw,t} \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right)\right) - 0 \right) + 0 \\
  &= \begin{bmatrix}I_2 & \mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(\partial_\mathbf{q} Q_{sw,t}\right) \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right) \\
%
\partial_{\mathbf{e}^c} h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \partial_{\mathbf{e}^c} \left(\begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(Q_{sw,t} \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right) - \mathbf{c}_s\right)\right) + \partial_{\mathbf{e}^c} \mathbf{e}^c_t \\
  &= 0 + I_3 \\
  &= I_3 \\
\end{align}
$$

To compute the camera measurement covariance $$R^c_t \approx \begin{bmatrix}\partial_{\mathbf{m}_{n,t}} h^c_t & \partial_{\mathbf{m}_{w,t}} h^c_t\end{bmatrix} \begin{bmatrix}R_{nn,t} & 0_{2 \times 3} \\ 0_{3 \times 2} & R_{ww,t} \end{bmatrix} \begin{bmatrix}\left(\partial_{\mathbf{m}_{n,t}} h^c_t\right)^\top \\ \left(\partial_{\mathbf{m}_{w,t}} h^c_t\right)^\top\end{bmatrix}$$, we need to know two more derivatives:

$$
\begin{align}
\partial_{\mathbf{m}_n} h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \left(\partial_{\mathbf{m}_n} \begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix}\right) Q_{cs} \left(Q_{sw,t} \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right) - \mathbf{c}_s\right) + 0 \\
  &= \begin{bmatrix}0_{2 \times 2} & -1_{2 \times 1}\end{bmatrix} Q_{cs} \left(Q_{sw,t} \left(\mathbf{m}_{w,t} - \mathbf{s}_{w,t}\right) - \mathbf{c}_s\right) \\
%
\partial_{\mathbf{m}_w} h^c(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_t)
  &= \begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} \left(Q_{sw,t} \left(\partial_{\mathbf{m}_w} \mathbf{m}_{w,t} - \partial_{\mathbf{m}_w} \mathbf{s}_{w,t}\right) - \partial_{\mathbf{m}_w} \mathbf{c}_s\right) + \partial_{\mathbf{m}_w} \mathbf{e}^c_t \\
  &= \begin{bmatrix}I_2 & -\mathbf{m}_{n,t}\end{bmatrix} Q_{cs} Q_{sw,t} I_3 \\
\end{align}
$$


## Bleser, Model 2 (gravity)

Given are state, process noise, observation and observation noise:

$$
\begin{align}
\mathbf{x}_t &= \begin{bmatrix} \mathbf{s}_{w,t} \\
                                \dot{\mathbf{s}}_{w,t} \\
                                \mathbf{q}_{sw,t} \\
                                \mathbf{\omega}_{s,t} \\
                                \mathbf{b}^\omega_{s,t} \\
                                \mathbf{b}^a_{s,t}
                \end{bmatrix} &
\mathbf{v}_t &= \begin{bmatrix}\mathbf{v}^\ddot{s}_{w,t} \\
                               \mathbf{v}^\omega_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^a}_{s,t}
                \end{bmatrix} &
\mathbf{y}_t &= \begin{bmatrix} \mathbf{y}^c_t \\
                                \mathbf{y}^\omega_t \\
                                \mathbf{y}^a_t
                \end{bmatrix} &
\mathbf{e}_t &= \begin{bmatrix} \mathbf{e}^c_t \\
                                \mathbf{e}^\omega_t \\
                                \mathbf{e}^a_t
                \end{bmatrix}
\end{align}
$$

### State transition function

$$
\begin{align}
f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
  &= \begin{bmatrix} \mathbf{s}_{w,t-T} + T \dot{\mathbf{s}}_{w,t-T} + \frac{T^2}{2} \mathbf{v}^\ddot{s}_{w,t} \\
                     \dot{\mathbf{s}}_{w,t-T} + T \mathbf{v}^\ddot{s}_{w,t} \\
                     \exp\left( -\frac{T}{2} (\omega_{s,t-T} + \mathbf{v}^\omega_{s,t}) \right) \odot \mathbf{q}_{sw,t-T} \\
                     \mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t} \\
                     \mathbf{b}^\omega_{s,t-T} + \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
                     \mathbf{b}^a_{s,t-T} + \mathbf{v}^{\mathbf{b}^a}_{s,t}
     \end{bmatrix} \\
\partial_\mathbf{x} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} %
        I_3 & T I_3 & 0 & 0   & 0   & 0\\
        0   & I_3   & 0 & 0   & 0   & 0\\
        0   & 0     & \partial_{\mathbf{q}_{sw}} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw} \right) & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}_{s,t-T}\right) & 0   & 0\\
        0   & 0     & 0 & I_3 & 0   & 0 \\
        0   & 0     & 0 & 0   & I_3 & 0 \\
        0   & 0     & 0 & 0   & 0   & I_3 \\
    \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        \frac{T^2}{2} I_3 & 0                                                                        & 0   & 0 \\
        T I_3             & 0                                                                        & 0   & 0 \\
        0                 & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{v}^{\omega_{s,t-T}}\right) & 0   & 0 \\
        0                 & I_3                                                                      & 0   & 0 \\
        0                 & 0                                                                        & I_3 & 0 \\
        0                 & 0                                                                        & 0   & I_3 \\
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } \mathbf{a} = \frac{T}{2}(\mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t})\\
  &\phantom{=\mbox{ with }} \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}\right) = \frac{\partial \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}}{\partial \exp(\mathbf{a})} \frac{\partial \exp(\mathbf{a})}{\partial \mathbf{a}} \frac{\partial \mathbf{a}}{\partial \mathbf{\omega}} \\
  &\phantom{=\mbox{ with } \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}\right)} = \left(\partial_{\exp(\mathbf{a})} \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \left(\partial_\mathbf{a} \exp(\mathbf{a})\right) \frac{T}{2} I_3
\end{align}
$$

### Measurement model

For $$\mathbf{y}^c_t$$, $$\mathbf{y}^\omega_t$$, $$\mathbf{e}^c_t$$ and $$\mathbf{e}^\omega_t$$, please see above.

$$
\begin{align}
\mathbf{y}^a_{s,t}
  &= h^a(\mathbf{x}_t, \mathbf{e}^a_t) \\
  &= -\left(Q_{sw,t} \mathbf{g}_w\right) + \mathbf{b}^a_{s,t} + \mathbf{e}^a_{s,t} \\
%
\partial_\mathbf{x} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= \begin{bmatrix} 0 & 0 & \partial_\mathbf{q} h^a & 0 & 0 & \partial_{\mathbf{b}^a} h^a \end{bmatrix}(\mathbf{x}_t, \mathbf{e}^a_t) \\
%
\partial_\mathbf{q} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= -\left(\partial_\mathbf{q} Q_{sw,t} \right) \mathbf{g}_w \\
%
\partial_{\mathbf{b}^a} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= I_3 \\
%
\partial_{\mathbf{e}^a} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= I_3 \\
\end{align}
$$


## Bleser Model 3 (acc)

Given are state, process noise, observation and observation noise:

$$
\begin{align}
\mathbf{x}_t &= \begin{bmatrix} \mathbf{s}_{w,t} \\
                                \dot{\mathbf{s}}_{w,t} \\
                                \ddot{\mathbf{s}}_{w,t} \\
                                \mathbf{q}_{sw,t} \\
                                \mathbf{\omega}_{s,t} \\
                                \mathbf{b}^\omega_{s,t} \\
                                \mathbf{b}^a_{s,t}
                \end{bmatrix} &
\mathbf{v}_t &= \begin{bmatrix}\mathbf{v}^\ddot{s}_{w,t} \\
                               \mathbf{v}^\omega_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^a}_{s,t}
                \end{bmatrix} &
\mathbf{y}_t &= \begin{bmatrix} \mathbf{y}^c_t \\
                                \mathbf{y}^\omega_t \\
                                \mathbf{y}^a_t
                \end{bmatrix} &
\mathbf{e}_t &= \begin{bmatrix} \mathbf{e}^c_t \\
                                \mathbf{e}^\omega_t \\
                                \mathbf{e}^a_t
                \end{bmatrix}
\end{align}
$$

### State transition function

$$
\begin{align}
f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        \mathbf{s}_{w,t-T} + T \dot{\mathbf{s}}_{w,t-T} + \frac{T^2}{2} \left(\ddot{\mathbf{s}}_{w,t-T} + \mathbf{v}^\ddot{s}_{w,t} \right) \\
        \dot{\mathbf{s}}_{w,t-T} + T \left(\ddot{s}_{w,t-T} + \mathbf{v}^\ddot{\mathbf{s}}_{w,t} \right) \\
        \ddot{\mathbf{s}}_{w,t-T} + \mathbf{v}^{\ddot{\mathbf{s}}}_{w,t} \\
        \exp\left( -\frac{T}{2} (\omega_{s,t-T} + \mathbf{v}^\omega_{s,t}) \right) \odot \mathbf{q}_{sw,t-T} \\
        \mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t} \\
        \mathbf{b}^\omega_{s,t-T} + \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
        \mathbf{b}^a_{s,t-T} + \mathbf{v}^{\mathbf{b}^a}_{s,t}
    \end{bmatrix} \\
\partial_\mathbf{x} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} %
        I_3 & T I_3 & \frac{T^2}{2} I_3   & 0 & 0   & 0   & 0\\
        0   & I_3   & T I_3               & 0 & 0   & 0   & 0\\
        0   & 0     & I_3                 & \partial_{\mathbf{q}_{sw}} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw} \right) & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}_{s,t-T}\right) & 0   & 0\\
        0   & 0     & 0                   & 0 & I_3 & 0   & 0 \\
        0   & 0     & 0                   & 0 & 0   & I_3 & 0 \\
        0   & 0     & 0                   & 0 & 0   & 0   & I_3 \\
    \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        \frac{T^2}{2} I_3 & 0                                                                        & 0   & 0 \\
        T I_3             & 0                                                                        & 0   & 0 \\
        I_3               & 0                                                                        & 0   & 0 \\
        0                 & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{v}^{\omega_{s,t-T}}\right) & 0   & 0 \\
        0                 & I_3                                                                      & 0   & 0 \\
        0                 & 0                                                                        & I_3 & 0 \\
        0                 & 0                                                                        & 0   & I_3 \\
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } \mathbf{a} = \frac{T}{2}(\mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t})\\
  &\phantom{=\mbox{ with }} \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}\right) = \frac{\partial \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}}{\partial \exp(\mathbf{a})} \frac{\partial \exp(\mathbf{a})}{\partial \mathbf{a}} \frac{\partial \mathbf{a}}{\partial \mathbf{\omega}} \\
  &\phantom{=\mbox{ with } \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\mathbf{\omega}\right)} = \left(\partial_{\exp(\mathbf{a})} \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \left(\partial_\mathbf{a} \exp(\mathbf{a})\right) \frac{T}{2} I_3
\end{align}
$$

### Measurement model

For $$\mathbf{y}^c_t$$, $$\mathbf{y}^\omega_t$$, $$\mathbf{e}^c_t$$ and $$\mathbf{e}^\omega_t$$, please see above.

$$
\begin{align}
\mathbf{y}^a_{s,t}
  &= h^a(\mathbf{x}_t, \mathbf{e}^a_t) \\
  &= Q_{sw,t}\left(\ddot{\mathbf{s}}_{w,t} - \mathbf{g}_w\right) + \mathbf{b}^a_{s,t} + \mathbf{e}^a_{s,t} \\
%
\partial_\mathbf{x} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= \begin{bmatrix} 0 & 0 & \partial_{\ddot{\mathbf{s}}_{w,t}} h^a & \partial_\mathbf{q} h^a & 0 & 0 & \partial_{\mathbf{b}^a} h^a \end{bmatrix}(\mathbf{x}_t, \mathbf{e}^a_t) \\
%
\partial_{\ddot{\mathbf{s}}} h^a(\mathbf{x}_t, \mathbf{e}^a_t)
  &= Q_{sw,t} \\
\partial_\mathbf{q} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= \left(\partial_\mathbf{q} Q_{sw,t} \right) \left(\ddot{\mathbf{s}}_{w,t} - \mathbf{g}_w\right) \\
%
\partial_{\mathbf{b}^a} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= I_3 \\
%
\partial_{\mathbf{e}^a} h^a(\mathbf{x}_t, \mathbf{e}^a_t) 
  &= I_3 \\
\end{align}
$$

## Bleser Model 4 (acc input)

Given are control vector, state, process noise, observation and observation noise:

$$
\begin{align}
\mathbf{u}_t &= \begin{bmatrix} \mathbf{y}^\omega_s \\
                                \mathbf{y}^a_s
                \end{bmatrix} &
\mathbf{x}_t &= \begin{bmatrix} \mathbf{s}_{w,t} \\
                                \dot{\mathbf{s}}_{w,t} \\
                                \mathbf{q}_{sw,t} \\
                                \mathbf{b}^\omega_{s,t} \\
                                \mathbf{b}^a_{s,t}
                \end{bmatrix} &
\mathbf{v}_t &= \begin{bmatrix}\mathbf{v}^a_{w,t} \\
                               \mathbf{v}^\omega_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
                               \mathbf{v}^{\mathbf{b}^a}_{s,t}
                \end{bmatrix} &
\mathbf{y}_t &= \begin{bmatrix} \mathbf{y}^c_t \\
                \end{bmatrix} &
\mathbf{e}_t &= \begin{bmatrix} \mathbf{e}^c_t \\
                \end{bmatrix}
\end{align}
$$

### State transition function

**Note:** If $$\mathbf{q}_{sw}$$ represents the rotation from frame $$w$$ to frame $$s$$, then rotating from frame $$s$$ to frame $$w$$ is represented by $$\mathbf{q}_{ws} = \mathbf{q}_{sw}^*$$.

$$
\begin{align}
f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix}
        \mathbf{s}_{w,t-T} + T \dot{\mathbf{s}}_{w,t-T} + \frac{T^2}{2} Q_{ws,t-T} \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right) + \frac{T^2}{2} \mathbf{g}_w \\
        \dot{\mathbf{s}}_{w,t-T} + T Q_{ws,t-T} \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right) + T \mathbf{g}_w \\
        \exp\left(-\frac{T}{2} \left(\mathbf{y}^\omega_{s,t} - \mathbf{b}^\omega_{s,t-T} - \mathbf{v}^\omega_{s,t}\right)\right) \odot \mathbf{q}_{sw,t-T} \\
        \mathbf{b}^\omega_{s,t-T} + \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
        \mathbf{b}^a_{s,t-T} + \mathbf{v}^{\mathbf{b}^a}_{s,t}
    \end{bmatrix} \\
\partial_\mathbf{x} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix}
        I_3 & T I_3 & \frac{T^2}{2} \left(\partial_{\mathbf{q}_{sw,t-T}} Q_{sw,t-T}^* \right) \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right) & 0   & -\frac{T^2}{2} Q_{ws,t-T} \\
        0   & I_3   & T \left(\partial_{\mathbf{q}_{sw,t-T}} Q_{sw,t-T}^* \right) \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right)             & 0   & -T Q_{ws,t-T} \\
        0   & 0     & \partial_{\mathbf{q}_{sw,t-T}} \left(\exp\left(\mathbf{a}'\right) \odot \mathbf{q}_{sw,t-T}\right)                                                & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left({\mathbf{b}^\omega{s,t-T}}\right) & 0 \\
        0   & 0     & 0                                                                                                                                                 & I_3 & 0 \\
        0   & 0     & 0                                                                                                                                                 & 0   & I_3 \\
    \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} \\
       -\frac{T^2}{2} Q_{ws,t-T} & 0                                                                    & 0   & 0 \\
       -T Q_{ws,t-T}             & 0                                                                    & 0   & 0 \\
       0                         & \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left({\mathbf{v}^{\mathbf{b}^\omega_{s,t-T}}}\right) & 0   & 0 \\
       0                         & 0                                                                    & I_3 & 0 \\
       0                         & 0                                                                    & 0   & I_3 \\
    \end{bmatrix} \\
    &\phantom{=}\mbox{ with } \mathbf{a}' = \frac{T}{2}\left(\mathbf{y}^\omega_{s,t} - \mathbf{b}^\omega_{s,t} - \mathbf{v}^\omega_{s,t}\right) \\
    &\phantom{=\mbox{ with }} \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\omega\right) = \frac{\partial \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}}{\partial \exp(\mathbf{a})} \frac{\partial \exp(\mathbf{a})}{\partial \mathbf{a}} \frac{\partial \mathbf{a}}{\partial \mathbf{\omega}} \\
    &\phantom{=\mbox{ with } \mathbf{D}^{\mathbf{q}_{sw,t-T}}\left(\omega\right)} = \left(\partial_{\exp(\mathbf{a})} \exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \left(\partial_\mathbf{a} \exp(\mathbf{a})\right) \frac{T}{2} I_3
\end{align}
$$
