# 🚀 Quick Start Guide

## One-Command Setup

### Windows
```bash
run.bat
```

### Mac/Linux
```bash
chmod +x run.sh
./run.sh
```

This will automatically:
1. ✅ Check Python and Node.js installation
2. ✅ Start FastAPI backend (http://localhost:8000)
3. ✅ Install frontend dependencies
4. ✅ Launch React app (http://localhost:3000)

---

## Manual Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Step 1: Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Train the models (if not already trained)
python train_linear_regression.py
python train_decision_tree.py
python train_xgboost.py
python train_neural_network.py

# Start the API server
python app.py
```

The API will be available at: `http://localhost:8000`

### Step 2: Frontend Setup

**In a new terminal/command prompt:**

```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The app will open at: `http://localhost:3000`

---

## Project Structure

```
Salary_Pred/
├── 📄 app.py                          # FastAPI backend ⭐
├── 📄 preprocessing.py
├── 📄 train_*.py                      # Model training scripts
├── 📄 ensemble_predict.py             # CLI predictor
├── 📄 ds_salaries.csv                # Dataset
├── 📄 requirements.txt                # Python dependencies
├── 📄 run.bat / run.sh               # Quick start scripts
├── 📄 README.md
├── 📄 QUICK_START.md                 # This file
│
└── 📁 frontend/                       # React Application ⭐
    ├── 📁 src/
    │   ├── 📄 index.js               # Entry point
    │   ├── 📄 App.js                 # Main app with routing
    │   ├── 📄 index.css              # Global styles
    │   └── 📁 pages/
    │       ├── 📄 Landing.js         # Home page
    │       ├── 📄 Landing.css
    │       ├── 📄 Predictor.js       # Prediction form
    │       └── 📄 Predictor.css
    ├── 📁 public/
    │   └── 📄 index.html
    ├── 📄 package.json               # Dependencies
    └── 📄 FRONTEND_SETUP.md          # Frontend docs
```

---

## Using the Application

### 1. Landing Page (Home)
- **URL**: http://localhost:3000/
- Beautiful hero section with features
- Call-to-action button to start predicting
- Showcase of 4 ML models

### 2. Predictor Page
- **URL**: http://localhost:3000/predict
- Fill in your job details:
  - Work year (2000-2030)
  - Experience level (EN, MI, SE, EX)
  - Employment type (FT, PT, CT, FL)
  - Job title
  - Salary currency (USD, EUR, GBP, etc.)
  - Employee residence (country code)
  - Remote work ratio (0%, 50%, 100%)
  - Company location
  - Company size (S, M, L)

- **Get Results**:
  - Linear Regression prediction
  - Decision Tree prediction
  - XGBoost prediction
  - Neural Network prediction
  - **Ensemble Average** (final prediction)

---

## API Endpoints

### Health Check
```
GET http://localhost:8000/
```

Response:
```json
{"message": "Salary Prediction API is running!"}
```

### Get Prediction
```
POST http://localhost:8000/predict
```

Request body:
```json
{
  "work_year": 2024,
  "experience_level": "SE",
  "employment_type": "FT",
  "job_title": "Data Scientist",
  "salary_currency": "USD",
  "employee_residence": "US",
  "remote_ratio": 100,
  "company_location": "US",
  "company_size": "L"
}
```

Response:
```json
{
  "linear_regression": 145000.50,
  "decision_tree": 158000.00,
  "xgboost": 152000.75,
  "neural_network": 150000.25,
  "ensemble_prediction": 151250.38
}
```

---

## Features

✨ **Beautiful UI**
- Modern dark theme with gradient backgrounds
- Glassmorphism effect
- Smooth animations and transitions
- Fully responsive design

🤖 **Ensemble Predictions**
- 4 different ML algorithms
- Individual predictions from each model
- Ensemble average for robust results

⚡ **Real-time Results**
- Instant predictions
- Error handling and validation
- Loading states

📊 **Data Insights**
- Based on real salary data
- Market-driven predictions
- Considers multiple job factors

---

## Troubleshooting

### "Failed to get predictions"
- Ensure FastAPI is running: `python app.py`
- Check models are in the main directory
- Verify port 8000 is not in use

### React app won't start
- Verify Node.js is installed: `node --version`
- Clear node_modules: `rm -rf node_modules` then `npm install`
- Try different port: `PORT=3001 npm start`

### Port already in use
Windows:
```bash
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

Mac/Linux:
```bash
lsof -i :3000
kill -9 <PID>
```

### Models not found
Ensure you've trained the models:
```bash
python train_linear_regression.py
python train_decision_tree.py
python train_xgboost.py
python train_neural_network.py
```

---

## Development

### Customizing Colors
Edit `frontend/src/index.css` CSS variables:
```css
:root {
  --primary: #6366f1;      /* Primary blue */
  --secondary: #8b5cf6;    /* Purple */
  --accent: #ec4899;       /* Pink */
  --success: #10b981;      /* Green */
}
```

### Changing API URL
Edit `frontend/src/pages/Predictor.js`:
```javascript
const response = await axios.post('http://localhost:8000/predict', formData);
```

### Adding New Features
- Create new page in `frontend/src/pages/`
- Add route in `frontend/src/App.js`
- Import and use with React Router

---

## Deployment

### Frontend
```bash
cd frontend
npm run build
# Deploy the 'build' folder to Vercel, Netlify, or any static host
```

### Backend
```bash
# Install production server
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

---

## Next Steps

- [ ] Train models with more data
- [ ] Add model comparison charts
- [ ] Implement user authentication
- [ ] Add salary history tracking
- [ ] Create API documentation (Swagger)
- [ ] Add caching for faster predictions
- [ ] Deploy to cloud (AWS, GCP, Azure)

---

## Support

For issues or questions:
1. Check [README.md](README.md)
2. Review [frontend/FRONTEND_SETUP.md](frontend/FRONTEND_SETUP.md)
3. Check error messages in browser console and terminal

---

**Happy predicting! 🎯**
