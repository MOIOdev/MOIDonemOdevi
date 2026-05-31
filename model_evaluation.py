import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, 
    recall_score, f1_score, roc_curve, roc_auc_score, mean_squared_error
)

def hesapla_ve_kaydet_performans_metrikleri(y_true, y_pred, y_prob, model_name):
    """
    Modellerin MSE, Accuracy, Precision, Recall, F1 ve AUC-ROC metriklerini hesaplar,
    Karmaşıklık Matrisini (Confusion Matrix) grafik olarak diske kaydeder.
    """
    # 1. Matematiksel Metriklerin Hesaplanması
    mse = mean_squared_error(y_true, y_pred)
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_prob)

    # 2. Bireysel Karmaşıklık Matrisi (Confusion Matrix) Çizimi
    plt.figure(figsize=(6, 5))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False,
                xticklabels=["Diyabet Yok (0)", "Diyabet Var (1)"],
                yticklabels=["Diyabet Yok (0)", "Diyabet Var (1)"])
    plt.title(f"{model_name} - Karmaşıklık Matrisi", fontsize=11, fontweight='bold')
    plt.xlabel("Tahmin Edilen Sınıf")
    plt.ylabel("Gerçek Sınıf")
    
    # TN, FP, FN, TP değerlerini grafik üzerine yazdırma
    tn, fp, fn, tp = cm.ravel()
    plt.text(0.5, 0.1, f"TN: {tn}", ha="center", va="center", color="black", fontsize=9, fontweight='bold')
    plt.text(1.5, 0.1, f"FP: {fp}", ha="center", va="center", color="red", fontsize=9, fontweight='bold')
    plt.text(0.5, 1.1, f"FN: {fn}", ha="center", va="center", color="red", fontsize=9, fontweight='bold')
    plt.text(1.5, 1.1, f"TP: {tp}", ha="center", va="center", color="black", fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    safe_name = model_name.lower().replace(' ', '_')
    plt.savefig(f"confusion_matrix_{safe_name}.png", dpi=300)
    plt.close()

    # Değerleri ana koda sözlük yapısında döndürme
    return {
        'Model': model_name,
        'MSE (Hata Payı)': round(mse, 4),
        'Accuracy': round(acc, 4),
        'Precision': round(prec, 4),
        'Recall (Duyarlılık)': round(rec, 4),
        'F1-Score': round(f1, 4),
        'AUC-ROC': round(auc, 4)
    }

def ciz_karsilastirmali_roc_egrisi(roc_curves_data):
    """Tüm modellerin AUC-ROC eğrilerini tek bir grafik düzleminde birleştirir."""
    plt.figure(figsize=(9, 7))
    for model_name, y_true, y_prob in roc_curves_data:
        fpr, tpr, _ = roc_curve(y_true, y_prob)
        auc_score = roc_auc_score(y_true, y_prob)
        plt.plot(fpr, tpr, lw=2, label=f'{model_name} (AUC = {auc_score:.4f})')

    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Rastgele Tahmin (0.5000)')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Yanlış Pozitif Oranı (FPR / 1 - Özgüllük)')
    plt.ylabel('Doğru Pozitif Oranı (TPR / Duyarlılık)')
    plt.title('Modeller Arası Karşılaştırmalı AUC-ROC Eğrisi', fontsize=12, fontweight='bold')
    plt.legend(loc="lower right")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig("tum_modeller_auc_roc_egrisi.png", dpi=300)
    plt.close()
