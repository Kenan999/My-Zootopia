import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">'

    name = animal.get("name")
    if name:
        output += f'<div class="card__title">{name}</div>'

    output += '<p class="card__text">'

    diet = animal.get("characteristics", {}).get("diet")
    if diet:
        output += f'<strong>Diet:</strong> {diet}<br/>'

    locations = animal.get("locations")
    if locations and len(locations) > 0:
        output += f'<strong>Location:</strong> {locations[0]}<br/>'

    animal_type = animal.get("characteristics", {}).get("type")
    if animal_type:
        output += f'<strong>Type:</strong> {animal_type}<br/>'

    output += '</p>'
    output += '</li>'

    return output


def main():
    animals_data = load_data('animals_data.json')

    animals_output = ''
    for animal in animals_data:
        animals_output += serialize_animal(animal)

    with open('animals_template.html', 'r') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace(
        '__REPLACE_ANIMALS_INFO__',
        animals_output
    )

    with open('animals.html', 'w') as output_file:
        output_file.write(new_html_content)


if __name__ == '__main__':
    main()