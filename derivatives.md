---
layout: page
text: Derivatives of formulas I use
---

Derivatives of some functions I need to use:

## Basic/helper derivatives

### Vector norm

$$
\begin{align}
\partial_\mathbf{v} \|\mathbf{v}\|
  &= \frac{\mathbf{v}}{\|\mathbf{v}\|}
\end{align}
$$

### Quaternion exponential
The trick here is to keep your values on the right basis; if you "blindly" differentiate the composed-vector-notation-version, you would get $$\begin{bmatrix}\frac{-\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| \\ \cos \|\mathbf{v}\| \end{bmatrix}$$.

With $$\mathbf{q}^* = q_0 - q_1 \mathbf{i} - q_2 \mathbf{j} - q_3 \mathbf{k}$$ the [quaternion conjugate](http://mathworld.wolfram.com/QuaternionConjugate.html):

$$
\begin{align}
\partial_\mathbf{v} \exp(\mathbf{v}) 
  &= \partial_\mathbf{v} \begin{bmatrix} \cos \|\mathbf{v}\| \\ 
                                         \frac{\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| 
                         \end{bmatrix} \\
  &= \partial_\mathbf{v} \left( \cos \|\mathbf{v}\| + \frac{\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| \right) \\
  &= \partial_\mathbf{v} \|\mathbf{v}\| \partial_{\|\mathbf{v}\|} \cos \|\mathbf{v}\| + \left(\partial_\mathbf{v} \frac{\mathbf{v}}{\|\mathbf{v}\|}\right) \sin\|\mathbf{v}\| + \frac{\mathbf{v}}{\|\mathbf{v}\|} \partial_\mathbf{v} \sin\|\mathbf{v}\| \\
  &= -\frac{\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| + \frac{\partial_\mathbf{v} \mathbf{v} \|\mathbf{v}\| - \mathbf{v} \partial_\mathbf{v} \|\mathbf{v}\|}{\|\mathbf{v}\|^2} \sin \|\mathbf{v}\| + \frac{\mathbf{v}}{\|\mathbf{v}\|} \partial_\mathbf{v} \|\mathbf{v}\| \partial_{\|\mathbf{v}\|} \sin \|\mathbf{v}\| \\
  &= -\frac{\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| + \frac{\mathbf{I}_3 \|\mathbf{v}\| - \mathbf{v} \frac{\mathbf{v}}{\|\mathbf{v}\|}}{\|\mathbf{v}\|^2} \sin \|\mathbf{v}\| + \frac{\mathbf{v}}{\|\mathbf{v}\|} \frac{\mathbf{v}}{\|\mathbf{v}\|} \cos \|\mathbf{v}\| \\
  &= \frac{-\mathbf{v}\|\mathbf{v}\| + \mathbf{I}_3\|\mathbf{v}\| - \frac{\mathbf{v} \mathbf{v}}{\|\mathbf{v}\|}}{\|\mathbf{v}\|^2} \sin \|\mathbf{v}\| + \cos \|\mathbf{v}\| \\
  &= \frac{-\mathbf{v}\|\mathbf{v}\| + \mathbf{I}_3\|\mathbf{v}\| - \|\mathbf{v}\|}{\|\mathbf{v}\|^2} \sin \|\mathbf{v}\| + \cos \|\mathbf{v}\| \\
  &= \frac{-\mathbf{v} + \mathbf{I}_3 - 1}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| + \cos \|\mathbf{v}\| \\
  &= \frac{-\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| + \cos \|\mathbf{v}\| \\
  &= \begin{bmatrix} \cos \|\mathbf{v}\| \\ 
                     \frac{-\mathbf{v}}{\|\mathbf{v}\|} \sin \|\mathbf{v}\| 
     \end{bmatrix} \\
  &= \exp(\mathbf{v})^*
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
\partial_\mathbf{p} (\mathbf{p} \odot \mathbf{q})
  &= \phantom{+} (q_0 - q_1 - q_2 - q_3)            & 
                                                    \partial_\mathbf{q} (\mathbf{p} \odot \mathbf{q})
                                                        &= \phantom{+} (p_0 - p_1 - p_2 - p_3)            \\
  &\phantom{=} + (q_1 + q_0 + q_3 - q_2) \mathbf{i} &   &\phantom{=} + (p_1 + p_0 - p_3 + p_2) \mathbf{i} \\
  &\phantom{=} + (q_2 - q_3 + q_0 + q_1) \mathbf{j} &   &\phantom{=} + (p_2 + p_3 + p_0 - p_1) \mathbf{j} \\
  &\phantom{=} + (q_3 + q_2 - q_1 + q_0) \mathbf{k} &   &\phantom{=} + (p_3 - p_2 + p_1 + p_0) \mathbf{k} \\
  &= \phantom{+} (q_0 - q_1 - q_2 - q_3)            &   &= \phantom{+} (p_0 - p_1 - p_2 - p_3)            \\
  &\phantom{=} + (q_0 + q_1 - q_2 + q_3) \mathbf{i} &   &\phantom{=} + (p_0 + p_1 + p_2 - p_3) \mathbf{i} \\
  &\phantom{=} + (q_0 + q_1 + q_2 - q_3) \mathbf{j} &   &\phantom{=} + (p_0 - p_1 + p_2 + p_3) \mathbf{j} \\
  &\phantom{=} + (q_0 - q_1 + q_2 + q_3) \mathbf{k} &   &\phantom{=} + (p_0 + p_1 - p_2 + p_3) \mathbf{k} \\
\end{align}
$$

-----------

## Bleser Model 1 (gyro)

Given are state and process noise:

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
                     0   & 0     & \partial_{\mathbf{q}_{sw}} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw} \right) & \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} & 0 \\
                     0   & 0     & 0 & I_3 & 0 \\
                     0   & 0     & 0 & 0   & I_3
     \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
  &= \begin{bmatrix} \frac{T^2}{2} I_3 & 0                                        & 0 \\
                     T I_3             & 0                                        & 0 \\
                     0                 & \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} & 0 \\
                     0                 & I_3                                      & 0 \\
                     0                 & 0                                        & I_3
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } \mathbf{a} = \frac{T}{2}(\mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t})\\
  &\phantom{=\mbox{ with }} \mathbf{r} = \left( \partial_{\exp(\mathbf{a})} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \right) \left(-\frac{T}{2} \exp(\mathbf{a})\right)\\
  &\phantom{=\mbox{ with }} \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} = \begin{bmatrix} \mathbf{r}\mathbf{i} & \mathbf{r}\mathbf{j} & \mathbf{r}\mathbf{k} \end{bmatrix}\\
