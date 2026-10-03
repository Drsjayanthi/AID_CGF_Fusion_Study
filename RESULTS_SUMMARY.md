# Results summary — AID_CGF_01
Config fingerprint: `0339809eac` · seeds: [42, 123, 2026] · epochs ≤ 25 · device: cuda

## Main results (test set, mean ± SD over seeds)
| Model | Seeds | Accuracy (%) | Macro-F1 (%) | MCC | Kappa | AUC (%) | ECE (%) | NLL | Params (M) |
|---|---|---|---|---|---|---|---|---|---|
| EfficientNet-B0 | 3 | 96.10 ± 0.22 | 95.79 ± 0.26 | 0.9597 ± 0.0022 | 0.9596 ± 0.0023 | 99.82 ± 0.05 | 9.34 ± 0.40 | 0.236 ± 0.012 | 4.0 |
| ViT-B/16 | 3 | 96.55 ± 0.43 | 96.34 ± 0.44 | 0.9643 ± 0.0045 | 0.9643 ± 0.0045 | 99.66 ± 0.09 | 8.28 ± 0.40 | 0.237 ± 0.007 | 85.8 |
| Late fusion (avg) | 3 | 97.22 ± 0.16 | 97.02 ± 0.17 | 0.9712 ± 0.0016 | 0.9712 ± 0.0017 | 99.92 ± 0.01 | 10.13 ± 0.39 | 0.204 ± 0.005 | cnn+vit |
| Late fusion (val-tuned) | 3 | 97.08 ± 0.44 | 96.89 ± 0.47 | 0.9698 ± 0.0045 | 0.9698 ± 0.0045 | 99.91 ± 0.02 | 10.09 ± 0.27 | 0.205 ± 0.008 | cnn+vit |
| Concat fusion | 3 | 96.25 ± 0.52 | 96.04 ± 0.51 | 0.9612 ± 0.0054 | 0.9612 ± 0.0054 | 99.79 ± 0.09 | 7.54 ± 0.90 | 0.235 ± 0.017 | 90.5 |
| Scalar-gate fusion | 3 | 96.25 ± 0.48 | 96.02 ± 0.51 | 0.9612 ± 0.0049 | 0.9612 ± 0.0049 | 99.78 ± 0.08 | 5.25 ± 0.64 | 0.215 ± 0.019 | 90.5 |
| CGF-Net (proposed) | 3 | 96.62 ± 0.59 | 96.38 ± 0.61 | 0.9650 ± 0.0061 | 0.9650 ± 0.0061 | 99.86 ± 0.05 | 6.03 ± 0.83 | 0.206 ± 0.017 | 91.3 |

## Statistical comparison against CGF-Net
| Comparison | Δ accuracy (pp) | 95% bootstrap CI | Seeds with Holm-p<0.05 | median p (Holm) |
|---|---|---|---|---|
| CGF-Net (proposed) − EfficientNet-B0 | 0.52 | [-0.07, +1.08] | 1/3 | 0.711 |
| CGF-Net (proposed) − ViT-B/16 | 0.07 | [-0.40, +0.50] | 0/3 | 1.0 |
| CGF-Net (proposed) − Late fusion (avg) | -0.6 | [-1.00, -0.20] | 1/3 | 0.754 |
| CGF-Net (proposed) − Late fusion (val-tuned) | -0.47 | [-0.90, -0.02] | 0/3 | 0.544 |
| CGF-Net (proposed) − Concat fusion | 0.37 | [-0.07, +0.80] | 1/3 | 0.137 |
| CGF-Net (proposed) − Scalar-gate fusion | 0.37 | [-0.07, +0.78] | 0/3 | 0.754 |

