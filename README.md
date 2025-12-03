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

- **Title**: "When Cats Get Brainrot #Shorts #Cats #Brainrot #Meme"
- **Script**: "Cats are adorable, but sometimes they just lose it! Watch as my cat gets distracted by… nothing! Pure chaos!
- **Hashtags**: #catbrainrot #funnycats #catantics #petproblems #catvideos #felinefunnies #catsofinstagram #adorablecats #crazycats #catlovers #petlovers #animalantics #catsareweird #caturday #comediccats"
- **Video**: [YouTube Shorts](https://www.youtube.com/shorts/9B1SFZwuwRo)

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
