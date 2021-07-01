import matplotlib.pyplot as plt
import mpmath
import numpy as np
import scipy.special

import cplot

# gray to improve visibility on github's dark background
_gray = "#969696"
style = {
    "text.color": _gray,
    "axes.labelcolor": _gray,
    "axes.edgecolor": _gray,
    "xtick.color": _gray,
    "ytick.color": _gray,
}
plt.style.use(style)


def riemann_zeta(z):
    z = np.asarray(z)
    z_shape = z.shape
    vals = [mpmath.zeta(val) for val in z.flatten()]
    return np.array([float(val.real) + 1j * float(val.imag) for val in vals]).reshape(
        z_shape
    )


def riemann_xi(z):
    # https://en.wikipedia.org/wiki/Riemann_Xi_function
    return (
        0.5
        * z
        * (z - 1)
        * np.pi ** (-z / 2)
        * scipy.special.gamma(z / 2)
        * riemann_zeta(z)
    )


def riemann_siegel_z(z):
    z = np.asarray(z)
    z_shape = z.shape
    vals = [mpmath.siegelz(val) for val in z.flatten()]
    return np.array([float(val.real) + 1j * float(val.imag) for val in vals]).reshape(
        z_shape
    )


def riemann_siegel_theta(z):
    z = np.asarray(z)
    z_shape = z.shape
    vals = [mpmath.siegeltheta(val) for val in z.flatten()]
    return np.array([float(val.real) + 1j * float(val.imag) for val in vals]).reshape(
        z_shape
    )


# First function from the SIAM-100-digit challenge
# <https://en.wikipedia.org/wiki/Hundred-dollar,_Hundred-digit_Challenge_problems>
def siam(z):
    return np.cos(np.log(z) / z) / z


n = 400

cplot.savefig("z1.png", lambda z: z ** 1, (-2, +2), (-2, +2), n)
cplot.savefig("z2.png", lambda z: z ** 2, (-2, +2), (-2, +2), n)
cplot.savefig("z3.png", lambda z: z ** 3, (-2, +2), (-2, +2), n)

cplot.savefig("1z.png", lambda z: 1 / z, (-2, +2), (-2, +2), n)
cplot.savefig("z-absz.png", lambda z: z / abs(z), (-2, +2), (-2, +2), n)
cplot.savefig("z+1-z-1.png", lambda z: (z + 1) / (z - 1), (-5, +5), (-5, +5), n)

cplot.savefig("root2.png", np.sqrt, (-2, +2), (-2, +2), n)
cplot.savefig("root3.png", lambda x: x ** (1 / 3), (-2, +2), (-2, +2), n)
cplot.savefig("root4.png", lambda x: x ** 0.25, (-2, +2), (-2, +2), n)

cplot.savefig("log.png", np.log, (-2, +2), (-2, +2), n)
cplot.savefig("exp.png", np.exp, (-2, +2), (-2, +2), n)
cplot.savefig("exp1z.png", lambda z: np.exp(1 / z), (-1, +1), (-1, +1), n)

cplot.savefig("sin.png", np.sin, (-5, +5), (-5, +5), n)
cplot.savefig("cos.png", np.cos, (-5, +5), (-5, +5), n)
cplot.savefig("tan.png", np.tan, (-5, +5), (-5, +5), n)

cplot.savefig("sinh.png", np.sinh, (-5, +5), (-5, +5), n)
cplot.savefig("cosh.png", np.cosh, (-5, +5), (-5, +5), n)
cplot.savefig("tanh.png", np.tanh, (-5, +5), (-5, +5), n)

cplot.savefig("arcsin.png", np.arcsin, (-2, +2), (-2, +2), n)
cplot.savefig("arccos.png", np.arccos, (-2, +2), (-2, +2), n)
cplot.savefig("arctan.png", np.arctan, (-2, +2), (-2, +2), n)

cplot.savefig("sinz-z.png", lambda z: np.sin(z) / z, (-7, +7), (-7, +7), n)
cplot.savefig("cosz-z.png", lambda z: np.cos(z) / z, (-7, +7), (-7, +7), n)
cplot.savefig("tanz-z.png", lambda z: np.tan(z) / z, (-7, +7), (-7, +7), n)

cplot.savefig("gamma.png", scipy.special.gamma, (-5, +5), (-5, +5), n)
cplot.savefig("digamma.png", scipy.special.digamma, (-5, +5), (-5, +5), n)
cplot.savefig("zeta.png", riemann_zeta, (-30, +30), (-30, +30), n)

cplot.savefig("riemann-xi.png", riemann_xi, (-20, +20), (-20, +20), n)
cplot.savefig("riemann-siegel-z.png", riemann_siegel_z, (-20, +20), (-20, +20), n)
cplot.savefig(
    "riemann-siegel-theta.png", riemann_siegel_theta, (-20, +20), (-20, +20), n
)

cplot.savefig("siam.png", siam, (-1, 1), (-1, 1), n, abs_scaling="h-0.5")


def f(z):
    return (z ** 2 - 1) * (z - 2 - 1j) ** 2 / (z ** 2 + 2 + 2j)


n = 201
for name in ["cam16", "cielab", "oklab", "hsl"]:
    cplot.savefig(f"{name}-10.png", f, (-3, +3), (-3, +3), n, colorspace=name)
    cplot.savefig(
        f"{name}-05.png", f, (-3, +3), (-3, +3), n, abs_scaling="h-0.5", colorspace=name
    )
    cplot.savefig(
        f"{name}-00.png", f, (-3, +3), (-3, +3), n, abs_scaling="h-0", colorspace=name
    )