\end{align}
$$

### Measurement model

$$
\begin{align}
\mathbf{y}^\omega_{s,t}
  &= h(\mathbf{x}_t, \mathbf{e}^\omega_{s,t}) \\
  &= \mathbf{\omega}_{s,t} + \mathbf{b}^\omega_{s,t} + \mathbf{e}^\omega_{s,t} \\

\partial_\mathbf{x} h(\mathbf{x}_t, \mathbf{e}^\omega_{s,t})
  &= \begin{bmatrix} 0 & 0 & 0 & I_3 & I_3 \end{bmatrix} \\

\mathbf{e} 
  &= \begin{bmatrix} \mathbf{e}^\omega_{s,t} \\ 
                     \mathbf{e}^c_{n,t} \\ 
                     \mathbf{e}^c_{w,t}
     \end{bmatrix} \\

\partial_\mathbf{e} h(\mathbf{x}_t, \mathbf{e}^\omega_{s,t})
  &= \begin{bmatrix} I_3 & 0 & 0 \end{bmatrix} \\

h(\mathbf{x}_t, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}^c_{n,t}, \mathbf{e}^c_{w,t})
  &= \begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs} \left( Q_{sw,t} \left(\mathbf{m}_{w,t} + \mathbf{e}_{w,t}^c - \mathbf{s}_{w,t} \right) - \mathbf{c}_s \right) \\

