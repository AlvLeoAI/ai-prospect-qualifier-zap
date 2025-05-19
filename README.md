# AI Prospect Qualifier (Zapier + ChatGPT + Python)

This automation reads company and role information from a Google Sheet, sends it to ChatGPT to evaluate, and parses the response into:
- **AI Score** (1–5)
- **Insight** (why it’s a match or not)
- **Next Step** (what to do next)

## 💡 Stack:
- Zapier
- Google Sheets
- ChatGPT (gpt-3.5-turbo-instruct)
- Python (in Zapier Code Step)

## 🔁 Flow:
1. **Trigger:** New row in Google Sheets
2. **Filter:** If "AI Score" is blank
3. **Send Prompt:** Use ChatGPT to qualify the lead
4. **Python:** Parse the response
5. **Update Sheet:** Write back the Score, Insight, and Next Step

## 📂 Files
- `qualifier_parser.py` – Code step to extract and clean AI response