## Ablation
| Model | Seeds | Cross-attn | Channel gate | Aux loss | Accuracy (%) | Macro-F1 (%) | ECE (%) | NLL | Params (M) | Δ Acc vs CGF (pp) |
|---|---|---|---|---|---|---|---|---|---|---|
| Scalar-gate fusion | 3 | – | scalar | – | 96.25 ± 0.48 | 96.02 ± 0.51 | 5.25 ± 0.64 | 0.215 ± 0.019 | 90.5 | -0.37 |
| Concat fusion | 3 | – | – | – | 96.25 ± 0.52 | 96.04 ± 0.51 | 7.54 ± 0.90 | 0.235 ± 0.017 | 90.5 | -0.37 |
| CGF w/o cross-attn | 3 | – | ✓ | ✓ | 95.97 ± 1.03 | 95.70 ± 1.05 | 5.51 ± 0.33 | 0.218 ± 0.017 | 90.7 | -0.65 |
| CGF w/o channel gate | 3 | ✓ | – | ✓ | 96.72 ± 0.71 | 96.48 ± 0.76 | 7.40 ± 0.38 | 0.222 ± 0.010 | 91.1 | +0.10 |
| CGF w/o aux loss | 3 | ✓ | ✓ | – | 96.53 ± 0.23 | 96.29 ± 0.22 | 6.10 ± 0.28 | 0.221 ± 0.017 | 91.3 | -0.08 |
| CGF-Net (proposed) | 3 | ✓ | ✓ | ✓ | 96.62 ± 0.59 | 96.38 ± 0.61 | 6.03 ± 0.83 | 0.206 ± 0.017 | 91.3 | — |

## Branch complementarity
| Subset | Share of test images (%) | CGF-Net accuracy on subset (%) |
|---|---|---|
| Both backbones correct | 94.55 | 99.21 |
| Only CNN correct | 1.55 | 62.77 |
| Only ViT correct | 2.0 | 74.84 |
| Both backbones wrong | 1.9 | 18.46 |

## Gate by subset
| Subset | Images | Mean CNN weight |
|---|---|---|
| Only CNN branch correct | 30 | 0.393 |
| Only ViT branch correct | 40 | 0.384 |
| Both branches correct | 1892 | 0.32 |
| Both branches wrong | 38 | 0.368 |

## Label efficiency
| model | fraction | n_train | pct_of_dataset | accuracy | macro_f1 | ece | n |
|---|---|---|---|---|---|---|---|
| cnn | 0.2 | 1411 | 14.0 | 93.1 | 92.746 | 8.716 | 1 |
| cnn | 0.5 | 3507 | 35.0 | 95.5 | 95.27 | 8.766 | 1 |
| cnn | 1.0 | 6999 | 70.0 | 95.95 | 95.552 | 9.788 | 1 |
| vit | 0.2 | 1411 | 14.0 | 94.15 | 93.714 | 9.308 | 1 |
| vit | 0.5 | 3507 | 35.0 | 95.55 | 95.216 | 8.421 | 1 |
| vit | 1.0 | 6999 | 70.0 | 97.05 | 96.854 | 7.819 | 1 |
| cgf | 0.2 | 1411 | 14.0 | 93.4 | 93.164 | 5.379 | 1 |
| cgf | 0.5 | 3507 | 35.0 | 95.55 | 95.327 | 6.108 | 1 |
| cgf | 1.0 | 6999 | 70.0 | 97.05 | 96.804 | 6.267 | 1 |

## Efficiency
| Unnamed: 0 | params_M | gflops | latency_ms_bs1 | throughput_img_s | accuracy_mean | accuracy_sd | train_min_per_run |
|---|---|---|---|---|---|---|---|
| cnn | 4.046 | 0.769 | 10.599 | 1869.656 | 96.1 | 0.218 | 15.406 |
| vit | 85.822 | 22.541 | 6.097 | 353.0 | 96.55 | 0.433 | 33.728 |
| concat | 90.538 | 23.42 | 16.972 | 303.333 | 96.25 | 0.522 | 41.465 |
| gate_scalar | 90.538 | 23.42 | 19.259 | 302.864 | 96.25 | 0.477 | 45.253 |
| cgf | 91.277 | 23.508 | 12.403 | 302.248 | 96.617 | 0.586 | 39.969 |
| cgf_noattn | 90.75 | 23.42 | 18.06 | 303.428 | 95.967 | 1.03 | 34.394 |
| cgf_nogate | 91.081 | 23.507 | 16.079 | 300.264 | 96.717 | 0.711 | 40.352 |
| cgf_noaux | 91.262 | 23.508 | 17.757 | 300.721 | 96.533 | 0.225 | 47.171 |
| late_avg | 89.868 | 23.31 | 16.696 | 296.937 | 97.217 | 0.161 | nan |
| late_val | 89.868 | 23.31 | 16.696 | 296.937 | 97.083 | 0.437 | nan |