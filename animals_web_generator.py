"""animals_web_generator.py

Generates an HTML website for animals filtered by skin type.

This script fetches animal data from the API-Ninjas Animals API,
prompts the user to select a skin type, filters animals by the
selected type, and generates an HTML file using a template.
"""

import os
import json
import requests


API_URL = "https://api.api-ninjas.com/v1/animals?name=Fox"


def fetch_data_from_api():
    """Fetch animal data from the API using the API key from environment."""
    api_key = os.environ.get("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")

    response = requests.get(
        API_URL,
        headers={"X-Api-Key": api_key},
        timeout=10,
    )

    response.raise_for_status()
    return response.json()


def get_available_skin_types(animals):
    """Return a sorted list of unique skin types found in the dataset."""
    skin_types = set()
    for animal in animals:
        skin = animal.get("characteristics", {}).get("skin_type")
        if skin:
            skin_types.add(skin)
    return sorted(skin_types)


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
    """Generate the filtered animal website based on selected skin type."""
    animals_data = fetch_data_from_api()

    available_skin_types = get_available_skin_types(animals_data)

    print("Available skin types:")
    for skin in available_skin_types:
        print(f"- {skin}")

    selected_skin = input(
        "\nEnter a skin type from the list above: "
    ).strip()

    filtered_animals = [
        animal
        for animal in animals_data
        if animal.get("characteristics", {}).get("skin_type")
        == selected_skin
    ]

    if not filtered_animals:
        print("No animals found with that skin type.")
        return

    animals_output = ''
    for animal in filtered_animals:
        animals_output += serialize_animal(animal)

    with open('animals_template.html', 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace(
        '__REPLACE_ANIMALS_INFO__',
        animals_output,
    )

    with open('animals.html', 'w', encoding='utf-8') as output_file:
        output_file.write(new_html_content)

    print("\nWebsite generated successfully for selected skin type.")


if __name__ == '__main__':
    main()