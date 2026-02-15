import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        name = animal.get("name")
        if name:
            print(f"Name: {name}")

        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            print(f"Diet: {diet}")

        locations = animal.get("locations")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")

        animal_type = animal.get("characteristics", {}).get("type")
        if animal_type:
            print(f"Type: {animal_type}")

        print()  


if __name__ == "__main__":
    main()