\partial_\mathbf{x} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= \left(\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs}\right) \partial_\mathbf{x} \left( Q_{sw,t} \left(\mathbf{m}_{w,t} + \mathbf{e}_{w,t}^c - \mathbf{s}_{w,t} \right) - \mathbf{c}_s \right) \\
  &= \left(\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs}\right) \left( \partial_\mathbf{x} Q_{sw,t} \mathbf{m}_{w,t} + \partial_\mathbf{x} Q_{sw,t} \mathbf{e}_{w,t}^c - \partial_\mathbf{x} Q_{sw,t} \mathbf{s}_{w,t} - \partial_\mathbf{x} \mathbf{c}_s \right) \\
  &= \left(\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs}\right) \left( \mathbf{0} + \mathbf{0} - \partial_\mathbf{x} Q_{sw,t} \mathbf{s}_{w,t} - \mathbf{0} \right) \\
  &= \left(\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs}\right) \left(-Q_{sw,t} \begin{bmatrix}I_3 & \mathbf{0}_{3 \times \ldots} \end{bmatrix} \right) \\
  &= -\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs} Q_{sw,t} \begin{bmatrix}I_3 & 0 & 0 & 0 & 0 \end{bmatrix} \\

\partial_\mathbf{e} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= \begin{bmatrix} \partial_{\mathbf{e}^\omega_{s,t}} h & \partial_{\mathbf{e}^c_{n,t}} h & \partial_{\mathbf{e}^c_{w,t}} h \end{bmatrix}(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c) \\
\partial_{\mathbf{e}^\omega_{s,t}} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= 0_3 \\
\partial_{\mathbf{e}^c_{n,t}} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= \partial_{\mathbf{e}^c_{n,t}} \left(\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} \right) Q_{cs} \left( Q_{sw,t} \left(\mathbf{m}_{w,t} + \mathbf{e}_{w,t}^c - \mathbf{s}_{w,t} \right) - \mathbf{c}_s \right) \\
  &= \begin{bmatrix} I_2 & -\partial_{\mathbf{e}^c_{n,t}} \mathbf{e}_{n,t}^c \end{bmatrix} Q_{cs} \left( Q_{sw,t} \left(\mathbf{m}_{w,t} + \mathbf{e}_{w,t}^c - \mathbf{s}_{w,t} \right) - \mathbf{c}_s \right) \\
  &= \begin{bmatrix} \partial_{\mathbf{e}^c_{n,t,1}} & \partial_{\mathbf{e}^c_{n,t,2}} \end{bmatrix} \\
  &\phantom{=} \mbox{ with } \partial_{\mathbf{e}^c_{n,t,1}} = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 0 \end{bmatrix} \mathbf{b}, \\
  &\phantom{=\mbox{ with }} \partial_{\mathbf{e}^c_{n,t,2}} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & -1 \end{bmatrix} \mathbf{b}, \\
  &\phantom{=\mbox{ with }} \mathbf{b} = Q_{cs} \left( Q_{sw,t} \left(\mathbf{m}_{w,t} + \mathbf{e}_{w,t}^c - \mathbf{s}_{w,t} \right) - \mathbf{c}_s \right) \\
\partial_{\mathbf{e}^c_{w,t}} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= \left(\begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs}\right) \left( \mathbf{0} + \partial_{\mathbf{e}^c_{w,t}} Q_{sw,t} \mathbf{e}^c_{w,t} - \mathbf{0} - \mathbf{0} \right) \\
  &= \begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs} Q_{sw,t} I_3 \\
  &= \begin{bmatrix} I_2 & -(\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c) \end{bmatrix} Q_{cs} Q_{sw,t} \\
  &\phantom{=} \mbox{ (analogous to $\partial_\mathbf{x} h$)} \\

