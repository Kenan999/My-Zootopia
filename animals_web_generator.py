import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">'

    name = animal.get("name", "Unknown")
    output += f'<div class="card__title">{name}</div>'

    characteristics = animal.get("characteristics", {})
    taxonomy = animal.get("taxonomy", {})
    locations = animal.get("locations", [])

    output += '<div class="card__text">'
    output += '<ul class="card__list">'

    if characteristics.get("diet"):
        output += f'<li class="card__list-item"><strong>Diet:</strong> {characteristics.get("diet")}</li>'

    if locations:
        output += f'<li class="card__list-item"><strong>Locations:</strong> {", ".join(locations)}</li>'

    if taxonomy.get("class"):
        output += f'<li class="card__list-item"><strong>Class:</strong> {taxonomy.get("class")}</li>'

    if taxonomy.get("order"):
        output += f'<li class="card__list-item"><strong>Order:</strong> {taxonomy.get("order")}</li>'

    if taxonomy.get("family"):
        output += f'<li class="card__list-item"><strong>Family:</strong> {taxonomy.get("family")}</li>'

    if characteristics.get("lifespan"):
        output += f'<li class="card__list-item"><strong>Lifespan:</strong> {characteristics.get("lifespan")}</li>'

    if characteristics.get("color"):
        output += f'<li class="card__list-item"><strong>Color:</strong> {characteristics.get("color")}</li>'

    if characteristics.get("temperament"):
        output += f'<li class="card__list-item"><strong>Temperament:</strong> {characteristics.get("temperament")}</li>'

    if characteristics.get("slogan"):
        output += f'<li class="card__list-item"><strong>Fact:</strong> {characteristics.get("slogan")}</li>'

    output += '</ul>'
    output += '</div>'
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