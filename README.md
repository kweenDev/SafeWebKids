# SafeWebKids

_(To be updated as project is completed)_

SafeWebKids is a web application designed to provide a safe and educational environment for children. It features user management, quizzes, a registration and login system. This project is built using Django for the backend and React.js for the frontend.

## Table of Contents

- [SafeWebKids](#safewebkids)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Available Scripts](#available-scripts)
  - [Backend Setup](#backend-setup)
    - [Virtual Environment](#virtual-environment)
    - [Django](#django)
  - [Frontend Setup](#frontend-setup)
    - [React.js](#reactjs)
  - [Folder Structure](#folder-structure)

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Node.js
- npm
- MySQL

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/SafeWebKids.git
   cd SafeWebKids
   ```

## Project Structure

SafeWebKids/
├── backend/
│ ├── core/
│ ├── safewebkids/
│ ├── manage.py
│ └── ...
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ ├── App.js
│ │ ├── index.js
│ │ └── store.js
│ ├── package.json
│ └── ...
├── README.md
└── ...

## Available Scripts

In the project directory, you can run:

#### Backend Setup

##### Virtual Environment

1. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

2. Install dependencies:

```sh
cd backend
pip install -r requirements.txt
```

##### Django

1. Create a `.env` file in the `backend` directory with the following content:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=safewebkids
DATABASE_USER=root
DATABASE_PASSWORD=your_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
```

2. Apply migrations and start the server:

```sh
python manage.py migrate
python manage.py runserver
```

#### Frontend Setup

##### React.js

1. Install frontend dependencies:

```sh
cd frontend
npm install
```

2. Start the React development server:

```sh
npm start
```

This will start the frontend server on `http://localhost:3000` and the backend server on `http://localhost:8000`.

## Folder Structure

### Backend

- `backend/safewebkids/`: Django project settings.
- `backend/core/`: Django app for core functionality.
- `backend/manage.py`: Django management script.

### Frontend

- `frontend/src/components/`: React components.
- `frontend/src/App.js`: Main application component.
- `frontend/src/index.js`: Entry point for React.
- `frontend/src/store.js`: Redux store configuration.

## Author

Refiloe Radebe (_kweenDev_)
