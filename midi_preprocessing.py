import os
import json
import glob

midi_folder = r"C:\Users\HP\Downloads\MAESTRO-V3.0.0-MIDI\MAESTRO-V3.0.0\2009"

midi_files = glob.glob(
    os.path.join(midi_folder, "**", "*.midi"),
    recursive=True
)

print("MIDI files found:", len(midi_files))

dataset = []

for file_path in midi_files[:100]:
    dataset.append({
        "file_name": os.path.basename(file_path),
        "file_path": file_path
    })

with open("midi_dataset.json", "w") as file:
    json.dump(dataset, file, indent=2)

print("MIDI file list saved successfully!")