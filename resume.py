# ===============================
# 💼 Local Resume Bullet Generator (SmolLM 1.7B)
# ===============================

# 1) Install dependencies
!pip -q install streamlit torch transformers accelerate sentencepiece > /dev/null

# 2) Write the Streamlit app
app_code = r"""
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

st.set_page_config(page_title="Local Resume Bullet Generator", page_icon="💼")
st.title("💼 Local Resume Bullet Point Generator (SmolLM 1.7B)")
st.markdown(
    "Enter a **description of your role or goal** and your **skills**. A lightweight local model (SmolLM) will generate tailored, action-oriented resume bullets—no internet or API needed!"
)

# ---------------------------
# Load SmolLM (cached, CPU-friendly)
# ---------------------------
@st.cache_resource
def load_model():
    model_name = "HuggingFaceTB/SmolLM-1.7B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32,  # Stable on CPU
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        device_map="auto"
    )
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.float32,
        device_map="auto"
    )
    return pipe

generator = load_model()

# ---------------------------
# Helper: Generate response
# ---------------------------
def generate_text(prompt, max_new_tokens=250):
    # SmolLM uses standard chat format
    messages = [{"role": "user", "content": prompt}]
    output = generator(
        messages,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    return output[0]['generated_text'].strip()

# ---------------------------
# UI
# ---------------------------
st.subheader("📝 Your Professional Context")
context = st.text_area(
    "Describe the role, your experience, or your goal (1–2 sentences)",
    placeholder="I'm applying for a Data Analyst role focused on marketing analytics and customer segmentation."
)
skills = st.text_area("Your Key Skills (comma-separated)", placeholder="Python, SQL, Power BI, A/B testing, Google Analytics")
num_bullets = st.slider("Number of bullet points", 3, 6, 4)

if st.button("✨ Generate Bullet Points"):
    if not context.strip():
        st.warning("Please describe your professional context.")
    elif not skills.strip():
        st.warning("Please enter at least one skill.")
    else:
        with st.spinner("Generating bullets with SmolLM (should take 10–30s on CPU)..."):
            prompt = (
                f"Generate exactly {num_bullets} strong resume bullet points based on: \"{context}\". "
                f"Skills: {skills}. "
                "Rules:\n"
                "- Start each with a past-tense action verb (e.g., Analyzed, Built, Improved)\n"
                "- Include a clear result or impact\n"
                "- Keep each to one sentence\n"
                "Return ONLY a numbered list. No other text."
            )
            try:
                response = generate_text(prompt)
                st.success("✅ AI-Generated Resume Bullets:")
                st.text_area("Copy & paste into your resume:", response, height=200)
            except Exception as e:
                st.error(f"Generation failed: {str(e)}")
else:
    st.info("Fill in the form and click **Generate Bullet Points**.")
"""

# Save app
with open("resume_smollm.py", "w") as f:
    f.write(app_code)

# 3) Launch Streamlit
!pkill -f streamlit || true
!fuser -k 8501/tcp || true
!streamlit run resume_smollm.py --server.port=8501 --server.headless=true &>/dev/null&

# 4) Expose via Cloudflare Tunnel
import subprocess, time, re
!wget -q -O cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64  
!chmod +x cloudflared

proc = subprocess.Popen(
    ["./cloudflared", "tunnel", "--url", "http://localhost:8501", "--no-autoupdate"],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)

url = None
for _ in range(200):
    line = proc.stdout.readline()
    if "trycloudflare.com" in line:
        match = re.search(r"https://[a-zA-Z0-9-]+\.trycloudflare\.com", line)
        if match:
            url = match.group(0)
            break
    time.sleep(0.1)

print("\n🔗 Your Local Resume Bullet Generator is live at:")
print(url if url else "Still starting... check logs.")
