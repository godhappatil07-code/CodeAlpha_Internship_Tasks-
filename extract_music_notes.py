import os
import glob
import json

try:
    import mido
except ImportError:
    print("Please install mido first: python -m pip install mido")
    raise SystemExit

midi_folder = r"C:\Users\HP\Downloads\MAESTRO-V3.0.0-MIDI\MAESTRO-V3.0.0\2009"

midi_files = glob.glob(
    os.path.join(midi_folder, "**", "*.midi"),
    recursive=True
)

midi_files += glob.glob(
    os.path.join(midi_folder, "**", "*.mid"),
    recursive=True
)

processed_data = []

for file_path in midi_files[:100]:
    try:
        midi = mido.MidiFile(file_path)
        notes = []

        for track in midi.tracks:
            for message in track:
                if message.type == "note_on" and message.velocity > 0:
                    notes.append(message.note)

        if notes:
            processed_data.append({
                "file_name": os.path.basename(file_path),
                "notes": notes
            })

    except Exception as error:
        print("Could not process:", os.path.basename(file_path))

with open("processed_music_notes.json", "w") as file:
    json.dump(processed_data, file, indent=2)

print("MIDI files processed:", len(processed_data))
print("Music notes extracted successfully!")
print("Saved to processed_music_notes.json")