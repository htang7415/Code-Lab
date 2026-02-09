import torch


class Value:
    """A tiny scalar wrapper that delegates all gradient work to PyTorch autograd."""

    def __init__(self, data, _tensor=None):
        # leaf node: create fresh tensor with grad; internal node: reuse tensor
        if _tensor is None:
            self._t = torch.tensor(float(data), dtype=torch.float64, requires_grad=True)
        else:
            self._t = _tensor

        # retain grad for non-leaf tensors too (so .grad is available for debugging)
        # Only call if tensor participates in autograd.
        if self._t.requires_grad:
            try:
                self._t.retain_grad()
            except RuntimeError:
                # In rare cases PyTorch can complain; safe to ignore for this tiny wrapper.
                pass

    # ------- conveniences -------
    @property
    def data(self):
        return float(self._t.item())

    @property
    def grad(self):
        g = self._t.grad
        return 0.0 if g is None else float(g.item())

    def __repr__(self):
        def fmt(x):
            return int(x) if float(x).is_integer() else round(float(x), 4)

        return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

    # ensure rhs is Value
    def _wrap(self, other):
        return other if isinstance(other, Value) else Value(other)

    # ------- arithmetic ops -------
    def __add__(self, other):
        other = self._wrap(other)
        return Value(0.0, _tensor=self._t + other._t)

    __radd__ = __add__

    def __mul__(self, other):
        other = self._wrap(other)
        return Value(0.0, _tensor=self._t * other._t)

    __rmul__ = __mul__

    # ------- activation -------
    def relu(self):
        return Value(0.0, _tensor=torch.relu(self._t))

    # ------- grad utilities -------
    def zero_grad(self):
        """
        Clear gradients for *this* node only.
        (If you want to clear an entire graph, keep references to leaves and clear those.)
        """
        if self._t.grad is not None:
            self._t.grad.zero_()

    # ------- back-prop entry -------
    def backward(self, retain_graph: bool = False):
        """
        Run autograd backward from this scalar output.
        Note: gradients accumulate unless you call zero_grad() on relevant nodes.
        """
        self._t.backward(retain_graph=retain_graph)
