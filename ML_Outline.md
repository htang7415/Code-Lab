## 1. Foundations of Deep Learning ⭐⭐⭐

### Neural Networks & Backprop

- Feedforward neural networks - **done**
- Neuron, weights, bias, activation - **done**
- Backpropagation (chain rule, local gradients) -
- Automatic differentiation (forward vs backward mode)
- Vanishing & exploding gradients
- Gradient checking (finite differences)

### Activation Functions

- Sigmoid, Tanh (limitations), Hard Sigmoid, Dynamic Tanh, Hardtanh - **done**
- ReLU family: ReLU, Leaky ReLU, ELU, PReLU **- done**
- Modern: GeLU, Swish, SwiGLU, Mish **- done**
- Softmax, Softplus, Softsign **- done**
- Failure modes (dead ReLU, saturation) **- done**

---

## 2. Optimization & Training Dynamics ⭐⭐⭐

### Optimizers

- SGD
- SGD with Momentum
- Nesterov Accelerated Gradient
- Adam
- AdamW (why decoupled weight decay matters)
- RMSProp
- Adagrad
- ⭐ Muon (high-level intuition)

### Learning Rate Strategies

- Constant LR
- Step decay
- Exponential decay
- Warmup
- Cosine decay

### Training Stability

- Gradient clipping (global norm)
- Loss scaling (mixed precision)
- Detecting NaNs / divergence

---

## 3. Initialization & Regularization ⭐⭐⭐

### Initialization

- Xavier / Glorot: symmetric activations - **done**
- He initialization: Relu- **done**
- Effect on gradient flow

### Regularization

- L1 (Lasso)
- L2 (Ridge)
- Weight decay
- Dropout
- Early stopping
- LoRA (conceptual regularization effect)

---

## 4. Data & Splitting ⭐⭐⭐

- Dataset vs batch vs epoch
- Batch iterator
- Train / validation / test split
- Stratified split
- Data leakage (common failure modes)
- Polynomial feature expansion
- Handling class imbalance

---

## 5. Loss Functions ⭐⭐⭐

### Classification

- Cross-entropy
- Hinge loss
- Focal loss (imbalanced data)

### Regression

- MSE
- MAE
- RMSE
- Huber loss

### Special

- Knowledge distillation loss
- KL divergence

---

## 6. Normalization ⭐⭐⭐

- BatchNorm (train vs eval behavior)
- LayerNorm
- RMSNorm
- GroupNorm
- InstanceNorm
- Why BatchNorm is bad for Transformers

---

## 7. Models & Classical ML ⭐⭐

- Linear regression
- Logistic regression
- Softmax regression
- Elastic Net
- Decision Trees
- Random Forest (bagging)
- AdaBoost
- KNN
- K-Means
- DBSCAN
- PCA
- Gaussian Naive Bayes
- Bernoulli Naive Bayes
- SVM (Pegasos)
- Gaussian Process Regression (GPR)

---

## 8. Metrics & Evaluation ⭐⭐⭐

### Classification

- Accuracy (when it fails)
- Precision / Recall
- F1
- ROC-AUC
- Confusion matrix
- Matthews correlation coefficient
- Jaccard index
- Dice score
- Gini impurity

### Clustering

- Silhouette score
- Davies–Bouldin index
- Calinski–Harabasz index

### Regression

- MAE vs MSE
- RMSE
- R² (pitfalls)

---

## 9. Training Loop Mechanics ⭐⭐⭐ (Very Important)

- Zeroing gradients
- Forward pass
- Backward pass
- Optimizer step
- Gradient accumulation
- Mixed precision training
- Check gradients are flowing
- Debug overfitting vs underfitting

---

## 10. MLOps & Production ML ⭐⭐

- ETL pipeline
- Offline vs online inference
- Batch vs real-time inference
- Data quality checks
- Feature drift detection (PSI)
- Prediction distribution monitoring
- Canary deployment
- A/B testing
- SLA metrics
- Request batching

---

## 11. NLP & LLMs ⭐⭐⭐

### Core Concepts

- Tokenization
- Embeddings
- Positional encoding
- Transformer
- Self-attention
- Multi-head attention
- Masked attention

### Training Stages

- Pretraining (next-token prediction / PTX loss)
- Supervised fine-tuning (SFT)
- Alignment / preference learning

### Alignment & Optimization

- RLHF
- DPO
- KL regularization
- PTX anchoring

### Efficiency & Systems ⭐⭐

- LoRA / QLoRA
- Inference head pruning
- Sparse attention
- MoE (Top-K routing, Noisy gating)
- FP16 / BF16 / FP8
- INT8 / INT4

---

## 12. Reinforcement Learning ⭐⭐

### Core Ideas

- MDPs
- Reward, return, discount factor
- Exploration vs exploitation

### Algorithms

- Bandits
- ε-greedy
- UCB
- REINFORCE
- PPO (why clipping helps)
- Q-Learning
- SARSA

### LLM-related RL ⭐⭐

- DPO vs PPO
- Group-based optimization (GSPO / GRPO)

---

## 13. Computer Vision ⭐⭐

### CNN Fundamentals

- CNNs
- Convolution layers
- Pooling (max, average)
- 2D vs 3D CNN
- Image preprocessing
- RGB → grayscale
- Contrast & brightness
- Bilinear resizing
- Sobel edge detection
- Optical flow (EPE)
- Data augmentation
- Non-maximum suppression

### Classic Architectures (Know the key idea + what changed) ⭐⭐

- LeNet-5
- AlexNet
- VGGNet
- ResNet

---

## 14. Generative Models ⭐⭐

### Core Families

- GAN (generator vs discriminator, mode collapse)
- VAE (ELBO, reconstruction + KL)
- Diffusion models (forward noise / reverse denoise, training objective)

### Interview-Level Skills

- Choose GAN vs VAE vs Diffusion for a task (trade-offs)
- Common failure modes and debugging:
    - GAN instability, mode collapse
    - VAE blurry samples, posterior collapse
    - Diffusion slow sampling, guidance trade-offs

---

## 15. Math for ML ⭐⭐⭐

### Linear Algebra

- Vectors, matrices
- Jacobian
- Hessian
- SVD
- Cosine similarity

### Probability & Statistics

- Distributions
- Empirical PMF
- Expectation
- Covariance
- Markov chains
- KL divergence
- Jensen–Shannon divergence
- Mutual information
- Two-sample t-test
- Bayesian inference (Beta-Binomial)

### Optimization

- Gradient descent
- Newton’s method
- Convex vs non-convex intuition
- ELBO (variational inference)