\partial_{\mathbf{m}_{n,t}} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= \begin{bmatrix} \partial_{\mathbf{m}_{n,t,1}} & \partial_{\mathbf{m}_{n,t,2}} \end{bmatrix} \\
  &= \begin{bmatrix} \partial_{\mathbf{e}^c_{n,t,1}} & \partial_{\mathbf{e}^c_{n,t,2}} \end{bmatrix} \\
\partial_{\mathbf{m}_{w,t}} h(\mathbf{x}, \mathbf{m}_{n,t}, \mathbf{m}_{w,t}, \mathbf{e}_{n,t}^c, \mathbf{e}_{w,t}^c)
  &= \begin{bmatrix} I_2 & -\mathbf{m}_{n,t} + \mathbf{e}_{n,t}^c \end{bmatrix} Q_{cs} Q_{sw,t} \\
  &\phantom{=} \mbox{ (analogous to $\partial_{\mathbf{e}^c_{w,t}}$)} \\
\end{align}
$$

## Bleser, Model 2 (gravity)

Given are state and process noise:

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
        0   & 0     & \partial_{\mathbf{q}_{sw}} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw} \right) & \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} & 0   & 0\\
        0   & 0     & 0 & I_3 & 0   & 0 \\
        0   & 0     & 0 & 0   & I_3 & 0 \\
        0   & 0     & 0 & 0   & 0   & I_3 \\
    \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        \frac{T^2}{2} I_3 & 0                                        & 0   & 0 \\
        T I_3             & 0                                        & 0   & 0 \\
        0                 & \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} & 0   & 0 \\
        0                 & I_3                                      & 0   & 0 \\
        0                 & 0                                        & I_3 & 0 \\
        0                 & 0                                        & 0   & I_3 \\
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } \mathbf{a} = \frac{T}{2}(\mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t})\\
  &\phantom{=\mbox{ with }} \mathbf{r} = \left( \partial_{\exp(\mathbf{a})} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \right) \left(-\frac{T}{2} \exp(\mathbf{a})\right)\\
  &\phantom{=\mbox{ with }} \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} = \begin{bmatrix} \mathbf{r}\mathbf{i} & \mathbf{r}\mathbf{j} & \mathbf{r}\mathbf{k} \end{bmatrix}\\
\end{align}
$$

### Measurement model

_Work in progress_


## Bleser Model 3 (acc)

Given are state and process noise:

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
        0   & 0     & I_3                 & \partial_{\mathbf{q}_{sw}} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw} \right) & \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} & 0   & 0\\
        0   & 0     & 0                   & 0 & I_3 & 0   & 0 \\
        0   & 0     & 0                   & 0 & 0   & I_3 & 0 \\
        0   & 0     & 0                   & 0 & 0   & 0   & I_3 \\
    \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        \frac{T^2}{2} I_3 & 0                                        & 0   & 0 \\
        T I_3             & 0                                        & 0   & 0 \\
        I_3               & 0                                        & 0   & 0 \\
        0                 & \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} & 0   & 0 \\
        0                 & I_3                                      & 0   & 0 \\
        0                 & 0                                        & I_3 & 0 \\
        0                 & 0                                        & 0   & I_3 \\
     \end{bmatrix} \\
  &\phantom{=}\mbox{ with } \mathbf{a} = \frac{T}{2}(\mathbf{\omega}_{s,t-T} + \mathbf{v}^\omega_{s,t})\\
  &\phantom{=\mbox{ with }} \mathbf{r} = \left( \partial_{\exp(\mathbf{a})} \left(\exp(\mathbf{a}) \odot \mathbf{q}_{sw,t-T}\right) \right) \left(-\frac{T}{2} \exp(\mathbf{a})\right)\\
  &\phantom{=\mbox{ with }} \mathbf{D}_{\omega_{s,t-T}}^{q_{sw,t-T}} = \begin{bmatrix} \mathbf{r}\mathbf{i} & \mathbf{r}\mathbf{j} & \mathbf{r}\mathbf{k} \end{bmatrix}\\
