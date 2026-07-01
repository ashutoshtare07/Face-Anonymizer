# 🎭 Real-Time Face Anonymization with OpenCV

A Python-based real-time face anonymization system that uses your webcam to automatically detect and blur human faces using Haar Cascade classification — preserving privacy in live video feeds.

---

## 📸 Demo

> Point your camera at a face → the face region is blurred instantly in the live window.

---

## 🏗️ Architecture

```
Webcam Feed → Grayscale Conversion → Haar Cascade Detection → Blur & Composite → Display
```

| Component | Role |
|-----------|------|
| **OpenCV** | Webcam capture, grayscale conversion, face detection, blur, rendering |
| **Haar Cascade XML** | Pre-trained frontal face classifier (bundled with OpenCV) |

---

## ⚙️ How It Works

1. Each frame is captured from the webcam and converted to **grayscale** for detection
2. The Haar Cascade classifier scans the grayscale frame for frontal face regions
3. Detected face coordinates `(x, y, w, h)` are mapped back onto the **original color frame**
4. Each face region is extracted, blurred with a `15×15` kernel, and composited back into the frame
5. The anonymized frame is displayed in real-time

---

## 🧠 Why Haar Cascades?

- Pre-trained on thousands of positive/negative face images — no custom training needed
- Grayscale processing reduces computational load vs. full color frames
- `detectMultiScale` handles faces at varying distances in a single pass
- Lightweight enough for real-time CPU inference — no GPU required

---

## 🔍 Detection & Blur Pipeline

| Step | Operation | Detail |
|------|-----------|--------|
| Grayscale conversion | `cv2.cvtColor` | Reduces noise, speeds up detection |
| Face detection | `detectMultiScale` | `scaleFactor=5.5`, `minNeighbors=1` |
| Region extraction | Array slicing | Sliced from **color** frame, not grayscale |
| Blur | `cv2.blur` | Box blur with `15×15` kernel |
| Compositing | Direct array assignment | Blurred slice written back in-place |

> ⚠️ **Tip:** The current `scaleFactor=5.5` is aggressive and may miss faces. Values between `1.1`–`1.3` give much better detection accuracy.

---




---

## 🚀 Usage

```bash
python main.py
```

- Point your camera at a face
- The face region will appear blurred in the live window
- Press **`q`** to quit

---


---

## 👨‍💻 Author

**Ashutosh Tare** — Aspiring ML Engineer | Data Science Enthusiast
