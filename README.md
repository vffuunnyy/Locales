# PyLocales

Locales - module for multilingual projects

## Getting Started

### Prerequisites

Locales uses only standard library **json**. You need to write the translations in *json format*

```json
{
  "languages": {
      "ru": "Русский", "eng": "English", "sp": "Español"
  },

  "messages": {
      "welcome": {
          "ru": "Добро пожаловать!",
          "eng": "Welcome!"
      },
      "goodbye": {
          "ru": "Пока",
          "eng": "Goodbye",
          "sp": "Adiós"
      }
  }
}
```
Keys `languages` and `messages` required.

To generate the same file use:
```python
import Locales

Locales().example()
```

### Installing

You can install Locales using pip

```sh
$ pip install locales
```
or download `Locales.py` and drop to folder with your project

### Using

```python
import Locales

loc = Locales("filename.json")
loc.set_default_lang("eng")  # Set the language by default

print(loc.get("welcome"))
# Welcome!

print(loc.get("welcome", "ru"))
# Добро пожаловать!

print(loc.get_all("goodbye")
# dict of key "goodbye"  ->  {'ru': 'Пока', 'eng': 'Goodbye', 'sp': 'Adiós'}

print(loc.get_by_name("English"))
# returns the abbreviation(key) of the language  ->  eng
```

## Authors

* **vffuunnyy** - *Initial work* - [@vffuunnyy](https://t.me/vffuunnyy)
