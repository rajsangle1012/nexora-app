# Nexora - Intelligent Knowledge Management System

Nexora is a powerful, AI-driven knowledge management system that combines document processing, intelligent Q&A, and podcast generation capabilities. Built with Django backend and React frontend, it leverages Google's Gemini AI for advanced document understanding and content generation.

## 🚀 Features

- **📚 Knowledge Base Management**: Create and organize multiple knowledge bases
- **📄 Document Processing**: Upload and process PDF, TXT, and other document formats
- **🤖 AI-Powered Q&A**: Interactive chat with your documents using Google Gemini AI
- **🎧 Podcast Generation**: Convert your knowledge bases into engaging podcast conversations
- **💬 Chat Sessions**: Maintain conversation history with your documents
- **🔍 Source Citations**: Get accurate citations and references for AI responses
- **📱 Modern UI**: Clean, responsive React-based user interface

## 🛠️ Technology Stack

### Backend

- **Django 4.2.14** - Web framework
- **Django REST Framework** - API development
- **Google Gemini AI** - AI processing and generation
- **SQLite** - Database (easily configurable to PostgreSQL/MySQL)
- **Python 3.9+** - Programming language

### Frontend

- **React 19.1.1** - UI framework
- **TypeScript** - Type-safe development
- **Vite** - Build tool and development server
- **React Markdown** - Markdown rendering
- **PDF.js** - PDF processing

## 📋 Prerequisites

Before installing Nexora, ensure you have the following installed:

- **Python 3.9 or higher**
- **Node.js 16 or higher**
- **npm or yarn**
- **Git**

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Crazymind7/Nexora
cd intelligent-notebook
```

### 2. Backend Setup (Django)

#### Navigate to Backend Directory

```bash
cd Nexora_backend
```

#### Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### Environment Configuration

Create a `.env` file in the `Nexora_backend` directory:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
DEBUG=True
SECRET_KEY=your_secret_key_here
```

#### Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Start Django Development Server

```bash
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 3. Frontend Setup (React)

#### Navigate to Frontend Directory

```bash
# From project root
cd ..  # Go back to project root if in Nexora_backend
```

#### Install Node.js Dependencies

```bash
npm install
```

#### Start Vite Development Server

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173`

## 🔑 API Configuration

### Google Gemini API Setup

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Add the API key to your `.env` file:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

## 📖 Usage

### 1. Creating Knowledge Bases

- Navigate to the application in your browser
- Click "Create Knowledge Base"
- Provide a name and description
- Start uploading documents

### 2. Document Upload

- Select your knowledge base
- Upload PDF, TXT, or other supported document formats
- Wait for processing to complete
- Documents are automatically indexed for AI queries

### 3. AI Chat Interface

- Select a knowledge base
- Start asking questions about your documents
- Get AI-powered responses with source citations
- View conversation history

### 4. Podcast Generation

- Select a knowledge base with uploaded documents
- Choose "Generate Podcast"
- Customize speaker names and content focus
- Download the generated audio podcast

## 🏗️ Project Structure

```text
intelligent-notebook/
├── Nexora_backend/           # Django backend
│   ├── api/                   # Main API app
│   │   ├── models.py         # Database models
│   │   ├── views.py          # API endpoints
│   │   ├── serializers.py    # Data serialization
│   │   ├── utils.py          # Utility functions
│   │   └── urls.py           # URL routing
│   ├── Nexora/              # Django project settings
│   │   ├── settings.py       # Configuration
│   │   ├── urls.py           # Main URL routing
│   │   ├── wsgi.py           # WSGI application
│   │   └── asgi.py           # ASGI application
│   ├── media/                # Uploaded files
│   ├── manage.py             # Django management
│   └── requirements.txt      # Python dependencies
├── components/               # React components
├── services/                 # API services
├── utils/                    # Utility functions
├── package.json             # Node.js dependencies
├── vite.config.ts           # Vite configuration
└── tsconfig.json            # TypeScript configuration
```

## 🔗 API Endpoints

### Knowledge Bases

- `GET /api/knowledge-bases/` - List all knowledge bases
- `POST /api/knowledge-bases/` - Create new knowledge base
- `GET /api/knowledge-bases/{id}/` - Get knowledge base details
- `DELETE /api/knowledge-bases/{id}/` - Delete knowledge base

### File Upload

- `POST /api/upload/` - Upload file to knowledge base
- `GET /api/files/` - List uploaded files
- `DELETE /api/files/{id}/` - Delete uploaded file

### Chat

- `POST /api/chat/` - Send chat message
- `GET /api/chat-sessions/` - List chat sessions
- `GET /api/chat-sessions/{id}/messages/` - Get chat history

### Podcast Generation

- `POST /api/generate-podcast/` - Generate podcast from knowledge base
- `GET /api/podcasts/` - List generated podcasts
- `GET /api/podcasts/{id}/` - Download podcast audio

## 🚀 Development

### Running Tests

```bash
# Backend tests
cd Nexora_backend
python manage.py test

# Frontend tests
npm test
```

### Building for Production

```bash
# Frontend build
npm run build

# Django static files
cd Nexora_backend
python manage.py collectstatic
```

## 🔧 Configuration

### Django Settings

Key settings in `Nexora_backend/Nexora/settings.py`:

- `ALLOWED_HOSTS` - Configure allowed hosts for production
- `CORS_ALLOWED_ORIGINS` - Configure CORS for frontend
- `DATABASES` - Database configuration
- `MEDIA_ROOT` - File upload directory

### Frontend Configuration

Vite configuration in `vite.config.ts`:

- Proxy settings for API calls
- Build optimization
- TypeScript compilation

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | Required |
| `DEBUG` | Django debug mode | `True` |
| `SECRET_KEY` | Django secret key | Generated |
| `DATABASE_URL` | Database connection string | SQLite |

## 🐛 Troubleshooting

### Common Issues

1. **Gemini API Errors**
   - Verify API key is correct
   - Check API quota and billing
   - Ensure network connectivity

2. **File Upload Issues**
   - Check file size limits
   - Verify file format support
   - Check media directory permissions

3. **CORS Errors**
   - Verify CORS settings in Django
   - Check frontend proxy configuration
   - Ensure correct origins are allowed

### Logs and Debugging

```bash
# Django logs
cd Nexora_backend
python manage.py runserver --verbosity=2

# Check Django admin for detailed error logs
# Visit http://localhost:8000/admin/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:

- Create an issue in the repository
- Check existing documentation
- Review troubleshooting section

## 🔄 Updates and Versioning

- Current version: 1.0.0
- Check releases page for updates
- Follow semantic versioning
