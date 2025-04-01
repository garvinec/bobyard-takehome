# Bobyard Take Home

## Project Structure

The project consists of two main parts:

- **Frontend**: React application built with Vite
- **Backend**: Django REST Framework API

## Setup Instructions

### Backend Setup

Open your terminal

1. Navigate to the backend directory:

   ```
   cd backend
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Go to the bobyardTakeHome Directory

   ```
   cd bobyardTakeHome
   ```

6. Set up the PostgreSQL database:

   - Install PostgreSQL if not already installed
   - Create a database named "bobyarddb"
   - Change the DB_PASSWORD to your postgres password on line 79 of bobyardTakeHome/settings.py

7. Run migrations:

   ```
   python manage.py migrate
   ```

8. Populate DB

   ```
   python manage.py populatedb
   ```

9. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

Open a separate window in your terminal

1. Navigate to the frontend directory:

   ```
   cd frontend
   ```

2. Install dependencies:

   ```
   npm install
   ```

   or

   ```
   yarn
   ```

3. Start the development server:

   ```
   npm run dev
   ```

   or

   ```
   yarn dev
   ```

4. Open your browser and navigate to your local host URL.
