class_labels = [
 "T-shirt/top",
 "Trouser",
 "Pullover",
 "Dress",
 "Coat",
 "Sandal",
 "Shirt",
 "Sneaker",
 "Bag",
 "Ankle boot"
]
# -----------------------------Import the necessary libraries------------------------------#
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# ---------------------------------Load the dataset-----------------------------------------#
(train_images, train_labels), (test_images, test_labels) =
tf.keras.datasets.fashion_mnist.load_data()
# -------------------------------Normalize the images--------------------------------------#
train_images = train_images / 255.0
test_images = test_images / 255.0
# ----------------Split the training data into training and validation sets--------------#
train_images, val_images, train_labels, val_labels = train_test_split(
 train_images, train_labels, test_size=0.2, random_state=42)
#--------------------------------- Build the model-----------------------------------------#
model = models.Sequential([
layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
layers.MaxPooling2D((2, 2)),
layers.Conv2D(64, (3, 3), activation='relu'),
layers.MaxPooling2D((2, 2)),
layers.Conv2D(64, (3, 3), activation='relu'),
layers.Flatten(),
layers.Dense(64, activation='relu'),
layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()
history = model.fit(train_images, train_labels, epochs=5)
#---------------------------------- Plot training & validation accuracy values-----------------------#
plt.figure(figsize=(12, 5))
# -----------------Accuracy-------------------#
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
#------------- Loss-------------------------#
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.show()
#--------------------------------Find and Display confusion matrix--------------------------#
from sklearn.metrics import confusion_matrix, precision_score, recall_score, 
ConfusionMatrixDisplay
predictions = model.predict(val_images)
predicted_labels = np.argmax(predictions, axis=1)
cm = confusion_matrix(val_labels, predicted_labels)
disp = ConfusionMatrixDisplay(cm, display_labels=class_labels)
disp.plot(cmap='Blues', values_format='d', ax=plt.gca()) # 'd' format to show integer values
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.yticks(fontsize=10)
plt.title('Confusion Matrix', fontsize=20)
plt.show()
# ----------------------Compute precision and recall--------------------------------#
precision = precision_score(val_labels, predicted_labels, average='weighted')
recall = recall_score(val_labels, predicted_labels, average='weighted')
print(f"# Precision: {precision:.2f}")
print(f"# Recall: {recall:.2f}")
#-------------------- function to test the model--------------------------------------#
def predict_image(index):
 image = val_images[index].reshape(1, 28, 28)
 predictions = model.predict(image)
 predicted_label = np.argmax(predictions)
 plt.imshow(val_images[index], cmap='gray')
 plt.title(f"True Label: {class_labels[val_labels[index]]} | Predicted: 
{class_labels[predicted_label]}")
 plt.axis('off')
 plt.show()
 print(f"Predicted probabilities: {predictions[0]}")
# Predict using the index 0 (you can change the index to any value from the val_images)
predict_image(100)
