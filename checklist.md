# Project Ideas Checklist

---

## Beginner → Intermediate
*Solidify fundamentals & modules you’ve learned*

### Text Analyzer
- **Input:** a text file
- **Features:**
  - Count word frequencies (use `collections.Counter`)
  - Find most common words
  - Output a summary report

### Task Manager (with `deque`)
- **Features:**
  - Add tasks (enqueue)
  - Process tasks (dequeue)
  - Support priority tasks (appendleft)

### Password Generator
- **Features:**
  - Use `itertools.product` to generate passwords of given length
  - Or use `random.choice` for randomized passwords

---

## Intermediate → Advanced
*Use decorators, context managers, JSON, API requests*

### Personal Finance Tracker
- **Features:**
  - Track expenses in JSON
  - Show monthly totals
  - Export reports to CSV

### Weather App (API project)
- **Features:**
  - Fetch weather from a free API (use `requests`)
  - Save results in JSON
  - Display neatly with formatting

### Web Scraper
- **Features:**
  - Use `requests` + `BeautifulSoup`
  - Collect headlines, product prices, or quotes
  - Store in a file

---

## Advanced but Fun
*Concurrency & real-world utilities*

### Bulk Image Downloader
- **Input:** list of URLs
- **Features:**
  - Download them with threading or asyncio
  - Save to a folder

### Chatbot (Mini)
- **Features:**
  - Rule-based responses (not AI, just keyword matching)
  - Load “intents” from JSON
  - Respond to user input in terminal

### Todo Web App
- **Features:**
  - Use Flask to build a simple CRUD app
  - Store todos in JSON or SQLite
  - Run locally in browser