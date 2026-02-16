

# My-Zootopia 🦊

My-Zootopia is a Python-based web generator that fetches animal data from the API-Ninjas Animals API and dynamically generates a styled HTML website.

The user enters the name of an animal, and the program fetches real-time data from the API and generates a modern HTML page displaying the results.

---

## Features

- Fetches live animal data from an external API
- Secure API key handling using `.env`
- Modular architecture (Data Fetcher + Website Generator)
- Error handling for non-existent animals
- Clean project structure following PEP 8 guidelines

---

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/My-Zootopia.git
cd My-Zootopia
```

2. Create a virtual environment (recommended):

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:

```
API_KEY=your_api_key_here
```

---

## Usage

Run the program:

```
python animals_web_generator.py
```

Enter the name of an animal when prompted:

```
Enter a name of an animal: Fox
```

The website will be generated in:

```
animals.html
```

Open it in your browser to view the result.

---

## Project Architecture

- `data_fetcher.py` → Handles API communication  
- `animals_web_generator.py` → Handles HTML generation  
- `.env` → Stores environment variables securely  
- `requirements.txt` → Lists project dependencies  

---

## License

This project is for educational purposes.