# 📄 DRF DOCX TO PDF API

A Django REST Framework project that allows users to upload a DOCX file and automatically convert it into a PDF document.

---

## 🚀 Features

* Upload DOCX files through a web interface.
* Convert Word documents to PDF.
* Download the generated PDF instantly.
* Automatic file cleanup after conversion.
* Error handling for invalid files.
* Built using Django REST Framework.

---

## 🛠 Technologies Used

* Python
* Django
* Django REST Framework
* docx2pdf
* HTML
* File Handling
* FileSystemStorage

---

## 📁 Project Structure

```text
doc-to-pdf/
│
├── api/
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── myproject/
│   ├── settings.py
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

---

## 🔗 API Endpoint

```http
GET  /api/convert/
POST /api/convert/
```

---

## ⚙️ How It Works

1. User uploads a DOCX file.
2. The file is stored temporarily.
3. The `docx2pdf` library converts the document.
4. The original DOCX file is deleted.
5. The generated PDF is returned as a downloadable file.

---

## ▶️ Installation

```bash
git clone https://github.com/kashaf-fatima794/DRF-DOCX-TO-PDF-API-TERM-PROJECT.git

cd DRF-DOCX-TO-PDF-API-TERM-PROJECT

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

---

## 🌐 URL

```text
http://127.0.0.1:8000/api/convert/
```

---

## 📌 Future Improvements

* Multiple file support
* Drag and drop upload
* User authentication
* Conversion history
* Cloud storage integration


CS Student | Python Developer | Django REST Framework Learner
