class CopyOp(Op):
    '''Copy a tensor'''

    def forward(self, x: AutogradTensor):
        self.x = x

        return AutogradTensor(x.child.copy(), requires_grad=x.requires_grad)

    def _backward(self, grad, backprop_id):

        if self.x.requires_grad:

            self.x.add_grad(AutogradTensor(grad.child.copy()))

            if self.x.grad_fn:
                self.x.backward(backprop_id=backprop_id) 