# CS50W Project 1: Wiki

## Project Description

This project is a simple wiki website built as part of Harvard's CS50W Web Programming with Python and JavaScript course. The site allows users to create, edit, and view encyclopedia entries written in Markdown.

## Features

- **View Entries**: Users can view a list of all encyclopedia entries.
- **View Entry**: Users can click on an entry to view its content.
- **Search**: Users can search for an entry by its title or content. Partial matches are also displayed.
- **Create New Entry**: Users can create a new encyclopedia entry.
- **Edit Entry**: Users can edit existing encyclopedia entries.
- **Random Entry**: Users can view a random encyclopedia entry.
- **Markdown Support**: Entries are written in Markdown and rendered as HTML.

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap5 CSS
- **Markdown**: Python-Markdown for rendering Markdown content

## Usage

1. **View Entries**: Navigate to the home page to see a list of all encyclopedia entries.
2. **Search Entries**: Use the search bar to find entries by title or content.
3. **Create New Entry**: Click on "Create New Page" to add a new entry.
4. **Edit Entry**: Open an entry and click "Edit" to modify its content.
5. **Random Entry**: Click on "Random Page" to view a random entry.

## Project Structure

- `encyclopedia/`: Contains the main application code.
  - `migrations/`: Database migrations.
  - `static/`: Static files (CSS).
  - `templates/`: HTML templates.
  - `models.py`: Database models.
  - `views.py`: Application views.
  - `urls.py`: URL routing.
- `wiki/`: Project settings and configurations.
  - `settings.py`: Project settings.
  - `urls.py`: Project URL routing.
  - `util.py`: Project encyclopedia query utilities


## Acknowledgements

- The project is part of the [CS50W Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/) course by Harvard University.
