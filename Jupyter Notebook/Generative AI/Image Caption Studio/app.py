import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import requests
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Image Caption Studio",
    page_icon="🖼️",
    layout="wide"
)

# ---------------- CONFIGURATION ----------------
TRACKER_URL = "https://image-caption-studio-url-tracker.onrender.com"  # ← YOUR TRACKER URL HERE

# ---------------- CSS (EXACT ORIGINAL - UNCHANGED) ----------------
st.markdown("""
<style>
body { background:#0e1117; }

.header { text-align:center; margin:30px 0 40px; }
.header h1 { font-size:42px; font-weight:800; margin:0; }
.header p { color:#aaa; margin-top:8px; }

.panel {
  background:#161b22;
  padding:24px;
  border-radius:16px;
}

/* Container with fixed dimensions */
.image-box-container {
  width: 100%;
  height: 450px;
  border: 2px dashed #30363d;
  border-radius: 16px;
  margin-bottom: 12px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #161b22;
}

/* For placeholder */
.image-placeholder {
  color: #888;
  font-size: 18px;
}

/* THE SOLUTION: STRETCH TO FILL */
.image-box-container img {
  width: 100% !important;
  height: 100% !important;
  object-fit: fill !important;
}

/* Generate button in right panel */
.generate-button-container {
  margin-top: 30px;
  width: 100%;
}

.generate-button-container button {
  background: linear-gradient(90deg,#6366f1,#06b6d4) !important;
  color:#fff !important;
  font-size:18px !important;
  font-weight:700 !important;
  padding:12px 36px !important;
  border-radius:16px !important;
  border:none !important;
  cursor:pointer !important;
  width: 100% !important;
}

/* OUTPUT SECTION - NEW STYLING */
.output-section {
  margin-top: 40px;
  width: 100%;
}

.output-title {
  text-align: center;
  color: #fff;
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 30px;
  padding-bottom: 15px;
  border-bottom: 2px solid #30363d;
}

/* Beautiful Output Cards */
.output-card {
  background: linear-gradient(145deg, #161b22, #1c2129);
  padding: 28px;
  border-radius: 18px;
  margin-bottom: 25px;
  border-left: 5px solid #6366f1;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.output-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.4);
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 1px solid #30363d;
}

.card-icon {
  font-size: 24px;
  margin-right: 15px;
}

.card-title {
  font-size: 22px;
  font-weight: 700;
  color: #fff;
  margin: 0;
}

.card-content {
  font-size: 16px;
  line-height: 1.6;
  color: #c9d1d9;
  padding: 10px 0;
}

/* Different card colors based on type */
.card-short {
  border-left-color: #06b6d4;
}

.card-short .card-icon {
  color: #06b6d4;
}

.card-technical {
  border-left-color: #10b981;
}

.card-technical .card-icon {
  color: #10b981;
}

.card-friendly {
  border-left-color: #f59e0b;
}

.card-friendly .card-icon {
  color: #f59e0b;
}

/* Empty state for output */
.empty-output {
  text-align: center;
  color: #666;
  font-size: 16px;
  padding: 40px;
  background: #161b22;
  border-radius: 16px;
  border: 2px dashed #30363d;
}

.footer {
  text-align:center;
  color:#777;
  font-size:14px;
  margin-top:80px;
  padding:20px;
  border-top:1px solid #30363d;
}

/* New styles for auto-find system */
.status-connected { 
  color: #10b981; 
  font-weight: bold;
}
.status-disconnected { 
  color: #ef4444; 
  font-weight: bold;
}
.backend-url {
  background: #1e293b;
  padding: 10px;
  border-radius: 8px;
  font-family: monospace;
  font-size: 12px;
  word-break: break-all;
  margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER (EXACT ORIGINAL - UNCHANGED) ----------------
st.markdown("""
<div class="header">
  <h1>🖼️ Image Caption Studio</h1>
  <p>Upload an image and generate Short, Technical, or Human-friendly captions using Generative AI.</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state at the VERY BEGINNING
if 'initialized' not in st.session_state:
    st.session_state.uploaded_image = None
    st.session_state.image_html = None
    st.session_state.captions_generated = False
    st.session_state.current_style = "All"
    st.session_state.generated_captions = {}
    st.session_state.backend_url = None
    st.session_state.backend_status = "checking"
    st.session_state.backend_info = {}
    st.session_state.initialized = True

# ---------------- HELPER FUNCTIONS ----------------
def get_backend_from_tracker():
    """Ask tracker service for current Colab URL"""
    try:
        response = requests.get(f"{TRACKER_URL}/url", timeout=25)
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success') and data.get('backend', {}).get('url'):
                backend_info = data['backend']
                st.session_state.backend_url = backend_info['url']
                st.session_state.backend_info = backend_info
                st.session_state.backend_status = "connected"
                return True
            else:
                st.session_state.backend_status = "disconnected"
                return False
        else:
            st.session_state.backend_status = "tracker_error"
            return False
            
    except Exception as e:
        st.session_state.backend_status = "error"
        return False

def test_backend_connection(url):
    """Test if the backend is responding"""
    try:
        response = requests.get(f"{url}/health", timeout=25)
        return response.status_code == 200
    except:
        return False

def generate_captions_from_api(image: Image.Image, styles: list, word_limits: dict) -> dict:
    """Call API with ORIGINAL PIL Image"""
    if not st.session_state.backend_url:
        return {'success': False, 'error': 'No backend URL found'}
    
    try:
        # Convert ORIGINAL image to base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Prepare payload with dynamic word limits
        payload = {
            "image": img_str,
            "styles": styles,
            "word_limits": word_limits
        }
        
        # Make API request
        response = requests.post(
            f"{st.session_state.backend_url}/generate-captions",
            json=payload,
            timeout=None
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {'success': False, 'error': f"API error {response.status_code}"}
            
    except requests.exceptions.Timeout:
        return {'success': False, 'error': "Timeout - please wait and try again"}
    except Exception as e:
        return {'success': False, 'error': str(e)}

# ---------------- SIDEBAR: AUTO-FIND BACKEND (NEW) ----------------
with st.sidebar:
    st.markdown("### 📡 Backend Status")
    st.markdown("---")
    
    # Auto-find button
    if st.button("🔍 Find Colab Backend", type="secondary", use_container_width=True):
        with st.spinner("Looking for Colab GPU backend..."):
            if get_backend_from_tracker():
                if test_backend_connection(st.session_state.backend_url):
                    st.success("✅ Connected to Colab GPU!")
                else:
                    st.warning("⚠️ Found backend but it's not responding")
            else:
                st.error("❌ No active backend found")
    
    # Display current status
    st.markdown("---")
    st.markdown("**Current Status:**")
    
    if st.session_state.backend_status == "connected":
        st.markdown('<p class="status-connected">🟢 Connected</p>', unsafe_allow_html=True)
        
        # Show backend info
        backend_info = st.session_state.backend_info
        if backend_info.get('last_updated'):
            from datetime import datetime
            last_update = datetime.fromisoformat(backend_info['last_updated'].replace('Z', '+00:00'))
            now = datetime.now()
            hours_ago = int((now - last_update).total_seconds() / 3600)
            
            st.markdown(f"**Last seen:** {hours_ago} hour{'s' if hours_ago != 1 else ''} ago")
        
        if backend_info.get('model'):
            st.markdown(f"**Model:** {backend_info['model']}")
        
        # Show URL (hidden by default)
        with st.expander("Show Backend URL"):
            st.code(st.session_state.backend_url, language="text")
    
    elif st.session_state.backend_status == "disconnected":
        st.markdown('<p class="status-disconnected">🔴 Disconnected</p>', unsafe_allow_html=True)
        st.info("No active Colab backend found. Start your Colab notebook first.")
    
    else:
        st.markdown('<p class="status-disconnected">⚪ Not checked</p>', unsafe_allow_html=True)
        st.info("Click 'Find Colab Backend' to connect")
    
    # Manual override (hidden by default)
    with st.expander("Manual URL (Advanced)"):
        manual_url = st.text_input(
            "Enter Colab URL manually:",
            value=st.session_state.backend_url or "",
            placeholder="https://xxxx.ngrok-free.app"
        )
        if st.button("Use Manual URL", type="secondary"):
            if manual_url and manual_url.startswith("http"):
                st.session_state.backend_url = manual_url.rstrip('/')
                st.session_state.backend_status = "manual"
                st.rerun()
    
    st.markdown("---")
    st.markdown("**How it works:**")
    st.markdown("1. Start Colab notebook (runs GPU model)")
    st.markdown("2. Click 'Find Colab Backend'")
    st.markdown("3. Upload image & generate captions")
    st.markdown("4. Colab runs for ~12 hours automatically")

# ---------------- LAYOUT (EXACT ORIGINAL - UNCHANGED) ----------------
left, right = st.columns(2, gap="large")

# ---------------- LEFT: IMAGE (EXACT ORIGINAL - UNCHANGED) ----------------
with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("<h3>Upload Image</h3>", unsafe_allow_html=True)
    
    # FIRST: Display image or placeholder
    if st.session_state.image_html:
        st.markdown(st.session_state.image_html, unsafe_allow_html=True)
    else:
        st.markdown('<div class="image-box-container"><div class="image-placeholder">📷 No image selected</div></div>', unsafe_allow_html=True)
    
    # SECOND: Handle file uploader
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["png", "jpg", "jpeg"],
        label_visibility="collapsed",
        help="Click to upload an image"
    )
    
    # Process uploaded file IMMEDIATELY
    if uploaded_file is not None:
        if 'last_uploaded_file' not in st.session_state or st.session_state.last_uploaded_file != uploaded_file.name:
            try:
                # Open and process the image
                image = Image.open(uploaded_file)
                
                # IMPORTANT: Store ORIGINAL image for API (not resized)
                st.session_state.uploaded_image = image
                
                # Get image dimensions
                original_width, original_height = image.size
                
                # Resize ONLY for display
                container_width = 600
                container_height = 450
                
                resized_image = image.resize((container_width, container_height), Image.Resampling.LANCZOS)
                
                # Convert to base64 for HTML embedding
                buffered = BytesIO()
                resized_image.save(buffered, format="PNG", optimize=True, quality=95)
                img_str = base64.b64encode(buffered.getvalue()).decode()
                
                # Create HTML with image embedded inside the box
                image_html = f'''
                <div class="image-box-container">
                    <img src="data:image/png;base64,{img_str}" alt="Uploaded Image" />
                </div>
                '''
                
                # Save to session state
                st.session_state.image_html = image_html
                st.session_state.last_uploaded_file = uploaded_file.name
                st.session_state.captions_generated = False
                st.session_state.generated_captions = {}
                
                st.rerun()
                
            except Exception as e:
                st.error(f"Error loading image: {e}")
                st.session_state.uploaded_image = None
                st.session_state.image_html = None
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RIGHT: OPTIONS (EXACT ORIGINAL - UNCHANGED) ----------------
with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("<h3>Caption Style</h3>", unsafe_allow_html=True)
    
    style = st.radio(" ", ["All", "Short", "Technical", "Human-friendly"], 
                     label_visibility="collapsed")
    
    with st.expander("Advanced Options", expanded=True):
        short_words = st.slider("Short caption words", 5, 30, 15)
        tech_words = st.slider("Technical caption words", 10, 60, 35)
        human_words = st.slider("Human-friendly caption words", 10, 50, 25)
    
    # GENERATE BUTTON IN RIGHT PANEL
    st.markdown('<div class="generate-button-container">', unsafe_allow_html=True)
    generate_clicked = st.button("Generate Captions", type="primary", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Handle generate button click
if generate_clicked:
    if st.session_state.backend_status != "connected":
        st.error("❌ Please connect to backend first (click 'Find Colab Backend' in sidebar)")
    elif not st.session_state.get("uploaded_image"):
        st.warning("⚠️ Please upload an image first!")
    else:
        # Prepare parameters with DYNAMIC word limits
        if style == "All":
            styles = ["all"]
        else:
            style_map = {
                "Short": "short",
                "Technical": "technical",
                "Human-friendly": "human-friendly"
            }
            styles = [style_map[style]]
        
        # Dynamic word limits from user sliders
        word_limits = {
            "short": short_words,
            "technical": tech_words,
            "human-friendly": human_words
        }
        
        # Show loading
        with st.spinner("🔄 Generating captions with your settings... Please wait 30-60 seconds..."):
            # Call API with ORIGINAL image and DYNAMIC word limits
            result = generate_captions_from_api(
                st.session_state.uploaded_image,
                styles,
                word_limits
            )
            
            if result.get('success'):
                st.session_state.captions_generated = True
                st.session_state.current_style = style
                st.session_state.generated_captions = result.get('captions', {})
                st.rerun()
            else:
                error_msg = result.get('error', 'Unknown error')
                st.error(f"❌ Error: {error_msg}")
                
                # Helpful suggestions
                if "Timeout" in error_msg:
                    st.info("💡 The Colab backend might be starting up. Try again in 60 seconds.")
                elif "Connection" in error_msg or "refused" in error_msg:
                    st.info("💡 The Colab backend may have disconnected. Click 'Find Colab Backend' again.")

# ---------------- OUTPUT SECTION (EXACT ORIGINAL - UNCHANGED) ----------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="output-section">', unsafe_allow_html=True)

# Display captions if they should be shown
if st.session_state.get("captions_generated", False) and st.session_state.generated_captions:
    # Caption data
    caption_display = {
        "short": {
            "icon": "⚡",
            "title": "Short Caption",
            "class": "card-short"
        },
        "technical": {
            "icon": "🔬",
            "title": "Technical Caption",
            "class": "card-technical"
        },
        "human-friendly": {
            "icon": "😊",
            "title": "Human-friendly Caption",
            "class": "card-friendly"
        }
    }
    
    # Display title
    st.markdown('<div class="output-title">✨ Generated Captions</div>', unsafe_allow_html=True)
    
    # FIXED ORDER: Display in correct order - Short, Technical, Human-friendly
    caption_order = ["short", "technical", "human-friendly"]
    
    for caption_type in caption_order:
        if caption_type in st.session_state.generated_captions:
            caption_data = st.session_state.generated_captions[caption_type]
            card_info = caption_display[caption_type]
            caption_text = caption_data.get('caption', '')
            
            st.markdown(f"""
            <div class="output-card {card_info['class']}">
                <div class="card-header">
                    <span class="card-icon">{card_info['icon']}</span>
                    <h3 class="card-title">{card_info['title']}</h3>
                </div>
                <div class="card-content">
                    {caption_text}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Add a refresh/regenerate option
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Generate New Captions", type="secondary", use_container_width=True):
            st.session_state.captions_generated = False
            st.session_state.generated_captions = {}
            st.rerun()

elif st.session_state.get("uploaded_image"):
    # Image uploaded but no captions generated yet
    st.markdown('<div class="empty-output">📷 Upload an image and click "Generate Captions" to see results here.</div>', unsafe_allow_html=True)
else:
    # No image uploaded at all
    st.markdown('<div class="empty-output">📷 Upload an image and click "Generate Captions" to see results here.</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER (EXACT ORIGINAL - UNCHANGED) ----------------
st.markdown("""
<div class="footer">
    Built for academic & demonstration purposes • Uses Qwen2.5-VL-7B-Instruct
</div>
""", unsafe_allow_html=True)

# Auto-check backend on load
if st.session_state.backend_status == "checking":
    with st.spinner("Checking for backend..."):
        if get_backend_from_tracker():
            if test_backend_connection(st.session_state.backend_url):
                st.session_state.backend_status = "connected"
            else:
                st.session_state.backend_status = "disconnected"
        else:
            st.session_state.backend_status = "disconnected"
