"""animals_web_generator.py

Generates an HTML website for animals filtered by skin type.

This script fetches animal data from the API-Ninjas Animals API,
prompts the user to select a skin type, filters animals by the
selected type, and generates an HTML file using a template.
"""

import data_fetcher


def serialize_animal(animal):
    """Serialize a single animal dictionary into an HTML list item."""
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
        output += (
            f'<li class="card__list-item"><strong>Diet:</strong> '
            f'{characteristics.get("diet")}</li>'
        )

    if locations:
        output += (
            f'<li class="card__list-item"><strong>Locations:</strong> '
            f'{", ".join(locations)}</li>'
        )

    if taxonomy.get("class"):
        output += (
            f'<li class="card__list-item"><strong>Class:</strong> '
            f'{taxonomy.get("class")}</li>'
        )

    if taxonomy.get("order"):
        output += (
            f'<li class="card__list-item"><strong>Order:</strong> '
            f'{taxonomy.get("order")}</li>'
        )

    if taxonomy.get("family"):
        output += (
            f'<li class="card__list-item"><strong>Family:</strong> '
            f'{taxonomy.get("family")}</li>'
        )

    if characteristics.get("lifespan"):
        output += (
            f'<li class="card__list-item"><strong>Lifespan:</strong> '
            f'{characteristics.get("lifespan")}</li>'
        )

    if characteristics.get("color"):
        output += (
            f'<li class="card__list-item"><strong>Color:</strong> '
            f'{characteristics.get("color")}</li>'
        )

    if characteristics.get("temperament"):
        output += (
            f'<li class="card__list-item"><strong>Temperament:</strong> '
            f'{characteristics.get("temperament")}</li>'
        )

    output += '</ul>'
    output += '</div>'
    output += '</li>'

    return output


def main():
    """Generate the animal website based on user input."""
    animal_name = input("Enter a name of an animal: ").strip()

    if not animal_name:
        print("Animal name cannot be empty.")
        return

    animals_data = data_fetcher.fetch_data(animal_name)

    if not animals_data:
        error_html = (
            f'<div class="cards__item">'
            f'<div class="card__title">Animal Not Found</div>'
            f'<div class="card__text">'
            f'<ul class="card__list">'
            f'<li class="card__list-item">'
            f'The animal "{animal_name}" does not exist.'
            f'</li>'
            f'</ul>'
            f'</div>'
            f'</div>'
        )

        with open('animals_template.html', 'r', encoding='utf-8') as template_file:
            template_content = template_file.read()

        new_html_content = template_content.replace(
            '__REPLACE_ANIMALS_INFO__',
            error_html,
        )

        with open('animals.html', 'w', encoding='utf-8') as output_file:
            output_file.write(new_html_content)

        print("Website generated with error message in animals.html.")
        return

    animals_output = ''
    for animal in animals_data:
        animals_output += serialize_animal(animal)

    with open('animals_template.html', 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace(
        '__REPLACE_ANIMALS_INFO__',
        animals_output,
    )

    with open('animals.html', 'w', encoding='utf-8') as output_file:
        output_file.write(new_html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == '__main__':
    main()