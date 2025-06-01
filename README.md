# AutoDocx

AutoDocx is a simple Python application that automates the process of filling out Word document templates with user-provided information. It features a user-friendly GUI for entering data and generates ready-to-use `.docx` files based on your templates.

## Features

- Fill multiple Word templates at once with custom data
- Easy-to-use graphical interface (Tkinter)
- Supports placeholders for name, address, ID code, and email
- Outputs ready documents to a dedicated folder

## Usage

1. **Prepare your templates:**  
   Place your `.docx` template files in the `templates/` folder. Use placeholders like `{name}`, `{address}`, `{id_code}`, and `{email}` in your documents.

2. **Run the application:**  
   ```sh
   python main.py
   ```
3. **Enter your data:**
Fill in your name, address, ID code, and email in the GUI, then click "Submit".

4. **Get your documents:**
The filled documents will be saved in the `ready/` folder as `ready_1.docx`, `ready_2.docx`, etc.

**Requirements**
Python 3.7+
python-docx

**Install dependencies with:**
```sh
pip install -r requirements.txt
```

### Project Structure
```sh
AutoDocx/
├── app.py
├── main.py
├── word_replacing.py
├── requirements.txt
├── templates/
│   └── template1.docx
│   └── template2.docx
├── ready/ 
│   └── ready_1.docx
│   └── ready_2.docx
└── README.md
```

##License
[MIT license](https://github.com/qannje/auto-docx/blob/master/LICENSE)

Made with ❤️.
