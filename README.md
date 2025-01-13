# Inventory Management System

## Overview

This Inventory Management System is a Django-based web application designed to manage products, suppliers, stock movements, and sales orders. The system provides full CRUD (Create, Read, Update, Delete) operations for managing products and suppliers, tracks stock levels, and allows users to generate sale orders with validation. Additionally, the application supports stock movements (incoming and outgoing), ensuring the accuracy of stock data.

## Features

- **Supplier Management**: Add, edit, and delete suppliers.
- **Product Management**: Add, edit, and delete products. Includes price and stock tracking.
- **Sale Order Management**: Create, edit, complete, and cancel sale orders. Tracks total price and updates stock levels accordingly.
- **Stock Movement Tracking**: Record incoming ("In") or outgoing ("Out") stock movements.
- **Stock Level Check**: View current stock levels for each product.
- **Data Validation**: Ensures correct input for email, phone number, price, stock, etc.
- **User Interface (UI)**: A user-friendly interface to interact with the backend functionality.

## Tech Stack

- **Backend**: Django (Python framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (for development; can be switched to MongoDB if needed)
- **Version Control**: GitHub (for source code management)

## Installation Instructions

### Prerequisites

- Python 3.x
- Django (installed via pip)
- SQLite (default database, no installation required)

### Steps to Set Up

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NavyaBoga1109/Inventory-Management-System.git
   cd Inventory-Management-System
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000` to view the Inventory Management System.

## Usage

### Admin Access:
To access the Django admin interface, navigate to:
`http://127.0.0.1:8000/admin`

Login with the superuser credentials created during setup.

### Features Walkthrough:

1. **Suppliers**: Add new suppliers, edit their information, and remove them.
2. **Products**: Create new products, assign suppliers, and manage stock levels.
3. **Sale Orders**: Create new sale orders by selecting products and quantities, track order status, and handle cancellations/completion.
4. **Stock Movements**: Record stock movements for incoming or outgoing products.
5. **Stock Level Check**: Check the current stock levels of all products.

## Database Model

The database consists of the following models:

- **Supplier**:
  - `name`: The name of the supplier.
  - `email`: The supplier's email address (must be unique).
  - `phone`: The supplier's phone number.
  - `address`: The supplier's physical address.

- **Product**:
  - `name`: The product name.
  - `description`: A brief description of the product.
  - `category`: The category to which the product belongs.
  - `price`: The price of the product.
  - `stock_quantity`: The available stock for the product.
  - `supplier`: A foreign key relation to the Supplier model.

- **Sale Order**:
  - `product`: The product being sold (foreign key to Product).
  - `quantity`: The quantity of the product being sold.
  - `total_price`: The total price of the sale order.
  - `sale_date`: The date when the sale was made.
  - `status`: The status of the order (`Pending`, `Completed`, `Cancelled`).

- **Stock Movement**:
  - `product`: The product whose stock is being updated.
  - `quantity`: The quantity being moved.
  - `movement_type`: The type of movement (`In` for incoming, `Out` for outgoing).
  - `movement_date`: The date when the stock movement occurred.
  - `notes`: Additional notes regarding the movement.

## Screenshots

**Home Page:**

![image](https://github.com/user-attachments/assets/4411646d-2106-4f41-a757-3101ade4b967)

**Supplier List:**

![image](https://github.com/user-attachments/assets/a9d32484-d0ff-417f-825a-50fae737a8a4)

**Product Management:**

![image](https://github.com/user-attachments/assets/38776da3-271e-4ab0-98ac-47337a195e86)

## Roadmap

- **Future Enhancements**:
  - Add filtering options for products and sale orders by categories, date ranges, etc.
  - Implement user authentication and roles for different levels of access (e.g., admin, manager).
  - Integrate MongoDB for a more scalable database solution.
  - Enhance the frontend UI using frameworks like Bootstrap or Tailwind CSS.

## Contribution

1. **Fork the repository** to your own GitHub account.
2. Create a new **branch** for each feature or bug fix.
3. Commit your changes and push to your fork.
4. Submit a **pull request** to the main repository.
