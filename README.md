# MediVision

MediVision is a Flask-based medical support web application that combines symptom-based disease prediction with image-based medical image classification.

## Project Overview

This project provides a user-facing system for:
- Predicting diseases from text symptoms using semantic search and FAISS embeddings.
- Classifying medical images with a trained RandomForest model.
- Tracking user predictions and displaying prediction history.
- Managing users, models, and prediction analytics through an admin dashboard.

## Why This Project Is Useful

- Helps users explore likely medical conditions from symptoms or diagnostic images.
- Demonstrates hybrid AI workflows: NLP for symptom matching and computer vision for medical image analysis.
- Supports a multi-domain dataset structure for bone, brain, eye, lung, and skin conditions.
- Provides an educational prototype for healthcare decision support, clinician dashboards, and ML model monitoring.

## Main Features

- User authentication with admin and regular user roles.
- Symptom text prediction using `SentenceTransformer` embeddings + FAISS index search.
- Image upload and prediction using RandomForest + HOG feature extraction.
- SQLite database for users, predictions, and model metrics.
- Admin pages for user management, model training simulation, and performance analytics.
- Seeded demo accounts and example prediction data.

## Repository Structure

- `app.py` - Flask server, authentication, prediction logic, admin and user routes.
- `templates/` - HTML templates for web pages.
- `static/` - Static assets, including uploaded image storage.
- `model/` - Pretrained files: `faiss.index`, `disease_labels.npy`, `RF.pkl`, and supporting numpy arrays.
- `Dataset/` - Medical image directories used for training or reference.
- `requirements.txt` - Python dependency list.
- `medivision.db` - SQLite database generated at runtime.

## Default User Accounts

- Admin: `admin` / `admin123`
- Demo user: `demo` / `user123`

## How to Run the Project

1. Open a terminal in the project root folder.
2. Create and activate a Python virtual environment:
   - Windows:
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the app:
   ```bash
   python app.py
   ```
5. Open the browser and go to:
   ```text
   http://127.0.0.1:5000
   ```

## Notes for Windows

If installing FAISS or PyTorch on Windows fails, install the CPU versions explicitly:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install faiss-cpu
```

## Supported Prediction Types

- Text symptoms input: Users enter symptoms and receive a best-match disease suggestion.
- Image upload: Users upload a medical image and receive a predicted disease label plus confidence.


  <img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/e5024506-7a42-4378-8655-6d6fa1917530" />


## Additional Information

- The app saves uploaded images to `static/uploads`.
- The SQLite database file `medivision.db` is created automatically on first run.
- Admin routes are available only to the admin account.
- Model training actions on the admin page simulate training and store mock performance metrics.

## License

This project is intended for educational and prototyping purposes.
