# 🎓 Telegram Result Bot 📲

A simple Telegram bot that lets students check their **exam results** by choosing the semester and entering their **Hall Ticket Number**. It extracts data from PDF files and sends back clean, subject-wise results.

---

## 📽️ Demo Video

👉 [Watch Demo Video](#) *(Add your video link here — YouTube/Drive/etc.)*

---

## ✨ Features

- 📚 Choose semester from a button list
- 🆔 Enter Hall Ticket number to fetch results
- 📄 See subject-wise results: Subcode, Name, Internals, Grade, and Credits
- ⚡ Fast and user-friendly Telegram experience
- 🔍 Uses PyMuPDF to parse structured PDFs

---

## 🚀 How It Works

1. User sends `/start`
2. Bot shows available semesters (from PDF files)
3. User selects semester
4. Bot asks for Hall Ticket Number
5. Results are fetched and displayed

---

## 🛠️ Tech Stack

- Python 🐍
- python-telegram-bot 🤖
- PyMuPDF 📄

---

## 📁 Folder Structure

```
telegram-result-bot/
│
├── results/              # Folder with semester result PDFs
├── main.py               # Bot source code
└── README.md             # You're reading it!
```

---

## 🧪 Sample Output

```
📄 Results for 216C1A5454 - R201114

📘 R201114 - ENVIRONMENTAL SCIENCE  
📎 Internals: 0 | Grade: COMPLE | Credits: 0
```

---

## 🔧 Setup & Run Locally

1. Clone the repo  
   `git clone https://github.com/yourusername/telegram-result-bot.git && cd telegram-result-bot`

2. Install dependencies  
   `pip install python-telegram-bot PyMuPDF`

3. Add PDF result files to the `results/` folder

4. Update `main.py` with your Bot Token  
   ```python
   token = "YOUR_BOT_TOKEN"
   ```

5. Run the bot  
   `python main.py`

---

## ⚠️ Notes

- PDF results should follow this structure:
  ```
  HTNO
  Subcode
  Subname
  Internals
  Grade
  Credits
  ```
- Only text-based PDFs work (not scanned images)
- All `.pdf` files should go in the `results/` folder

```

## 📄 License

MIT License - free to use, share, and improve!
