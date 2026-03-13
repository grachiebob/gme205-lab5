from spatial import Parcel, Building, Road
import json
import os

DATA_PATH = "data/spatial_features.json"
OUTPUT_DIR = "output"
RESULTS_PATH = os.path.join(OUTPUT_DIR, "lab5_results.json")

def load_features(filepath: str) -> list:
    with open("data/spatial_features.json") as f:
        data = json.load(f)

    features = []
    for item in data:
        f_type = item.get("type")

        if f_type == "Parcel":
            attri = item.get("attributes", {})
            f = Parcel(
                p_id=item.get("parcel_id"),
                zone=attri.get("zone", "Unknown"),
                is_active=item.get("is_active", False),
                geometry_data=item.get("geometry")
            )

        elif f_type == "Building":
            f = Building(
                geometry_data=item.get("geometry"),
                floors=item.get("floors")
            )

        elif f_type == "Road":
            f = Road (
                geometry_data=item.get("geometry"),
                width=item.get("width")
            )

        else:
            continue

        features.append(f)
    return features
        
def compute_total_area(features: list) -> float:
    return sum(f.effective_area() for f in features)

def compute_area_by_type(features: list) -> dict:
    area_type = {}
    for f in features:
        feature_name = type(f).__name__
        if feature_name not in area_type:
            area_type[feature_name] = 0.0
        area_type[feature_name] += f.effective_area()
    return area_type

def main():
    print("=== Laboratory Exercise 5 ===")

    features = load_features(DATA_PATH)

    if not features:
        print("Error: No spatial features found.")
        return
    else:
        print(f"Features loaded successfully: {len(features)} features.")

    total_area = compute_total_area(features)
    area_type = compute_area_by_type(features)

    print(f"Total Effective Area: {total_area:.2f} m²")
    print("Area by Feature Type:")
    for type_name, type_area in area_type.items():
        print(f" {type_name}: {type_area:.2f} m²")

    summary = {
        "total_effective_area": f"{total_area:.2f} m²",
        "area_type": {key: f"{value:.2f} m²" for key, value in area_type.items()}                      
    }

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\nSaved report to: {RESULTS_PATH}")


if __name__ == "__main__":
    main()