import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

# Load processed music notes
with open("processed_music_notes.json", "r") as file:
    music_data = json.load(file)

# Combine extracted notes
notes = []

for item in music_data:
    notes.extend(item["notes"])

if len(notes) < 20:
    raise ValueError("Not enough notes to train the model.")

# Prepare note sequences
sequence_length = 10
X = []
y = []

for i in range(len(notes) - sequence_length):
    X.append(notes[i:i + sequence_length])
    y.append(notes[i + sequence_length])

X = np.array(X)
y = np.array(y)

# Build the neural network
model = Sequential([
    Embedding(input_dim=128, output_dim=32),
    LSTM(64),
    Dense(128, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy"
)

# Train the model
model.fit(X, y, epochs=5, batch_size=32)

# Save the trained model
model.save("music_model.keras")

print("Music AI model trained and saved successfully!")