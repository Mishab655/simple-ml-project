# Simple ML Project

A simple ML pipeline using Logistic Regression, FastAPI, Docker, and GitHub Actions.

## Steps

### Local Run
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Generate data and train model
   ```bash
   python data/generate_data.py
   python src/train.py
   ```
3. Start FastAPI app
   ```bash
   uvicorn app.main:app --reload
   ```

### Docker Run
```bash
docker build -t simple-ml-app .
docker run -p 8000:8000 simple-ml-app
```

### GitHub Actions
Automatically installs dependencies, runs tests, trains model, and uploads `models/` as an artifact.
