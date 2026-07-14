# AquaAI-2040

## Overview

AquaAI-2040 is a CrewAI-based multi-agent system that analyzes water management challenges in Saudi Arabia and generates AI-powered sustainability recommendations aligned with Saudi Vision 2030 and UN Sustainable Development Goal 6 (Clean Water and Sanitation).

## Features

* Water challenge analysis
* Climate risk prediction
* AI-based water management solutions
* Final sustainability report generation

## Technologies Used

* Python
* CrewAI
* Groq LLM
* LiteLLM
* python-dotenv

## Project Structure

* `agents.py` – AI agent definitions
* `tasks.py` – Task definitions
* `crew.py` – Crew configuration
* `main.py` – Runs the project

## How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Add your Groq API key to the `.env` file:

   ```
   GROQ_API_KEY=gsk-api-keyxxxxxxxxxxxxxxxxxxxxx
   ```

3. Run the project:

   ```bash
   python main.py
   ```

## Output

The system generates a sustainability report containing:

* Water management challenges
* Climate predictions
* AI-based solutions
* Strategic recommendations for Saudi Vision 2030
