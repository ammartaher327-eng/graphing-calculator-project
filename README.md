# Graphing Calculator Project

A Python graphing calculator that evolved from manual coefficient entry + NumPy polynomial evaluation (v1.x) to **symbolic expression parsing with SymPy → NumPy lambdify** (v2.0).

## Version History

### v1.x — Coefficient-Driven Polynomial/Trig/Exp Calculator
- **Approach**: Manual coefficient input → NumPy `polyval` / custom trig/exp functions
- **Workflow**: User enters coefficients one by one → hardcoded function blocks (`poly()`, `trig()`, `exp()`) → NumPy evaluation → Matplotlib plot
- **Limitations**: Only predefined function types; user must know polynomial degree upfront; no arbitrary expressions

### v2.0 — Symbolic Expression → NumPy Function (SymPy + Lambdify)
**Key architectural shift**: User enters **any mathematical expression as a string** → SymPy parses it symbolically → `sp.lambdify()` compiles it to a fast NumPy-callable function → Matplotlib plots it.

```python
# v2.0 core flow
x = sp.symbols('x')
f = sp.sympify(user_input, locals={"e": sp.E, "pi": sp.pi})  # symbolic parse
y = sp.lambdify(x, f, 'numpy')                                # symbolic → numpy callable
y_vals = y(x_vals)                                            # fast numpy evaluation
```

**What changed:**
| Aspect | v1.x | v2.0 |
|--------|------|------|
| Input | Coefficients (a, b, c...) one by one | Free-form expression string: `sin(x) + x**2`, `exp(-x)*cos(x)`, `log(x+1)` |
| Parsing | Manual per-function blocks | `sp.sympify()` — arbitrary expressions |
| Evaluation | NumPy `polyval` / custom loops | `sp.lambdify(..., 'numpy')` → vectorized NumPy ufunc |
| Extensibility | Add new `def` blocks | Any SymPy-parseable expression works automatically |
| Constants | Manual | `e`, `pi` auto-recognized via `locals` |

**Example v2.0 inputs that just work:**
```
sin(x) + x**2
exp(-x**2) * cos(3*x)
log(x + 1) / (x**2 + 1)
sqrt(x) * sin(1/x)
```

## Files
| File | Version | Description |
|------|---------|-------------|
| `v1.2.py` | v1.x | Polynomial / trig / exponential with manual coefficient entry |
| `grapher v1.2.py` | v1.x | Earlier graphing variant |
| `calc v2.0.py` | **v2.0** | **SymPy symbolic → NumPy lambdify calculator (current)** |
| `NANO.py` | — | Transformers pipeline (DistilGPT-2 on GPU) |
| `import torch.py` | — | PyTorch/CUDA test |

## Requirements
```bash
pip install sympy numpy matplotlib
# For NANO.py: pip install torch transformers
```

## Usage
```bash
python "calc v2.0.py"
# Enter any expression using x, e, pi, sin, cos, exp, log, sqrt, etc.
```

## Hardware
Tested on: AMD Ryzen 7 7445HS (8C/16T), 16GB DDR5, RTX 3050 Laptop 4GB VRAM, Windows 11