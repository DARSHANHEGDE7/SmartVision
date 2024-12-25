🚀 SmartVision
Real-Time Monitoring and Detection of Suspicious Human Activity Using Deep Learning
📌 Abstract
SmartVision is an AI-powered security system designed to monitor and detect suspicious human activities in real-time. Using advanced Deep Learning and Computer Vision techniques, the system analyzes surveillance footage to identify:

Complex human behaviors
Threats
Aggressive actions
By integrating technologies like SlowFast for activity classification, YOLOv5 for real-time threat detection, and MediaPipe for pose estimation, SmartVision delivers a robust and efficient solution for both public and private space security.

🔍 Features
✅ Real-Time Suspicious Activity Detection

Identifies complex human behaviors using SlowFast.
🛡 Threat Detection

Detects high-risk scenarios like weapons, accidents, and explosions using YOLOv5.
💪 Pose Estimation

Leverages MediaPipe to detect physical confrontations or aggressive movements.
📊 Activity Classification

Differentiates between typical and suspicious activities with ResNet50.
📢 Real-Time Alerts

Sends instant notifications to authorities when a potential threat is detected.
⚙ Technologies Used
🧠 Deep Learning
SlowFast: For activity classification from slow and fast video frames.
ResNet50: Recognizes activity patterns to differentiate normal and suspicious behavior.
YOLOv5: Detects high-risk threats in real-time.
👁 Computer Vision
OpenCV: Video processing and feature extraction.
MediaPipe: Human pose estimation to identify aggressive actions.
🛠 Libraries/Tools
Python
TensorFlow
PyTorch
OpenCV
MediaPipe

🏗 System Architecture
Below is the architecture powering SmartVision's real-time suspicious activity detection.

Data Input

Video input is taken from surveillance cameras.
Processing

SlowFast and ResNet50 analyze video streams to detect human activities.
Threat Detection

YOLOv5 scans for high-risk threats such as weapons, accidents, and explosions.
Pose Estimation

MediaPipe detects aggressive body movements like fights or confrontations.
Alert System

Immediate notifications are sent to authorities if any threat is detected.
