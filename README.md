# Auto-Generated Shorts: AI Agent for YouTube Shorts

An AI-powered agent that automates the creation of YouTube Shorts.  
From a single seed idea → script → voice → video → upload.  
Built for small creators, businesses, and social media managers.

---

## Problem
Creating short-form content is time-consuming.  
This agent saves hours by automating:
- Scriptwriting
- Voiceover
- Video generation
- Upload to YouTube

---

## How It Works

| Step | Tool | Description |
|------|------|-------------|
| 1. Brainstorm | OpenAI GPT-4o-mini | Generates a short, viral script |
| 2. TTS | Fal.ai | Converts script to realistic voice |
| 3. Video | WaveSpeed (ByteDance) | Generates 9:16 silent video |
| 4. Merge | FFmpeg | Combines audio + video |
| 5. Upload | YouTube Data API v3 | Uploads final Shorts video |

---

## Example Output

- **Title**: "Cat Brainrot Explained 🧠🐱 #Shorts"
- **Script**: "Cats experience brainrot when they're hyper-stimulated or bored. Watch as they bounce off walls or stare into space."
- **Hashtags**: #catbrainrot #funnycats #shorts #catbehavior #viral
- **Video**: [YouTube Shorts](https://www.youtube.com/shorts/Q1-pJyYYE5U)

---

## Tech Stack

- **Platform**: Google Colab
- **Language**: Python
- **AI Models**: OpenAI GPT-4o-mini, Fal.ai TTS, WaveSpeed T2V
- ** APIs**: YouTube Data API v3
- **Tools**: FFmpeg, Tenacity, UUID, tempfile

---

##  Setup Instructions

### 1. Clone Repo
```bash
git clone https://github.com/emp5954/Auto-Generated-Shorts.git
