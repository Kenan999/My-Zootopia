import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def main():
    animals_data = load_data('animals_data.json')

    animals_output = ""

    for animal in animals_data:
        name = animal.get("name")
        if name:
            animals_output += f"Name: {name}\n"

        diet = animal.get("characteristics", {}).get("diet")
        if diet:
            animals_output += f"Diet: {diet}\n"

        locations = animal.get("locations")
        if locations and len(locations) > 0:
            animals_output += f"Location: {locations[0]}\n"

        animal_type = animal.get("characteristics", {}).get("type")
        if animal_type:
            animals_output += f"Type: {animal_type}\n"

        animals_output += "\n"

    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    with open('animals.html', 'w') as output_file:
        output_file.write(new_html_content)


if __name__ == "__main__":
    main()