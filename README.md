# 👟 Footwear — E-Commerce Platform

> A full-stack footwear e-commerce web application built with **Django**, **SQLite**, **Razorpay** payment integration, and server-side rendered templates.

---

## 📖 Overview

**Footwear** is a multi-role e-commerce platform that connects **buyers** and **sellers** of footwear products. Buyers can browse a wide catalogue of shoes, filter by gender, category, and size, add items to their wishlist or cart, and complete purchases via **Razorpay** payment gateway. Sellers get their own dashboard to list, update, and manage their product inventory.

Key highlights:

- **Buyer experience** — browse, search, wishlist, cart, checkout, and online payment.
- **Seller dashboard** — add products with images, view listings, edit details, and delete items.
- **Razorpay integration** — secure payment processing with real-time order confirmation.
- **Email-based OTP** — password-reset flow using Django's built-in mail framework.
- **Role-based access** — separate interfaces and permissions for buyers and sellers.

---

## ✨ Features

### 🛒 Buyer Module
| Feature | Description |
|---|---|
| **Home / Index** | Landing page showcasing featured products |
| **Product Catalogue** | Browse all available footwear products |
| **Product Details** | View detailed product info (brand, price, description, image) |
| **Wishlist** | Save products to a personal wishlist for later |
| **Shopping Cart** | Add products, adjust quantities, view running total |
| **Checkout & Payment** | Secure checkout with Razorpay payment gateway |
| **Order Confirmation** | Order-complete page after successful payment |
| **Profile** | View and manage account details |
| **Auth** | Signup, Login, Logout, Change Password, Forgot Password (OTP) |
| **Static Pages** | About, Contact |

### 🏪 Seller Module
| Feature | Description |
|---|---|
| **Seller Dashboard** | Overview of listed products and sales |
| **Add Product** | List a new product with image, pricing, category, gender, and size |
| **View Products** | Browse all of your listed products |
| **Edit Product** | Update product details (name, price, description, image, etc.) |
| **Delete Product** | Remove a product from the catalogue |
| **Profile** | View and manage seller account details |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3, Django |
| **Database** | SQLite 3 |
| **Frontend** | Django Templates (HTML5), CSS, JavaScript |
| **Payment Gateway** | Razorpay |
| **Email** | Django `send_mail` (SMTP) |
| **Media Handling** | Django `ImageField` with file uploads |

---

## 📁 Project Structure

```
Footwear_complete/
├── myproject/
│   ├── myapp/
│   │   ├── migrations/      # Django database migrations
│   │   ├── static/          # CSS, JavaScript, images
│   │   ├── templates/       # HTML templates (28 pages)
│   │   ├── models.py        # Data models (User, Product, Wishlist, Cart)
│   │   ├── views.py         # Business logic & route handlers
│   │   ├── urls.py          # URL routing configuration
│   │   └── admin.py         # Django admin registration
│   ├── myproject/
│   │   ├── settings.py      # Django settings & configuration
│   │   ├── urls.py          # Root URL configuration
│   │   └── wsgi.py          # WSGI entry point
│   ├── media/               # User-uploaded files (profile pics, product images)
│   ├── db.sqlite3           # SQLite database
│   ├── manage.py            # Django management utility
│   └── requirements.txt     # Python dependencies
└── venv/                    # Python virtual environment
```

---

## 📊 Data Models

| Model | Key Fields | Description |
|---|---|---|
| **User** | `fname`, `lname`, `email`, `mobile`, `password`, `profile`, `usertype` | Stores buyer & seller accounts (role determined by `usertype`) |
| **Product** | `seller` (FK), `gen`, `cat`, `sz`, `bname`, `pname`, `price`, `desc`, `pimage` | Footwear product listing linked to a seller |
| **Wishlist** | `user` (FK), `product` (FK), `ttime` | Buyer's saved-for-later items |
| **Cart** | `user` (FK), `product` (FK), `qty`, `total`, `roundtotal`, `payment` | Shopping cart with quantity and payment status tracking |

### Product Taxonomy

- **Gender:** Male, Female, Kids
- **Category:** Casual, Sports, Sneakers, Flip-Flops, Party, Crocs, Sandals
- **Size:** S, M, L, XL, XXL

---

## 🚀 Getting Started

### Prerequisites

- **Python** ≥ 3.8
- **pip** (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd Footwear_complete/myproject

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Database Setup

```bash
# Apply migrations
python manage.py makemigrations
python manage.py migrate
```

### Running the Application

```bash
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 💳 Payment Integration

The application uses **Razorpay** for payment processing. To enable payments:

1. Create a [Razorpay account](https://razorpay.com/) and obtain your API keys.
2. Add your keys to `myproject/settings.py`:

```python
RAZORPAY_KEY_ID = 'your_key_id'
RAZORPAY_KEY_SECRET = 'your_key_secret'
```

---

## 📬 Key URL Routes

| URL | Description |
|---|---|
| `/` | Home page |
| `/product/` | Product catalogue |
| `/pdetails/<id>` | Product details |
| `/wishlist/` | User's wishlist |
| `/cart/` | Shopping cart |
| `/checkout/` | Checkout page |
| `/signup/` | User registration |
| `/login/` | User login |
| `/sindex/` | Seller dashboard |
| `/sadd_details/` | Add new product (seller) |
| `/viewprod/` | View seller's products |

---

## 📄 License

This project is developed for educational / portfolio purposes.

---

<p align="center">Made with ❤️ by the Footwear E-Commerce team</p>
