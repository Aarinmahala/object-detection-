# Smart Object Detection System

This project implements a comprehensive object detection system using YOLOv5 with multiple versions offering increasing functionality.

## 🚀 Deployment Options

### Option 1: Vercel (Limited Functionality)
This version includes a serverless-compatible version that works on Vercel but has limitations:

**✅ What's Included:**
- Web dashboard and interface
- Statistics and data viewing
- User authentication
- Basic API endpoints

**❌ Limitations:**
- No real-time camera streaming (serverless limitation)
- No live object detection
- No camera management features
- Reduced functionality compared to full version

**Deploy to Vercel:**
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# For production
vercel --prod
```

### Option 2: Full Local Deployment (Recommended)
For full functionality including real-time camera streaming and object detection, run locally:

```bash
pip install -r requirements.txt
python web_interface.py
```

Access at: http://localhost:5000

## Versions

### 1. Basic Detection (`detect_objects.py`)
- Simple object detection using webcam
- Basic bounding boxes around detected objects
- Press 'q' to quit

### 2. Enhanced Detection (`enhanced_detection.py`)
- Color-coded confidence levels (green, yellow, red)
- Basic UI with on-screen controls
- Video recording capability
- Save individual frames

### 3. Tracking Detection (`tracking_detection.py`)
- Object counting and tracking
- Statistics logging
- Organized output folders
- Maximum object count tracking

### 4. Smart Detection (`smart_detection.py`)
- Motion detection capabilities
- Email notifications for detected objects
- Sound alerts
- Customizable alert settings

### 5. Web Interface (`web_interface.py`)
- Flask-based web interface
- Live video streaming to browser
- Real-time statistics display
- Responsive web UI
- Motion detection alerts in browser
- Snapshot capturing and viewing
- Web-based settings configuration
- Secure authentication system
- Statistics dashboard with visual analytics

## Setup and Installation

### Requirements
- Python 3.8+
- Web camera (built-in or USB)
- Internet connection (for model download)

### Installation
```
pip install -r requirements.txt
```

## Quick Start Guide

To run the latest version (Web Interface):
```
python web_interface.py
```
Then open your browser and navigate to: `http://localhost:5000`

## Detailed Instructions

### Running Different Versions

1. **Basic Detection**:
   ```
   python detect_objects.py
   ```

2. **Enhanced Detection**:
   ```
   python enhanced_detection.py
   ```

3. **Tracking Detection**:
   ```
   python tracking_detection.py
   ```

4. **Smart Detection**:
   ```
   python smart_detection.py
   ```

5. **Web Interface**:
   ```
   python web_interface.py
   ```

### Email Configuration

To use email notifications, edit the `email_config.py` file with your email settings:
- Set your email address
- Configure SMTP settings
- Adjust notification preferences

### Motion Detection Settings

Motion detection sensitivity can be adjusted in the `email_config.py` file:
- Higher values = less sensitive
- Lower values = more sensitive

## Notes
- First run may take a few minutes to download the YOLOv5 model
- For best performance, run on a machine with a dedicated GPU
- The web interface runs on port 5000 by default

## Features Guide

### Detection Zones
The system now supports zone-based detection for precise monitoring of specific areas:
1. **Define Custom Zones**: Draw rectangular zones directly on the camera feed 
2. **Zone-Specific Settings**: Configure each zone with custom object types to monitor
3. **Visual Indicators**: Zones are highlighted in the video feed with color coding for triggered zones
4. **Per-Zone Statistics**: Track detections specific to each defined zone
5. **Active/Inactive Toggle**: Easily enable or disable zones without deleting them
6. **Zone Management**: Add, remove, and modify zones through an intuitive interface

### Multiple Camera Support
The system now supports multiple cameras for comprehensive surveillance:
1. **Auto-detection**: The system automatically detects all available cameras connected to your computer
2. **Individual feeds**: View each camera feed independently or in a grid layout
3. **Camera-specific stats**: Filter statistics and reports by camera
4. **Add to grid**: Create customized multi-camera views to monitor different areas simultaneously
5. **Per-camera snapshots**: Take and organize snapshots from specific cameras

### IP Camera Integration
The system supports connecting to network IP cameras in addition to USB webcams:
1. **RTSP/HTTP Support**: Connect to IP cameras using RTSP, HTTP, or MJPEG stream URLs
2. **Camera Management**: Add, edit, and remove IP cameras through the dedicated Cameras page
3. **Connection Testing**: Test camera connections before adding them to ensure proper configuration
4. **Authentication**: Support for username/password authentication for secured camera streams
5. **Auto-reconnect**: The system will automatically try to reconnect if a camera connection is lost
6. **Status Monitoring**: Visual indicators show the connection status of each camera
7. **Mixed Camera Types**: Use both USB webcams and IP cameras simultaneously in the same interface

### Mobile Interface
The system now includes a dedicated mobile view optimized for smartphones and tablets:
1. **Touch-friendly Controls**: Large buttons and controls designed for touch interactions
2. **Responsive Layout**: Adapts to different screen sizes from small phones to tablets
3. **Streamlined UI**: Simplified interface focusing on essential monitoring functions
4. **Side Navigation**: Space-efficient menu that slides in from the side when needed
5. **Performance Optimized**: Lighter interface designed for mobile networks and devices
6. **Camera Switching**: Easy dropdown to switch between different camera feeds
7. **Real-time Alerts**: Mobile-optimized motion and object detection alerts

To use the mobile interface, simply navigate to `/mobile` in your browser or access the system from a mobile device which will automatically redirect to the mobile-optimized view.

### Using Snapshots
The web interface allows you to capture and review snapshots:
1. Click the "Take Snapshot" button on the main interface
2. View saved snapshots by clicking "Snapshots" in the navigation bar
3. You can download any snapshot from the snapshots page
4. All snapshots are automatically timestamped and saved in the "snapshots" folder

### Configuring Settings
The web interface includes a settings page for easy configuration:
1. Click "Settings" in the navigation bar
2. Adjust detection confidence threshold to balance between detection accuracy and false positives
3. Modify motion sensitivity based on your environment
4. Configure email notification settings for alerts
5. Select which objects should trigger notifications
6. All settings are automatically saved to the configuration file

### Authentication
The system includes secure authentication to protect access:
1. Default login credentials are admin/password
2. You can change credentials in the Settings page
3. All pages are protected and require login
4. The system uses secure hashing for password storage
5. Session management ensures secure access

### Statistics Dashboard
The dashboard provides visual analytics for detection data:
1. View object detection trends over time
2. See distribution of detected object types
3. Analyze hourly detection patterns
4. Filter statistics by different time periods (day/week/month/all time)
5. Track motion events and detection rates
6. Export detection and motion data as CSV files for further analysis
7. All detection data is stored in a local database for historical analysis

### Docker Support
You can run the application in a Docker container:

1. Build the Docker image:
```
docker build -t object-detection .
```

2. Run the container:
```
docker run -p 5000:5000 object-detection
```

3. Access the web interface at http://localhost:5000 

6. Security: Implemented user authentication, secure password hashing, and session management to protect access to the system.

7. Mobile Responsive Interface: Added a dedicated mobile view optimized for smartphones and tablets with touch-friendly controls, streamlined statistics, and an adaptive layout for monitoring cameras on the go.

8. Statistics Dashboard: Added data visualization with interactive charts showing detection patterns, object distribution, and hourly trends, with filters for different time periods. 