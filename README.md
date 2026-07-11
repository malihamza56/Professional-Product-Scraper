# 📚 Books Scraper (Python)

A production-style Python web scraping project that extracts book information from **Books to Scrape**, cleans the data, and exports it into multiple file formats.

## 🚀 Features

- Fetch HTML using the Requests library
- Parse HTML with BeautifulSoup
- Extract book information
- Clean and transform raw data
- Export data to:
  - JSON
  - CSV
  - Excel
- Centralized logging
- Modular project architecture
- Exception handling throughout the project

---

# 📂 Project Structure

```
Products_Scraper/
│
├── config.py
├── logger.py
├── scraper.py
├── parser.py
├── cleaner.py
├── exporter.py
├── main.py
│
├── Data/
│   ├── raw/
│   │   ├── books.html
│   │   └── raw_books.json
│   │
│   └── processed/
│       ├── books.json
│       ├── books.csv
│       └── books.xlsx
│
├── Logs/
│   └── scraper.log
│
├── requirements.txt
└── README.md
```

---

# 🛠 Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- OpenPyXL
- Logging

---

# 📖 Workflow

```
Website

    ↓

Fetch HTML

    ↓

Parse HTML

    ↓

Extract Raw Data

    ↓

Clean Data

    ↓

Export Files

(JSON / CSV / Excel)
```

---

# 📄 Extracted Fields

Each book contains:

- Title
- Price
- Rating
- Availability
- Product Link
- Image Link

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Products_Scraper.git
```

Move into the project

```bash
cd Products_Scraper
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# 📦 Output Files

### Raw Data

- books.html
- raw_books.json

### Processed Data

- books.json
- books.csv
- books.xlsx

---

# 📝 Logging

All scraping activities and errors are recorded in:

```
Logs/scraper.log
```

---

# 💡 Future Improvements

- Pagination support
- Retry mechanism
- Random User-Agent rotation
- Proxy support
- Command-line arguments
- Database integration
- Multi-threaded scraping

---

# 📸 Sample Output

| Title | Price | Rating | Availability |
|-------|------:|--------:|-------------|
| A Light in the Attic | 51.77 | 3 | True |
| Tipping the Velvet | 53.74 | 1 | True |

---

# 📄 License

This project is created for learning and educational purposes.

---

# 👨‍💻 Author

**Hamza**

Computer Science Student

Python • Web Scraping • Automation • Data Processing