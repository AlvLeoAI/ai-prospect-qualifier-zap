# Extract AI response from ChatGPT
raw_response = input_data.get('ai_reply', '')

# Split into lines
lines = raw_response.strip().split('\n')

# Initialize output values
score = ""
insight = ""
next_step = ""

# Parse each line for Score, Insight, Next Step
for line in lines:
    lower = line.lower()
    if 'score' in lower:
        score = ''.join([char for char in line if char.isdigit()])
    elif 'insight' in lower:
        insight = line.split(':', 1)[-1].strip()
    elif 'next step' in lower:
        next_step = line.split(':', 1)[-1].strip()

# Format fallback if missing
if not score:
    score = "0"
if not insight:
    insight = "No insight returned"
if not next_step:
    next_step = "No next step provided"

# Output
output = {
    "ai_score": score,
    "ai_insight": insight,
    "next_step": next_step
}
