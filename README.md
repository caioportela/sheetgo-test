# sheetgo-test

## Installation

```bash
$ git clone https://github.com/caioportela/sheetgo-test.git
$ cd sheetgo-test
$ pip install -r requirements.txt
```
## Usage

To run the application use
```bash
$ export FLASK_APP=src/app.py
$ flask run
```
or simply
```bash
$ python src/app.py
```

The application is now running on `http://localhost:5000`.

-------------------------------------------------------------

Authorization is needed in all endpoints and there's a script to generate a valid token.

```bash
$ python src/auth_token.py
```

-------------------------------------------------------------

Requesting the API through cURL with a valid token:
- `/excel/info` - Returns the list of the tabs from the excel file, ordered alphabetically
  - `file`: binary xlsx file  
  
  ```bash 
  $ curl -X POST http://localhost:5000/excel/info -H "Authorization:$(python src/auth_token.py)" -F file=@sample1.xlsx
  ```
  
  
- `/image/convert`- Converts the format of an image
  - `file`: image file to convert
  - `format`: format of the output image; `jpeg` or `png`
  
  ```bash
  $ curl -X POST http://localhost:5000/image/convert -H "Authorization:$(python src/auth_token.py)" -F file=@image1.jpeg -F format=png
  ```
  
- `/image/convert/fromdropbox` - Converts the format of an image from [Dropbox](https://www.dropbox.com) to `jpeg` or `png`
  - `Dropbox-Token`: generated access token from dropbox app
  - `path`: path of the image stored on dropbox
  - `format`: format of the output image; `jpeg` or `png`
  
  ```bash
  $ curl -X POST http://localhost:5000/image/convert/fromdropbox -H "Authorization:$(python src/auth_token.py)" -H "Dropbox-Token:<access_token>" -d path=/image.jpeg -d format=png
  ```
  
## Unit Tests

[`pytest`](https://docs.pytest.org/en/stable/index.html) was used for the unit testing

```bash
$ pytest
```
