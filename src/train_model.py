"""Train Random Forest Model for Password Classification"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent))


def train_model(data_file, model_output, encoder_output):
    """Train Random Forest classifier on password data"""
    
    print("🚀 Starting model training...\n")
    
    # Load data
    print(f"Loading data from {data_file}...")
    df = pd.read_csv(data_file)
    print(f"Loaded {len(df)} samples")
    print(f"\nLabel distribution:")
    print(df['label'].value_counts())
    
    # Prepare features and labels
    feature_columns = [
        'length', 'entropy', 'has_uppercase', 'has_lowercase',
        'has_digit', 'has_special', 'uppercase_count', 'lowercase_count',
        'digit_count', 'special_count', 'char_diversity', 'has_leet_speak',
        'has_common_pattern', 'sequential_chars', 'repeated_chars',
        'keyboard_patterns'
    ]
    
    X = df[feature_columns]
    y = df['label']
    
    # Encode labels
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    
    print(f"\nFeatures shape: {X.shape}")
    print(f"Labels: {label_encoder.classes_}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
    )
    
    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")
    
    # Train Random Forest
    print("\n🌲 Training Random Forest Classifier...")
    rf_model = RandomForestClassifier(
        n_estimators=100,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1,
        verbose=1
    )
    
    rf_model.fit(X_train, y_train)
    
    # Evaluate model
    print("\n📊 Evaluating model...")
    y_pred = rf_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(
        y_test, y_pred,
        target_names=label_encoder.classes_
    ))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Feature importance
    print("\n📈 Feature Importance:")
    feature_importance = pd.DataFrame({
        'feature': feature_columns,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)
    print(feature_importance.head(10))
    
    # Save model and encoder
    print(f"\n💾 Saving model to {model_output}...")
    os.makedirs(os.path.dirname(model_output), exist_ok=True)
    joblib.dump(rf_model, model_output)
    
    print(f"💾 Saving label encoder to {encoder_output}...")
    joblib.dump(label_encoder, encoder_output)
    
    print("\n✅ Model training complete!")
    
    return rf_model, label_encoder


if __name__ == "__main__":
    data_file = "data/processed/cleaned_passwords.csv"
    model_output = "models/password_model.pkl"
    encoder_output = "models/label_encoder.pkl"
    
    # Check if data exists
    if not os.path.exists(data_file):
        print(f"❌ Data file {data_file} not found!")
        print("Please run clean_data.py first to process the dataset.")
        sys.exit(1)
    
    train_model(data_file, model_output, encoder_output)
