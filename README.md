
# Free Image Generator

A web application that generates images based on user prompts using the freeGPT API.

## Features

- Generate images from text prompts.
- Display generated images on the same page.
- Handle errors gracefully.

## Installation

### Prerequisites

- Python 3.x
- Flask
- PIL (Pillow)
- freeGPT

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/NagiPragalathan/FreeImageGenerator.git
    cd FreeImageGenerator
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter a prompt in the input field and click "Generate Image".

4. The generated image will be displayed on the same page.

## Deployment

### Vercel

1. Install Vercel CLI:
    ```bash
    npm install -g vercel
    ```

2. Deploy the application:
    ```bash
    vercel
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
