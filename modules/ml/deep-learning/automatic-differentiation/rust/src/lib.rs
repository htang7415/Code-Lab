use std::cell::RefCell;
use std::collections::HashSet;
use std::rc::Rc;

#[derive(Clone)]
enum Op {
    Leaf,
    Add,
    Mul,
    Relu,
}

#[derive(Clone)]
pub struct Value {
    node: Rc<RefCell<Node>>,
}

#[derive(Clone)]
struct Node {
    data: f64,
    grad: f64,
    op: Op,
    left: Option<Value>,
    right: Option<Value>,
}

impl Value {
    pub fn new(data: f64) -> Self {
        Self {
            node: Rc::new(RefCell::new(Node {
                data,
                grad: 0.0,
                op: Op::Leaf,
                left: None,
                right: None,
            })),
        }
    }

    fn from_unary(data: f64, op: Op, left: Value) -> Self {
        Self {
            node: Rc::new(RefCell::new(Node {
                data,
                grad: 0.0,
                op,
                left: Some(left),
                right: None,
            })),
        }
    }

    fn from_binary(data: f64, op: Op, left: Value, right: Value) -> Self {
        Self {
            node: Rc::new(RefCell::new(Node {
                data,
                grad: 0.0,
                op,
                left: Some(left),
                right: Some(right),
            })),
        }
    }

    pub fn data(&self) -> f64 {
        self.node.borrow().data
    }

    pub fn grad(&self) -> f64 {
        self.node.borrow().grad
    }

    pub fn add(&self, other: &Value) -> Value {
        Value::from_binary(self.data() + other.data(), Op::Add, self.clone(), other.clone())
    }

    pub fn mul(&self, other: &Value) -> Value {
        Value::from_binary(self.data() * other.data(), Op::Mul, self.clone(), other.clone())
    }

    pub fn relu(&self) -> Value {
        Value::from_unary(self.data().max(0.0), Op::Relu, self.clone())
    }

    pub fn zero_grad(&self) {
        self.node.borrow_mut().grad = 0.0;
    }

    pub fn backward(&self) {
        let mut topo = Vec::new();
        let mut visited = HashSet::new();
        build_topo(self, &mut visited, &mut topo);

        // Match autograd's "accumulate gradients" behavior at the output seed.
        self.node.borrow_mut().grad += 1.0;

        for v in topo.into_iter().rev() {
            let (op, grad, left, right) = {
                let n = v.node.borrow();
                (n.op.clone(), n.grad, n.left.clone(), n.right.clone())
            };

            match op {
                Op::Leaf => {}
                Op::Add => {
                    if let Some(l) = left {
                        l.node.borrow_mut().grad += grad;
                    }
                    if let Some(r) = right {
                        r.node.borrow_mut().grad += grad;
                    }
                }
                Op::Mul => {
                    if let (Some(l), Some(r)) = (left, right) {
                        let l_data = l.data();
                        let r_data = r.data();
                        l.node.borrow_mut().grad += r_data * grad;
                        r.node.borrow_mut().grad += l_data * grad;
                    }
                }
                Op::Relu => {
                    if let Some(l) = left {
                        let local = if l.data() > 0.0 { 1.0 } else { 0.0 };
                        l.node.borrow_mut().grad += local * grad;
                    }
                }
            }
        }
    }
}

fn build_topo(v: &Value, visited: &mut HashSet<usize>, topo: &mut Vec<Value>) {
    let id = Rc::as_ptr(&v.node) as usize;
    if visited.insert(id) {
        let (left, right) = {
            let n = v.node.borrow();
            (n.left.clone(), n.right.clone())
        };
        if let Some(l) = left {
            build_topo(&l, visited, topo);
        }
        if let Some(r) = right {
            build_topo(&r, visited, topo);
        }
        topo.push(v.clone());
    }
}
