# map-be

A React.js application served using **Nginx** and deployed on **Google Cloud Run**.

## 🚀 Features
- React frontend built with Node.js
- Served via Nginx for optimized performance
- Containerized using Docker
- CI/CD using Google Cloud Build
- Deployed on Google Cloud Run

---

## 🛠️ Setup & Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Raghavendra17N/Simple-Backend-APP.git
cd map-be
```

### **2️⃣ Install Dependencies**
```sh
npm install
```

### **3️⃣ Run Locally**
```sh
npm start
```
App runs on `http://localhost:3000`

---

## 🐳 Docker Setup
### **1️⃣ Build Docker Image**
```sh
docker build -t map-be .
```

### **2️⃣ Run Docker Container**
```sh
docker run -e PORT=8080 -p 8080:8080 map-be
```
App runs on `http://localhost:8080`

---

## 🚀 Deploying to Google Cloud Run
### **1️⃣ Authenticate & Set Project**
```sh
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### **2️⃣ Build & Push Docker Image**
```sh
docker build -t gcr.io/YOUR_PROJECT_ID/map-be .
docker push gcr.io/YOUR_PROJECT_ID/map-be
```

### **3️⃣ Deploy to Cloud Run**
```sh
gcloud run deploy map-be \
  --image gcr.io/YOUR_PROJECT_ID/map-be \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
```
After deployment, Cloud Run provides a URL like:
```
https://map-backend-320668246657.xyz.run.app/
```

### 🌐 **Live App URL**
[Click here to access the app](https://map-backend-320668246657.us-central1.run.app/)

---

## 🔄 CI/CD with Google Cloud Build
### **Trigger Deployment on Git Push**
A Cloud Build trigger automatically builds and deploys the app on every push to `main`.

To manually trigger:
```sh
gcloud builds submit --config cloudbuild.yaml .
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 💡 Contributing
We welcome contributions! Feel free to submit PRs or open issues.

---

## 📞 Contact
For queries, reach out at: **lahariamudala10@gmail.com**
