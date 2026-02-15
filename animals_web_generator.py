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

    if characteristics.get("diet"):
        output += f'<p><strong>Diet:</strong> {characteristics.get("diet")}</p>'

    if locations:
        output += f'<p><strong>Locations:</strong> {", ".join(locations)}</p>'

    if taxonomy.get("class"):
        output += f'<p><strong>Class:</strong> {taxonomy.get("class")}</p>'

    if taxonomy.get("order"):
        output += f'<p><strong>Order:</strong> {taxonomy.get("order")}</p>'

    if taxonomy.get("family"):
        output += f'<p><strong>Family:</strong> {taxonomy.get("family")}</p>'

    if characteristics.get("lifespan"):
        output += f'<p><strong>Lifespan:</strong> {characteristics.get("lifespan")}</p>'

    if characteristics.get("color"):
        output += f'<p><strong>Color:</strong> {characteristics.get("color")}</p>'

    if characteristics.get("temperament"):
        output += f'<p><strong>Temperament:</strong> {characteristics.get("temperament")}</p>'

    if characteristics.get("slogan"):
        output += f'<p><strong>Fact:</strong> {characteristics.get("slogan")}</p>'

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