\end{align}
$$

### Measurement model

_Work in progress_


## Bleser Model 4 (acc input)

Given are control vector, state vector and process noise:

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
                \end{bmatrix}
\end{align}
$$

### State transition function

$$
\begin{align}
f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        \mathbf{s}_{w,t-T} + T \dot{\mathbf{s}}_{w,t-T} + \frac{T^2}{2} Q_{ws,t-T} \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right) + \frac{T^2}{2}\mathbf{g}_w \\
        \dot{\mathbf{s}}_{w,t-T} + T Q_{ws,t-T} \left(\mathbf{y}^a_s - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right) + T \mathbf{g}_w \\
        \exp\left( -\frac{T}{2} \left(\mathbf{y}^\omega_{s,t} - \mathbf{b}^\omega_{s,t} - \mathbf{v}^\omega_{s,t}\right) \right) \odot \mathbf{q}_{sw,t-T} \\
        \mathbf{b}^\omega_{s,t-T} + \mathbf{v}^{\mathbf{b}^\omega}_{s,t} \\
        \mathbf{b}^a_{s,t-T} + \mathbf{v}^{\mathbf{b}^a}_{s,t}
    \end{bmatrix} \\
\partial_\mathbf{x} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix}
        I_3 & T I_3 & \frac{T^2}{2} \dot{Q} \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right) & 0                   & -\frac{T^2}{2} Q_{ws,t-T} I_3 \\
        0   & I_3   & T \dot{Q} \left(\mathbf{y}^a_{s,t} - \mathbf{b}^a_{s,t-T} - \mathbf{v}^a_{s,t}\right)             & 0                   & -T Q_{ws,t-T}             I_3 \\
        0   & 0     & \partial_{q_{sw,t-T}} \left(\exp(\mathbf{a}') \odot \mathbf{q}_{sw,t-T}\right)                    & D^{q_{sw,t-T}}_{a'} & 0                             \\
        0   & 0     & 0                                                                                                 & I_3                 & 0                             \\
        0   & 0     & 0                                                                                                 & 0                   & I_3
    \end{bmatrix} \\
\partial_\mathbf{v} f(\mathbf{x}_{t-T}, \mathbf{u}_t, \mathbf{v}_t)
    &= \begin{bmatrix} 
        -\frac{T^2}{2} Q_{ws,t-T} I_3 & 0                   & 0   & 0   \\
        -T Q_{ws,t-T} I_3             & 0                   & 0   & 0   \\
        0                             & D^{q_{sw,t-T}}_{a'} & 0   & 0   \\
        0                             & 0                   & I_3 & 0   \\
        0                             & 0                   & 0   & I_3 \\
    \end{bmatrix} \\
    &\phantom{=}\mbox{ with } \mathbf{a}' = \frac{T}{2}(\mathbf{y}^\omega_{s,t} - \mathbf{b}^\omega_{s,t} - \mathbf{v}^\omega_{s,t})\\
    &\phantom{=\mbox{ with }} \mathbf{r} = \left( \partial_{\exp(\mathbf{a}')} \left(\exp(\mathbf{a}') \odot \mathbf{q}_{sw,t-T}\right) \right) \left(-\frac{T}{2} \exp(\mathbf{a}')\right)\\
    &\phantom{=\mbox{ with }} \mathbf{D}_{a'}^{q_{sw,t-T}} = \begin{bmatrix} \mathbf{r}\mathbf{i} & \mathbf{r}\mathbf{j} & \mathbf{r}\mathbf{k} \end{bmatrix}\\
    &\phantom{=\mbox{ with }} \dot{Q} = ?
\end{align}
$$
