import random
import json
import os

# AI Music Generation - Code Alpha Task 3

notes = ["C", "D", "E", "F", "G", "A", "B"]

# Create a simple music dataset
dataset = []

for i in range(100):
    sequence = [random.choice(notes) for _ in range(16)]
    dataset.append(sequence)

# Save the dataset
with open("music_dataset.json", "w") as file:
    json.dump(dataset, file, indent=2)

# Simple note sequence preprocessing
processed_data = []

for sequence in dataset:
    processed_data.append([note for note in sequence])

# Generate a new music sequence
generated_music = random.choice(processed_data)

print("Music Dataset Created Successfully!")
print("Generated Music:")
print(" - ".join(generated_music))

with open("generated_music.txt", "w") as file:
    file.write(" - ".join(generated_music))

print("Generated music saved successfully!")