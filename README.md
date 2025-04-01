# Bobyard Take Home

## Project Structure

The project consists of two main parts:

- **Frontend**: React application built with Vite
- **Backend**: Django REST Framework API

## Setup Instructions

### Backend Setup

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

4. Go to the bobyardTakeHome Directory

   ```
   cd bobyardTakeHome
   ```

5. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend Setup

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
