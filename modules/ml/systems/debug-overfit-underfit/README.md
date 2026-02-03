# Debug Overfitting vs Underfitting

> Track: `ml` | Topic: `systems`

## Concept

Debugging overfitting and underfitting is the process of comparing training loss against validation loss to diagnose whether a model has the right capacity for the task. Overfitting means the model memorizes training data but fails to generalize, visible as low training loss paired with high validation loss. Underfitting means the model lacks the capacity or has not trained long enough, visible as both losses remaining high.

These failure modes connect directly to the bias-variance tradeoff. An underfit model has high bias -- it cannot capture the true underlying pattern. An overfit model has high variance -- it is too sensitive to noise in the training set. A practical debugging workflow starts by overfitting a single small batch to verify the model and optimizer are wired correctly, then scales up to the full dataset while monitoring the gap between training and validation loss.

## Math

The expected test error decomposes into bias, variance, and irreducible noise:

$$\mathbb{E}[L_{\text{test}}] = \mathrm{Bias}^2 + \mathrm{Variance} + \sigma^2_{\text{noise}}$$

Diagnostic rules based on observed losses:

$$L_{\text{train}} \ll L_{\text{val}} \implies \text{overfitting (high variance)}$$

$$L_{\text{train}} \approx L_{\text{val}} \gg L^{*} \implies \text{underfitting (high bias)}$$

- $L_{\text{train}}$ -- average loss on the training set
- $L_{\text{val}}$ -- average loss on the validation set
- $L^{*}$ -- irreducible (Bayes-optimal) error
- $\sigma^2_{\text{noise}}$ -- variance of the irreducible noise

- $\mathbb{E}$ -- expectation
- $\sigma$ -- standard deviation
- $L$ -- loss value

## Key Points

- Always overfit a single small batch first to confirm the model can memorize -- if it cannot, there is a bug before you even consider generalization.
- Overfitting remedies include regularization (dropout, weight decay, data augmentation) and reducing model size.
- Underfitting remedies include increasing model capacity, training longer, or reducing regularization strength.
- The gap between training and validation loss is more informative than either value alone.
- Early stopping monitors validation loss and halts training when it begins to rise, providing a simple defense against overfitting.

## Function

```python
def diagnose(train_loss: float, val_loss: float) -> str:
```

- `train_loss` -- average loss computed on the training set
- `val_loss` -- average loss computed on the validation set

## Run tests

```bash
pytest modules/ml/systems/debug-overfit-underfit/python -q
```
