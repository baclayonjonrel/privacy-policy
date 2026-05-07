import json

config_path = "es_ES-davefx-medium.onnx.json"

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

with open("tokens.txt", "w", encoding="utf-8") as f:
    for symbol, ids in config["phoneme_id_map"].items():
        f.write(f"{symbol} {ids[0]}\n")

print("tokens.txt created")