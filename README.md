# FPL_Project

# ⚽ FPL_Project

A modern, monetized spin on the Fantasy Premier League!  
**FPL_Project** allows users to create, join, and compete in custom leagues with real rewards, simplified payments, and a vibrant football community.

---

## 🚀 Features

- 🌍 Create or join fantasy football leagues based on real Premier League matches
- 💰 Pay entry fees securely via M-Pesa, PayPal, or Stripe
- 🏆 Automatic reward distribution to league winners
- 🧠 Real-time updates based on official FPL statistics
- 🔐 Secure user authentication and league management
- 🎨 Clean and responsive UI, inspired by the official FPL design

---

## 💼 Premium Features

- Create private or public paid leagues
- Set custom entry fees and prize pools
- Manage payouts and invite-only access
- View detailed player and team performance analytics

---

## 🛠️ Tech Stack

- **Backend:** Django, PostgreSQL
- **Frontend:** Django Templates, Bootstrap
- **Payments:** M-Pesa API, Stripe, PayPal
- **Task Scheduler:** Celery (periodic FPL API updates)
- **Deployment:** Render / Railway / GitHub Actions

---

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/KemboiK/FPL_Project.git
cd FPL_Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set up your environment variables (.env)
# Run migrations and start the server
python manage.py migrate
python manage.py runserver
