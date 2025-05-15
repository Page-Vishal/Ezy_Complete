# EzyBot Server [![Made with Prisma](http://made-with.prisma.io/indigo.svg)](https://prisma.io)


![Python](https://img.shields.io/badge/Python-3.11-blue)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-green)
![Prisma](https://img.shields.io/badge/ORM-Prisma-orange)
![Made with ❤️ in Nepal](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20in%20Nepal-purple)

A lightweight **FastAPI** server for hosting the EzyBot backend with **Docker** support.

The main python code for the project is in: [EzyBot](https://github.com/Page-Vishal/ezybot)

## 🚀 Features

- FastAPI-based lightweight server
- Prisma ORM for MongoDB communication
- Secure environment with `.env` configuration
- Dockerfile and Docker Compose support for easy deployment

## 🛠️ Tech Stack

- **Backend**: Python (FastAPI)
- **Database**: MongoDB
- **ORM**: Prisma ORM
- **Containerization**: Docker, Docker Compose

## ⚙️ Installation and Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Page-Vishal/ezybot-server.git
   cd ezybot-server
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**  
   Create a `.env` file with:
   ```env
   GROQ_API_KEY=your_groq_api_key
   DATABASE_URL=your_mongodb_url
   ```

4. **Run the server locally**
   ```bash
   uvicorn main:app --reload
   ```
   ---
   OR
   ---
   ```bash
   python script.py
   ```
   

## 🐳 Running with Docker

1. **Build the Docker image**
   ```bash
   docker build -t ezybot-server .
   ```

2. **Run using Docker Compose**
   ```bash
   docker-compose up
   ```

---

### 📢 Notes
- Prisma migrations and generation must be done before building the Docker image if the schema is updated.
- Server endpoints will be documented via FastAPI's auto-generated docs at `/docs`.

