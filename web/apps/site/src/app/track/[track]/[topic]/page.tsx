import CodeBlock from "@/components/CodeBlock";
import MarkdownRenderer from "@/components/MarkdownRenderer";
import TableOfContents from "@/components/TableOfContents";
import type { TocHeading } from "@/components/TableOfContents";
import PrevNextNav from "@/components/PrevNextNav";
import GradientDescentViz from "@/components/GradientDescentViz";
import { buildNavItems, getAdjacentPages } from "@/lib/navigation";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { notFound } from "next/navigation";

type VizComponent = () => JSX.Element;

const VIZ_REGISTRY: Record<string, VizComponent> = {
  "ml/fundamentals/gradient-descent": GradientDescentViz,
};

/* ── Markdown cleaning helpers ─────────────────────────── */

function stripTopHeading(markdown: string) {
  const lines = markdown.split(/\r?\n/);
  if (lines.length === 0) return markdown;
  if (!lines[0].trim().startsWith("# ")) return markdown;
  let index = 1;
  while (index < lines.length && lines[index].trim() === "") index += 1;
  return lines.slice(index).join("\n");
}

/** Remove `> Track: ... | Topic: ...` blockquote lines. */
function stripTrackMeta(markdown: string): string {
  return markdown
    .split(/\r?\n/)
    .filter((line) => !/^>\s*Track:\s*`/i.test(line.trim()))
    .join("\n");
}

/** Remove the "## Run tests" section (and everything below it until the next ## heading or EOF). */
function stripRunTests(markdown: string): string {
  const lines = markdown.split(/\r?\n/);
  const result: string[] = [];
  let skipping = false;
  for (const line of lines) {
    if (/^##\s+Run\s+tests/i.test(line)) {
      skipping = true;
      continue;
    }
    if (skipping && /^##\s+/.test(line)) {
      skipping = false;
    }
    if (!skipping) result.push(line);
  }
  return result.join("\n");
}

/**
 * Parse README-style markdown into structured sections.
 * Recognized h2 sections: Concept, Purpose, Math, Key points.
 * Everything before the first h2 becomes "intro".
 */
interface ContentSection {
  id: string;
  label: string;
  icon: "concept" | "math" | "function" | "keypoints";
  content: string;
}

const SECTION_MAP: Record<string, { label: string; icon: ContentSection["icon"] }> = {
  concept: { label: "Concept", icon: "concept" },
  concepts: { label: "Concept", icon: "concept" },
  math: { label: "Math", icon: "math" },
  mathematics: { label: "Math", icon: "math" },
  function: { label: "Purpose", icon: "function" },
  functions: { label: "Purpose", icon: "function" },
  api: { label: "Purpose", icon: "function" },
  "key points": { label: "Key Points", icon: "keypoints" },
  "key-points": { label: "Key Points", icon: "keypoints" },
  keypoints: { label: "Key Points", icon: "keypoints" },
};

const SECTION_ORDER: Record<ContentSection["icon"], number> = {
  concept: 0,
  function: 1,
  math: 2,
  keypoints: 3,
};

function orderSections(sections: ContentSection[]) {
  return sections
    .map((section, index) => ({ section, index }))
    .sort((a, b) => {
      const orderA = SECTION_ORDER[a.section.icon] ?? 99;
      const orderB = SECTION_ORDER[b.section.icon] ?? 99;
      if (orderA !== orderB) return orderA - orderB;
      return a.index - b.index;
    })
    .map(({ section }) => section);
}

function stripCodeBlocks(markdown: string): string {
  const lines = markdown.split(/\r?\n/);
  const out: string[] = [];
  let inCode = false;
  for (const line of lines) {
    if (line.trim().startsWith("```")) {
      inCode = !inCode;
      continue;
    }
    if (!inCode) out.push(line);
  }
  return out.join("\n").trim();
}

