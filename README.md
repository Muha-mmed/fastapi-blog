# Beam Blog

Beam Blog is a simple logging API built with FastAPI and SQLite. It allows users to post and comment on blog entries. There's no login required for now, as administrative tasks can be handled via the built-in admin panel powered by SQLAdmin.

## 🚀 Tech Stack

- FastAPI
- SQLite
- SQLAdmin

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Muha-mmed/fastapi-blog.git
   cd beam-blog
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with the necessary configuration (database URL, secret keys, etc.).

4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

## 📌 Usage

Use your terminal or a tool like [Postman](https://www.postman.com/) to send requests to the API.

Example to create a post:
```bash
curl -X POST http://localhost:8000/posts/ -H "Content-Type: application/json" -d '{"title": "Hello", "content": "First post!"}'
```

## 🛠 Admin Panel

Visit:

```bash
http://localhost:8000/admin
```

## 🔐 Authentication

No authentication is required at the moment.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project doesn't currently use a specific license. If you'd like to open-source it, consider adding an [MIT License](https://opensource.org/licenses/MIT) or [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

---

## 🙋‍♂️ Author

Built with ❤️ by [Muhammad](https://www.linkedin.com/in/muhd8/)
