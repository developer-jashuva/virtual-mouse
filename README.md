# 🖱️ Virtual Mouse using Hand Gestures

Control your computer mouse using your hands — no touch or device required!

This Python project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to track your hand in real-time using your webcam and control the mouse pointer through intuitive gestures like finger movement and pinches.

---

## 🚀 Features

- 🖐️ Move your mouse by moving your index finger in the air.
- 👆 Left click when thumb and index finger touch.
- 👉 Right click when thumb and middle finger touch.
- 🔒 Touchless control — great for accessibility and fun demos.
- 🖼️ Live webcam feed with hand landmark overlay.

---

## 🛠️ Tech Stack

- Python 🐍
- OpenCV 🎥 – For webcam feed and image processing
- MediaPipe 🤖 – For real-time hand landmark detection
- PyAutoGUI 🖱️ – For controlling the actual mouse

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/virtual-mouse.git
cd virtual-mouse
pip install -r requirements.txt

## ▶️ How to Run

python virtual_mouse.py

-Press Q to quit

-Make sure your camera has good lighting and your hand is visible

## 📷 Demo

You can include a short demo video or animated GIF too.

## 📁 File Structure

virtual-mouse/
├── virtual_mouse.py           # Main Python script
├── requirements.txt           # Required packages
├── README.md                  # Project documentation
├── assets/                    # Screenshots or demo media
└── .gitignore                 # (Optional) Python ignores


⚙️ How It Works
1.OpenCV captures live video feed from your webcam.

2.MediaPipe detects hand landmarks (like finger tips).

3.Index finger tip coordinates are mapped to your screen resolution.

4.PyAutoGUI moves the mouse to that position.

5.Gestures like thumb-index touch trigger mouse clicks.


## 💡 Use Cases
• Assistive technology for users with limited mobility

• Touchless interaction in labs or hospitals

• Interactive kiosks or smart mirrors

• Gesture-controlled presentations

## 🔮 Future Enhancements
• 📜 Gesture-based scrolling

• 🖌️ Drawing mode (air sketch)

• 🎤 Voice + gesture combo

• 🌐 Streamlit or Tkinter GUI for toggling features

• 📱 Android version with OpenCV mobile

## 🚀 Deployment
• This project is currently designed to run as a Python desktop script.
• To deploy as an app:

• Use PyInstaller to build a .exe

• Or turn it into a Streamlit-based browser UI

• You could even build a kiosk mode with auto-start

## 📬 Contact
Sri jashuva
GitHub: @developer-jashuva
Email: jashuva@example.com 
LinkedIn: https://linkedin.com/sri-jashuva


---

✅ Let me know if you'd like:
- A **starter GitHub repo template**
- To move to **Step 2: building `virtual_mouse.py`**
- A **Streamlit version** instead of a desktop app

You're set for a professional GitHub-ready project!