function sanitizePurpose(text: string) {
  const withoutCode = stripCodeBlocks(text);
  if (!withoutCode) return undefined;
  const cleaned = withoutCode
    .replace(/^\s*>\s*/gm, "")
    .replace(/^\s*[-*+]\s+/gm, "")
    .replace(/^\s*\d+\.\s+/gm, "")
    .replace(/`([^`]*)`/g, "$1")
    .replace(/\[(.*?)\]\(.*?\)/g, "$1")
    .replace(/\s+/g, " ")
    .trim();
  if (!cleaned) return undefined;
  const match = cleaned.match(/(.+?[.!?])(\s|$)/);
  const sentence = match ? match[1].trim() : cleaned;
  return sentence.length > 220 ? `${sentence.slice(0, 217).trimEnd()}…` : sentence;
}

function toBaseVerb(verb: string) {
  const lower = verb.toLowerCase();
  if (["is", "are", "was", "were"].includes(lower)) return lower;
  if (lower.endsWith("ies")) return `${lower.slice(0, -3)}y`;
  if (lower.endsWith("es")) return lower.slice(0, -2);
  if (lower.endsWith("s")) return lower.slice(0, -1);
  return lower;
}

function ensurePeriod(text: string) {
  return /[.!?]$/.test(text) ? text : `${text}.`;
}

const PURPOSE_PATTERNS: Array<{ pattern: RegExp; purpose: string }> = [
  { pattern: /\bcosine similarity\b/i, purpose: "Use this to compare vector directions independent of magnitude." },
  { pattern: /\bvectors? and matrices?\b/i, purpose: "Use this to apply linear transforms to data." },
  { pattern: /\bjacobian\b/i, purpose: "Use this to capture local sensitivities of vector-valued functions." },
  { pattern: /\bhessian\b/i, purpose: "Use this to measure curvature with second derivatives." },
  { pattern: /\b(svd|singular value)\b/i, purpose: "Use this to decompose matrices and analyze structure." },
  { pattern: /\bpca\b/i, purpose: "Use this to reduce dimensionality while preserving variance." },
  { pattern: /\b(distribution|normalize probabilities)\b/i, purpose: "Use this to represent or normalize probability masses." },
  { pattern: /\bempirical pmf\b/i, purpose: "Use this to estimate probabilities from samples." },
  { pattern: /\bexpectation\b/i, purpose: "Use this to compute average outcomes under a distribution." },
  { pattern: /\bcovariance\b/i, purpose: "Use this to quantify how two variables move together." },
  { pattern: /\bmarkov\b/i, purpose: "Use this to model state transitions with conditional dependence." },
  { pattern: /\bkl divergence\b/i, purpose: "Use this to measure divergence between distributions for regularization or comparison." },
  { pattern: /\bjensen[-\s]?shannon\b/i, purpose: "Use this to compare distributions with a symmetric divergence." },
  { pattern: /\bmutual information\b/i, purpose: "Use this to quantify shared information between variables." },
  { pattern: /\b(two-sample t-test|t-stat)\b/i, purpose: "Use this to test whether two sample means differ." },
  { pattern: /\bbeta[-\s]?binomial\b/i, purpose: "Use this to update uncertainty about a Bernoulli rate." },
  { pattern: /\bgradient descent\b/i, purpose: "Use this to move parameters along the negative gradient." },
  { pattern: /\bnewton'?s method\b/i, purpose: "Use this to speed optimization using curvature." },
  { pattern: /\bconvex\b/i, purpose: "Use this to reason about optimization landscapes and guarantees." },
  { pattern: /\belbo\b/i, purpose: "Use this to optimize variational inference objectives." },
  { pattern: /\b(feedforward|mlp)\b/i, purpose: "Use this to model nonlinear mappings with stacked layers." },
  { pattern: /\b(neuron|weights|bias)\b/i, purpose: "Use this to compute affine transforms plus nonlinearity." },
  { pattern: /\bbackprop\b/i, purpose: "Use this to compute gradients efficiently through networks." },
  { pattern: /\bautomatic differentiation\b/i, purpose: "Use this to automate gradient computation." },
  { pattern: /\bvanishing|exploding\b/i, purpose: "Use this to diagnose unstable gradient magnitudes." },
  { pattern: /\bgradient checking\b/i, purpose: "Use this to validate analytic gradients with finite differences." },
  { pattern: /\bgradient flow\b/i, purpose: "Use this to assess how initialization affects gradients." },
  { pattern: /\bactivation failure\b/i, purpose: "Use this to diagnose dead or saturated activations." },
  { pattern: /\b(xavier|glorot)\b/i, purpose: "Use this to keep signal variance stable across layers." },
  { pattern: /\bhe initialization\b/i, purpose: "Use this to initialize ReLU networks with stable variance." },
  { pattern: /\b(l1|l2|weight decay|dropout|early stopping|regularization)\b/i, purpose: "Use this to reduce overfitting by constraining model capacity." },
  { pattern: /\b(sgd)\b/i, purpose: "Use this to update parameters with noisy gradients." },
  { pattern: /\b(momentum)\b/i, purpose: "Use this to smooth updates and accelerate in consistent directions." },
  { pattern: /\bnesterov\b/i, purpose: "Use this to anticipate gradients for faster convergence." },
  { pattern: /\badamw\b/i, purpose: "Use this to decouple weight decay from adaptive updates." },
  { pattern: /\badam\b/i, purpose: "Use this to combine momentum and adaptive step sizes." },
  { pattern: /\brmsprop\b/i, purpose: "Use this to adapt learning rates using recent gradient magnitudes." },
  { pattern: /\badagrad\b/i, purpose: "Use this to scale updates by accumulated gradients." },
  { pattern: /\bmuon\b/i, purpose: "Use this to stabilize matrix updates with orthogonalized momentum." },
  { pattern: /\b(learning rate|lr|warmup|cosine decay|step decay|exponential decay)\b/i, purpose: "Use this to control the learning rate over time for stable convergence." },
  { pattern: /\bgradient clipping\b/i, purpose: "Use this to prevent gradient explosions." },
  { pattern: /\bloss scaling\b/i, purpose: "Use this to avoid underflow in mixed-precision training." },
  { pattern: /\b(nan|divergence|detect)\b/i, purpose: "Use this to catch unstable training early." },
  { pattern: /\b(sigmoid|tanh|hardtanh|hard sigmoid)\b/i, purpose: "Use this to add bounded nonlinearities." },
  { pattern: /\b(relu|leaky relu|elu|prelu)\b/i, purpose: "Use this to preserve gradients in positive activations." },
  { pattern: /\b(gelu|swish|swiglu|mish)\b/i, purpose: "Use this to improve expressiveness and gradient flow." },
  { pattern: /\b(softmax|softplus|softsign)\b/i, purpose: "Use this to normalize logits or smooth activations." },
  { pattern: /\b(batchnorm transformers)\b/i, purpose: "Use this to understand why BatchNorm conflicts with sequence modeling." },
  { pattern: /\b(batchnorm|layernorm|rmsnorm|groupnorm|instancenorm)\b/i, purpose: "Use this to stabilize training by normalizing activations." },
  { pattern: /\bcross-entropy\b/i, purpose: "Use this to train classifiers with probabilistic targets." },
  { pattern: /\bhinge\b/i, purpose: "Use this to maximize margin in classifiers." },
  { pattern: /\bfocal\b/i, purpose: "Use this to focus learning on hard or rare examples." },
  { pattern: /\bmse\b/i, purpose: "Use this to penalize squared prediction errors." },
  { pattern: /\bmae\b/i, purpose: "Use this to penalize absolute prediction errors." },
  { pattern: /\brmse\b/i, purpose: "Use this to report error magnitude in original units." },
  { pattern: /\bhuber\b/i, purpose: "Use this to blend MAE and MSE robustness." },
  { pattern: /\bknowledge distillation\b/i, purpose: "Use this to transfer knowledge from a larger model." },
  { pattern: /\baccuracy\b/i, purpose: "Use this to measure overall classification correctness." },
  { pattern: /\bprecision\b/i, purpose: "Use this to measure correctness of positive predictions." },
  { pattern: /\brecall\b/i, purpose: "Use this to measure coverage of true positives." },
  { pattern: /\bf1\b/i, purpose: "Use this to balance precision and recall." },
  { pattern: /\broc[-\s]?auc\b/i, purpose: "Use this to evaluate ranking quality across thresholds." },
  { pattern: /\bconfusion matrix\b/i, purpose: "Use this to analyze error types." },
  { pattern: /\bmatthews\b/i, purpose: "Use this to evaluate binary classification with imbalance." },
  { pattern: /\bjaccard\b/i, purpose: "Use this to compare overlap between sets." },
  { pattern: /\bdice\b/i, purpose: "Use this to score overlap for segmentation tasks." },
  { pattern: /\bgini impurity\b/i, purpose: "Use this to measure split quality in trees." },
  { pattern: /\bsilhouette\b/i, purpose: "Use this to evaluate clustering cohesion and separation." },
  { pattern: /\bdavies[-\s]?bouldin\b/i, purpose: "Use this to evaluate clustering compactness." },
  { pattern: /\bcalinski[-\s]?harabasz\b/i, purpose: "Use this to evaluate clustering separation." },
  { pattern: /\br2\b/i, purpose: "Use this to quantify explained variance in regression." },
  { pattern: /\b(dataset|batch|epoch)\b/i, purpose: "Use this to understand training data flow." },
  { pattern: /\b(batch iterator)\b/i, purpose: "Use this to generate mini-batches for training." },
  { pattern: /\btrain.*validation.*test\b/i, purpose: "Use this to create unbiased evaluation splits." },
  { pattern: /\bstratified\b/i, purpose: "Use this to preserve class balance across splits." },
  { pattern: /\bleakage\b/i, purpose: "Use this to avoid invalid evaluation due to data contamination." },
  { pattern: /\bpolynomial features?\b/i, purpose: "Use this to add nonlinear feature interactions." },
  { pattern: /\bclass imbalance\b/i, purpose: "Use this to rebalance losses across classes." },
  { pattern: /\blinear regression\b/i, purpose: "Use this to model linear relationships in regression." },
  { pattern: /\blogistic regression\b/i, purpose: "Use this to model binary classification probabilities." },
  { pattern: /\bsoftmax regression\b/i, purpose: "Use this to model multi-class classification probabilities." },
  { pattern: /\belastic net\b/i, purpose: "Use this to combine L1 and L2 regularization." },
  { pattern: /\bdecision trees?\b/i, purpose: "Use this to model nonlinear splits with interpretable rules." },
  { pattern: /\brandom forest\b/i, purpose: "Use this to reduce variance with bagged trees." },
  { pattern: /\badaboost\b/i, purpose: "Use this to boost weak learners into a strong model." },
  { pattern: /\bknn\b/i, purpose: "Use this to classify or regress using nearest neighbors." },
  { pattern: /\bk-means\b/i, purpose: "Use this to cluster data around centroids." },
  { pattern: /\bdbscan\b/i, purpose: "Use this to find density-based clusters and outliers." },
  { pattern: /\bgaussian naive bayes\b/i, purpose: "Use this for probabilistic classification with Gaussian features." },
  { pattern: /\bbernoulli naive bayes\b/i, purpose: "Use this for binary or count-like features." },
  { pattern: /\bsvm\b/i, purpose: "Use this to find maximum-margin decision boundaries." },
  { pattern: /\bgaussian process\b/i, purpose: "Use this for nonparametric regression with uncertainty." },
  { pattern: /\bzeroing gradients\b/i, purpose: "Use this to clear gradients before backprop." },
  { pattern: /\bforward pass\b/i, purpose: "Use this to compute model outputs from inputs." },
  { pattern: /\bbackward pass\b/i, purpose: "Use this to compute gradients from a loss." },
  { pattern: /\boptimizer step\b/i, purpose: "Use this to apply gradients to parameters." },
  { pattern: /\bgradient accumulation\b/i, purpose: "Use this to simulate larger batch sizes." },
  { pattern: /\bmixed precision\b/i, purpose: "Use this to speed training while controlling numeric stability." },
  { pattern: /\bcheck gradients\b/i, purpose: "Use this to verify gradients are finite and non-zero." },
  { pattern: /\b(overfit|underfit)\b/i, purpose: "Use this to diagnose data-model fit issues." },
  { pattern: /\betl\b/i, purpose: "Use this to prepare and transform data for ML pipelines." },
  { pattern: /\boffline.*online inference\b/i, purpose: "Use this to choose deployment modes by latency needs." },
  { pattern: /\bbatch vs real-time\b/i, purpose: "Use this to select inference cadence by use case." },
  { pattern: /\bdata quality\b/i, purpose: "Use this to detect invalid or drifting inputs." },
  { pattern: /\bfeature drift\b/i, purpose: "Use this to detect distribution shifts in features." },
  { pattern: /\bprediction monitoring\b/i, purpose: "Use this to track output drift and performance." },
  { pattern: /\bcanary\b/i, purpose: "Use this to roll out models safely with small traffic." },
  { pattern: /\ba\/b testing\b/i, purpose: "Use this to compare model variants experimentally." },
  { pattern: /\bsla\b/i, purpose: "Use this to define latency and reliability targets." },
  { pattern: /\brequest batching\b/i, purpose: "Use this to improve throughput at inference time." },
  { pattern: /\btokenization|tokenizer\b/i, purpose: "Use this to turn text into model-friendly tokens." },
  { pattern: /\bembeddings?\b/i, purpose: "Use this to map discrete items into continuous vectors." },
  { pattern: /\bpositional encoding\b/i, purpose: "Use this to inject order information into sequences." },
  { pattern: /\bmasked attention\b/i, purpose: "Use this to enforce causal or selective context in attention." },
  { pattern: /\bself-attention\b/i, purpose: "Use this to let tokens attend to relevant context." },
  { pattern: /\bmulti-head attention\b/i, purpose: "Use this to learn diverse attention patterns in parallel." },
  { pattern: /\btransformer\b/i, purpose: "Use this to model long-range dependencies efficiently." },
  { pattern: /\bpretraining\b/i, purpose: "Use this to learn general representations from large corpora." },
  { pattern: /\bsupervised fine-tuning|sft\b/i, purpose: "Use this to adapt pretrained models to specific tasks." },
  { pattern: /\bpreference learning\b/i, purpose: "Use this to align outputs to human preferences." },
  { pattern: /\brlhf\b/i, purpose: "Use this to align models with reward feedback." },
  { pattern: /\bdpo\b/i, purpose: "Use this to optimize preferences without reward models." },
  { pattern: /\bppo\b/i, purpose: "Use this to update policies with stable clipped ratios." },
  { pattern: /\bkl regularization\b/i, purpose: "Use this to keep policies close to a reference distribution." },
  { pattern: /\bptx anchoring\b/i, purpose: "Use this to prevent alignment from drifting off pretraining." },
  { pattern: /\bqlora\b/i, purpose: "Use this to fine-tune large models with quantized weights." },
  { pattern: /\blora\b/i, purpose: "Use this to adapt large models with low-rank updates." },
  { pattern: /\binference head pruning\b/i, purpose: "Use this to reduce attention heads for efficiency." },
  { pattern: /\bsparse attention\b/i, purpose: "Use this to scale attention with fewer interactions." },
  { pattern: /\bmoe|mixture of experts\b/i, purpose: "Use this to scale capacity with routed experts." },
  { pattern: /\b(fp16|bf16|fp8)\b/i, purpose: "Use this to speed up training/inference with lower precision." },
  { pattern: /\b(int8|int4|quantization)\b/i, purpose: "Use this to reduce memory and accelerate inference." },
  { pattern: /\bmdp\b/i, purpose: "Use this to formalize states, actions, transitions, and rewards." },
  { pattern: /\b(return|discount)\b/i, purpose: "Use this to compute discounted reward sums." },
  { pattern: /\bexploration.*exploitation\b/i, purpose: "Use this to balance trying new actions vs exploiting known rewards." },
  { pattern: /\bbandits?\b/i, purpose: "Use this to learn action values from bandit feedback." },
  { pattern: /\bepsilon-greedy\b/i, purpose: "Use this to add simple exploration to greedy policies." },
  { pattern: /\bucb\b/i, purpose: "Use this to explore using uncertainty bonuses." },
  { pattern: /\bq-learning\b/i, purpose: "Use this to learn action values with temporal-difference updates." },
  { pattern: /\bsarsa\b/i, purpose: "Use this to learn on-policy action values." },
  { pattern: /\breinforce\b/i, purpose: "Use this to update policies with Monte Carlo returns." },
  { pattern: /\bdpo vs ppo\b/i, purpose: "Use this to compare preference and policy optimization tradeoffs." },
  { pattern: /\bgroup[-\s]?based optimization\b/i, purpose: "Use this to stabilize preference optimization with group-normalized rewards." },
  { pattern: /\bcnn\b/i, purpose: "Use this to extract spatial features from images." },
  { pattern: /\bconvolution layer\b/i, purpose: "Use this to apply learned filters over spatial inputs." },
  { pattern: /\bpooling\b/i, purpose: "Use this to downsample features for invariance." },
  { pattern: /\b2d vs 3d\b/i, purpose: "Use this to choose spatial vs spatiotemporal convolutions." },
  { pattern: /\bimage preprocessing\b/i, purpose: "Use this to normalize pixel ranges and stabilize training." },
  { pattern: /\brgb to grayscale\b/i, purpose: "Use this to convert images to luminance channels." },
  { pattern: /\bcontrast|brightness\b/i, purpose: "Use this to adjust image intensity distributions." },
  { pattern: /\bbilinear resizing\b/i, purpose: "Use this to resize images with smooth interpolation." },
  { pattern: /\bsobel\b/i, purpose: "Use this to compute image gradients for edges." },
  { pattern: /\boptical flow\b/i, purpose: "Use this to estimate motion between frames." },
  { pattern: /\bdata augmentation\b/i, purpose: "Use this to increase effective dataset diversity." },
  { pattern: /\bnon-maximum suppression\b/i, purpose: "Use this to remove overlapping detections." },
  { pattern: /\blenet|alexnet|vgg|resnet\b/i, purpose: "Use this to understand classic CNN design patterns." },
  { pattern: /\bgan\b/i, purpose: "Use this to generate data via adversarial training." },
  { pattern: /\bvae\b/i, purpose: "Use this to learn latent-variable generative models." },
  { pattern: /\bdiffusion\b/i, purpose: "Use this to generate data via denoising processes." },
  { pattern: /\bmodel selection\b/i, purpose: "Use this to choose a generative model family for a task." },
  { pattern: /\bmode collapse\b/i, purpose: "Use this to diagnose diversity failures in GANs." },
  { pattern: /\bposterior collapse\b/i, purpose: "Use this to detect latent variable underuse in VAEs." },
  { pattern: /\bguidance tradeoffs\b/i, purpose: "Use this to balance fidelity vs diversity in diffusion sampling." },
  { pattern: /\b(loss|objective)\b/i, purpose: "Use this to define the learning target for optimization." },
  { pattern: /\b(accuracy|precision|recall|f1|roc|auc|confusion|matthews|jaccard|dice|gini|silhouette|davies|calinski|r2)\b/i, purpose: "Use this to evaluate model performance for the task." },
];

function purposeFromKeywords(title: string, ...texts: Array<string | undefined>) {
  const haystack = [title, ...texts].filter(Boolean).join(" ").toLowerCase();
  for (const { pattern, purpose } of PURPOSE_PATTERNS) {
    if (pattern.test(haystack)) {
      return ensurePeriod(purpose);
    }
  }
  return undefined;
}

function makePurposeSentence(text: string) {
  const cleaned = sanitizePurpose(text);
  if (!cleaned) return undefined;
  const lowered = cleaned.toLowerCase();
  if (
    lowered.startsWith("use this") ||
    lowered.startsWith("helps ") ||
    lowered.startsWith("help ") ||
    lowered.startsWith("useful ") ||
    lowered.startsWith("useful for") ||
    lowered.startsWith("enables ") ||
    lowered.startsWith("allows ") ||
    lowered.startsWith("lets ") ||
    lowered.startsWith("improves ") ||
    lowered.startsWith("reduces ") ||
    lowered.startsWith("prevents ")
  ) {
    return ensurePeriod(cleaned);
  }

  const verbList = [
    "is",
    "are",
    "was",
    "were",
    "measures",
    "computes",
    "estimates",
    "normalizes",
    "stabilizes",
    "reduces",
    "adds",
    "applies",
    "maps",
    "converts",
    "splits",
    "updates",
    "compares",
    "detects",
    "balances",
    "samples",
    "clips",
    "approximates",
    "factorizes",
    "decomposes",
    "models",
    "encodes",
    "decodes",
    "optimizes",
    "regularizes",
    "encourages",
    "prevents",
    "controls",
    "limits",
    "aligns",
    "routes",
    "uses",
  ];

  for (const verb of verbList) {
    const regex = new RegExp(`\\b${verb}\\b`, "i");
    const match = cleaned.match(regex);
    if (match && match.index !== undefined) {
      const rest = cleaned.slice(match.index + match[0].length).trim();
      if (["is", "are", "was", "were"].includes(verb)) {
        if (!rest) break;
        return ensurePeriod(`Use this to understand ${rest}`);
      }
      const baseVerb = toBaseVerb(match[0]);
      if (!rest) break;
      return ensurePeriod(`Use this to ${baseVerb} ${rest}`);
    }
  }

  return ensurePeriod(`Use this to understand ${cleaned}`);
}

function normalizeSections(
  sections: ContentSection[],
  summary: string | undefined,
  title: string,
  intro: string
) {
  const normalized = sections.map((section) => {
    if (section.icon !== "function") return section;
    const functionContent = stripCodeBlocks(section.content);
    const purposeFromFunction = functionContent
      ? makePurposeSentence(functionContent)
      : undefined;
    return {
      ...section,
      content: purposeFromFunction ?? "",
    };
  });

  const conceptText = normalized.find((section) => section.icon === "concept")?.content;
  const keypointsText = normalized.find((section) => section.icon === "keypoints")?.content;

  let fallback = summary ? summary.trim() : undefined;
  if (fallback && title) {
    const lowerSummary = fallback.toLowerCase();
    const lowerTitle = title.toLowerCase();
    if (lowerSummary.startsWith(lowerTitle)) {
      fallback = fallback.slice(title.length).trim();
      fallback = fallback.replace(/^[\s:–-]+/, "");
      fallback = fallback.replace(/^(is|are|was|were)\s+/i, "");
    }
  }
  const keywordPurpose = purposeFromKeywords(title, fallback, conceptText, intro, keypointsText);
  fallback = fallback ? makePurposeSentence(fallback) : undefined;
  if (!fallback) {
    if (conceptText) fallback = makePurposeSentence(conceptText);
  }
  if (!fallback && intro) {
    fallback = makePurposeSentence(intro);
  }
  if (!fallback) {
    if (keypointsText) fallback = makePurposeSentence(keypointsText);
  }

  const functionIndex = normalized.findIndex((section) => section.icon === "function");
  const existingPurpose =
    functionIndex === -1 ? "" : normalized[functionIndex].content.trim();
  const finalPurpose = existingPurpose || keywordPurpose || fallback;

  if (functionIndex === -1) {
    if (!finalPurpose) return normalized;
    const insertAt = normalized.findIndex((section) => section.icon === "concept");
    const functionSection: ContentSection = {
      id: "function",
      label: "Purpose",
      icon: "function",
      content: finalPurpose,
    };
    if (insertAt === -1) {
      return [functionSection, ...normalized];
    }
    return [
      ...normalized.slice(0, insertAt + 1),
      functionSection,
      ...normalized.slice(insertAt + 1),
    ];
  }

  if (finalPurpose) {
    normalized[functionIndex] = {
      ...normalized[functionIndex],
      content: finalPurpose,
    };
  } else {
    return normalized.filter((_, idx) => idx !== functionIndex);
  }

  return normalized;
}

function parseSections(markdown: string): { intro: string; sections: ContentSection[] } {
  const lines = markdown.split(/\r?\n/);
  const sections: ContentSection[] = [];
  let intro = "";
  let currentKey: string | null = null;
  let currentLines: string[] = [];

  function flush() {
    if (currentKey !== null) {
      const mapping = SECTION_MAP[currentKey];
      if (mapping) {
        const id = currentKey.replace(/\s+/g, "-");
        sections.push({
          id,
          label: mapping.label,
          icon: mapping.icon,
          content: currentLines.join("\n").trim(),
        });
      } else {
        // Unknown section -- keep as a generic section
        sections.push({
          id: currentKey.replace(/\s+/g, "-"),
          label: currentKey.charAt(0).toUpperCase() + currentKey.slice(1),
          icon: "concept",
          content: currentLines.join("\n").trim(),
        });
      }
    }
    currentLines = [];
  }

  for (const line of lines) {
    const h2 = line.match(/^##\s+(.+)$/);
    if (h2) {
      if (currentKey === null) {
        intro = currentLines.join("\n").trim();
      } else {
        flush();
      }
      currentKey = h2[1].trim().toLowerCase();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }
  // Flush last section
  if (currentKey === null) {
    intro = currentLines.join("\n").trim();
  } else {
    flush();
  }

  return { intro, sections };
}

function cleanSummary(summary?: string) {
  if (!summary) return undefined;
  const trimmed = summary.trim();
  if (trimmed.toLowerCase().startsWith("> track")) return undefined;
  return trimmed;
}

function extractHeadings(markdown: string): TocHeading[] {
  const headings: TocHeading[] = [];
  const lines = markdown.split(/\r?\n/);
  for (const line of lines) {
    const match = line.match(/^(#{2,3})\s+(.+)$/);
    if (match) {
      const text = match[2].trim();
      // Skip "Run tests" headings
      if (/^Run\s+tests$/i.test(text)) continue;
      const level = match[1].length;
      const id = text
        .toLowerCase()
        .replace(/[^\w\s-]/g, "")
        .replace(/\s+/g, "-");
      headings.push({ id, text, level });
    }
  }
  return headings;
}

/* ── Section icon SVGs ────────────────────────────────── */

function SectionIcon({ icon }: { icon: ContentSection["icon"] }) {
  switch (icon) {
    case "concept":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <circle cx="8" cy="8" r="6" stroke="currentColor" strokeWidth="1.3" />
          <path d="M8 5v3.5M8 10.5v.5" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "math":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <path d="M3 8h10M8 3v10" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "function":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <path d="M5.5 4L2 8l3.5 4M10.5 4L14 8l-3.5 4" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "keypoints":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <path d="M4 4h8M4 8h6M4 12h8" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
  }
}

/* ── Page ─────────────────────────────────────────────── */

export function generateStaticParams() {
  const content = contentData as ContentIndex;
  return content.topics.map((topic) => ({
    track: topic.track,
    topic: topic.topic,
  }));
}

export default async function TopicPage({
  params,
}: {
  params: Promise<{ track: string; topic: string }>;
}) {
  const { track: trackId, topic: topicId } = await params;
  const content = contentData as ContentIndex;
  const track = content.tracks.find((item) => item.id === trackId);
  const topic = content.topics.find(
    (item) => item.track === trackId && item.topic === topicId
  );
  if (!track || !topic) return notFound();

  const navItems = buildNavItems(content);
  const { prev, next } = getAdjacentPages(navItems, trackId, topicId);

  const docs = content.docs
    .filter((item) => item.track === trackId && item.topic === topicId)
    .sort((a, b) => a.title.localeCompare(b.title));
  const modules = content.modules
    .filter((item) => item.track === trackId && item.topic === topicId)
    .sort((a, b) => a.title.localeCompare(b.title));

  const docBySlug = new Map(docs.map((doc) => [doc.slug, doc]));
  const moduleBySlug = new Map(modules.map((module) => [module.slug, module]));
  const entrySlugs = Array.from(
    new Set([
      ...docs.map((doc) => doc.slug),
      ...modules.map((module) => module.slug),
    ])
  );

  const entries = entrySlugs
    .map((slug) => {
      const doc = docBySlug.get(slug);
      const mod = moduleBySlug.get(slug);
      const title = doc?.title ?? mod?.title ?? slug;
      const summary = cleanSummary(doc?.summary) ?? cleanSummary(mod?.summary);

      // Clean the markdown: strip title, track meta, run tests
      let rawContent = doc ? doc.content : mod ? mod.readme : "";
      rawContent = stripTopHeading(rawContent);
      rawContent = stripTrackMeta(rawContent);
      rawContent = stripRunTests(rawContent);

      const parsed = parseSections(rawContent);
      const normalizedSections = normalizeSections(parsed.sections, summary, title, parsed.intro);
      const hasTheory = parsed.intro.length > 0 || parsed.sections.length > 0;
      const codeSources = mod?.sources ?? [];
      const hasCode = codeSources.length > 0;
      const vizKey = `${trackId}/${topicId}/${slug}`;
      const Viz = VIZ_REGISTRY[vizKey];

      return {
        slug,
        title,
        summary,
        rawContent,
        parsed: { ...parsed, sections: normalizedSections },
        hasTheory,
        codeSources,
        hasCode,
        Viz,
      };
    })
    .sort((a, b) => a.title.localeCompare(b.title));

  // Build TOC headings
  const allHeadings: TocHeading[] = [];
  for (const entry of entries) {
    allHeadings.push({ id: entry.slug, text: entry.title, level: 2 });
    for (const section of orderSections(entry.parsed.sections)) {
      if (section.icon === "concept" || section.icon === "math" || section.icon === "function") {
        continue;
      }
      allHeadings.push({ id: `${entry.slug}-${section.id}`, text: section.label, level: 3 });
    }
    // Hide "Demo Code" from the right-side TOC by request.
  }

  return (
    <div className="handbook-content-wrapper">
      <div>
        {/* Page header */}
        <div className="flex items-center gap-2 mb-1.5">
          <span
            className="h-2 w-2 rounded-full"
            style={{ background: `var(${track.accentVar})` }}
          />
          <span className="text-[0.7rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
            {track.name}
          </span>
        </div>
        <h1 className="text-[1.65rem] font-semibold tracking-tight leading-tight">
          {topic.name}
        </h1>

        {entries.length === 0 ? (
          <div className="empty-state mt-10">
            This topic is waiting on its first concept note or lab.
          </div>
        ) : (
          <div className="mt-8">
            {entries.map((entry, idx) => (
              <article
                key={entry.slug}
                id={entry.slug}
                className="concept-article"
              >
                {idx > 0 && <div className="concept-divider" />}

                <h2 className="concept-title">{entry.title}</h2>
                {entry.summary && (
                  <p className="mt-1 text-[0.85rem] text-[var(--text-secondary)]">
                    {entry.summary}
                  </p>
                )}

                {/* Intro text (before any ## heading) */}
                {entry.parsed.intro && (
                  <div className="mt-3">
                    <MarkdownRenderer content={entry.parsed.intro} />
                  </div>
                )}

                {/* Structured sections */}
                {orderSections(entry.parsed.sections).map((section) => (
                  <div
                    key={section.id}
                    id={`${entry.slug}-${section.id}`}
                    className="concept-section"
                  >
                    <div className={`section-header section-header-${section.icon}`}>
                      <SectionIcon icon={section.icon} />
                      <span>{section.label}</span>
                    </div>
                    <div className="section-body">
                      <MarkdownRenderer content={section.content} />
                    </div>
                  </div>
                ))}

                {entry.Viz && (
                  <div id={`${entry.slug}-viz`} className="concept-section">
                    <div className="section-header section-header-viz">
                      <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                        <path
                          d="M3 11l3-4 3 3 4-6"
                          stroke="currentColor"
                          strokeWidth="1.3"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                        />
                        <circle cx="3" cy="11" r="1.2" fill="currentColor" />
                        <circle cx="6" cy="7" r="1.2" fill="currentColor" />
                        <circle cx="9" cy="10" r="1.2" fill="currentColor" />
                        <circle cx="13" cy="4" r="1.2" fill="currentColor" />
                      </svg>
                      <span>Interactive</span>
                    </div>
                    <div className="section-body">
                      <entry.Viz />
                    </div>
                  </div>
                )}

                {/* Demo code */}
                {entry.hasCode && (
                  <div
                    id={`${entry.slug}-code`}
                    className="concept-section"
                  >
                    <div className="section-header section-header-code">
                      <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                        <path d="M5.5 4L2 8l3.5 4M10.5 4L14 8l-3.5 4" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round"/>
                      </svg>
                      <span>Demo Code</span>
                    </div>
                    <div className="section-body">
                      <div className="grid gap-3">
                        {entry.codeSources.map((source) => (
                          <CodeBlock
                            key={source.path}
                            filename={source.path}
                            language={source.language}
                            code={source.content}
                          />
                        ))}
                      </div>
                    </div>
                  </div>
                )}

                {!entry.hasTheory && !entry.hasCode && (
                  <p className="mt-3 text-[0.85rem] text-[var(--text-muted)]">
                    Content coming soon.
                  </p>
                )}
              </article>
            ))}
          </div>
        )}

        <PrevNextNav prev={prev} next={next} />
      </div>

      <TableOfContents headings={allHeadings} />
    </div>
  );
}
