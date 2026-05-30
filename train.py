import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt

np.random.seed(42)


train_data = pd.read_csv("train_processed.csv")
test_data = pd.read_csv("test_processed.csv")

X_train = train_data.drop(columns="DIABETE4")
y_train = train_data["DIABETE4"]
X_test = test_data.drop(columns="DIABETE4")
y_test = test_data["DIABETE4"]

performance_results = []

def save_performance_metrics(model_adi, y_true, y_pred, y_proba):
    """Hesaplanan tüm metrikleri listeye ve sözlüğe kaydeder."""
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, zero_division=0)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_proba)

    # Raporlama ekibi için tablo verisi
    performance_results.append({
        'Model': model_adi,
        'Accuracy': round(acc, 4),
        'Precision': round(prec, 4),
        'Recall (Duyarlılık)': round(rec, 4),
        'F1-Score': round(f1, 4),
        'AUC-ROC': round(auc, 4)
    })

# Lojistik Regresyon
print("--- Lojistik Regresyon Modeli Eğitiliyor ---")
reg = LogisticRegression(random_state=42,class_weight="balanced",penalty="l2",C=1.0)
reg.fit(X_train, y_train)

reg_preds = reg.predict(X_test)
reg_probs = reg.predict_proba(X_test)[:,1]

save_performance_metrics("Lojistik Regresyon",y_test,reg_preds,reg_probs)

# Karar Ağacı
print("\n--- Karar Ağacı Eğitiliyor ---")
tree_model = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42, class_weight="balanced")
tree_model.fit(X_train, y_train)

tree_preds = tree_model.predict(X_test)
tree_probs = tree_model.predict_proba(X_test)[:,1]

save_performance_metrics("Karar Ağacı",y_test,tree_preds,tree_probs)

# Random Forest
print("\n--- Random Forest Eğitiliyor ---")
rf_model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42, class_weight='balanced', n_jobs=-1)
rf_model.fit(X_train, y_train)

rf_preds = rf_model.predict(X_test)
rf_probs = rf_model.predict_proba(X_test)[:,1]

save_performance_metrics("Random Forest",y_test,rf_preds,rf_probs)

# MLP
print("\n--- Çok Katmanlı Algılayıcı (MLP) Eğitiliyor ---")
mlp = MLPClassifier(hidden_layer_sizes=(64,32),activation="relu",solver="adam",max_iter=300,early_stopping=True,random_state=42)
mlp.fit(X_train, y_train)

mlp_preds = mlp.predict(X_test)
mlp_probs = mlp.predict_proba(X_test)[:,1]

save_performance_metrics("Çok Katmanlı Algılayıcı",y_test,mlp_preds,mlp_probs)

print("\n✅ Tüm modeller başarıyla eğitildi!")


feature_importance = pd.DataFrame({
    'Değişken': X_train.columns,
    'Önem Derecesi (Entropy)': tree_model.feature_importances_
}).sort_values(by='Önem Derecesi (Entropy)', ascending=False)
print("\n--- Karar Ağacı Hiyerarşik Risk Analizi Çıktısı ---")
print(feature_importance)

df_performance = pd.DataFrame(performance_results)
print("--- AKADEMİK RAPOR İÇİN MODEL PERFORMANS KARŞILAŞTIRMA TABLOSU ---")
print(df_performance.to_string(index=False))