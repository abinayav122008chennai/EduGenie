# EduGenie - AI Model Selection and Architecture
# Assigned to Abinaya V

MODELS = {
    "Gemini 1.5 Pro (via API)": {
        "used_for": "Q&A, summarization, quiz generation, learning paths",
        "benefits": "Advanced reasoning, structured outputs, and cloud inference"
    },
    "LaMini-Flan-T5-783M (local)": {
        "used_for": "Concept explanation",
        "benefits": "Instruction-tuned, lightweight, CPU-compatible"
    }
}

ARCHITECTURE = """
EduGenie/
├── main.py                  # FastAPI app
├── model_selection.py       # AI Models config
├── explanation_module.py    # Concept explanation using LaMini
├── quiz_module.py           # Quiz generation
├── summarization.py         # Summarization module
└── requirements.txt         # Dependencies
"""

def get_model_info(model_name):
    return MODELS.get(model_name, "Model not found")

def list_models():
    for name, details in MODELS.items():
        print(f"Model: {name}")
        print(f"  Used for: {details['used_for']}")
        print(f"  Benefits: {details['benefits']}\n")

if __name__ == "__main__":
    list_models()
    print(ARCHITECTURE)
