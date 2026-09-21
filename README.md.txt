# AquaSense AI

## An AI-Powered Water-Loss Intelligence and Intervention System for Sustainable Water Management

AquaSense AI is a prototype designed to help campuses and communities manage water-loss incidents more intelligently. It converts natural-language water-loss reports into structured information, analyzes the available evidence, identifies recurring problem locations, prioritizes incidents, and recommends suitable intervention actions.

## Problem

Water-loss incidents are often reported as simple complaints, making it difficult for maintenance teams to understand which problems need attention first. Repeated incidents at the same locations may also go unnoticed when each complaint is handled separately.

## Solution

AquaSense AI provides four main intelligence functions:

- **Incident Intelligence** – understands natural-language water-loss reports.
- **Intervention Intelligence** – assigns a transparent priority level and recommends actions.
- **Historical Pattern Intelligence** – uses previous incidents to identify recurring locations.
- **Hotspot Intelligence** – highlights locations that require closer attention.

## AI Technology

The project uses **IBM Granite (Granite-4.0-H-Small)** through **IBM watsonx.ai** for natural-language incident understanding and information extraction.

The priority score is calculated using a transparent scoring engine based on available evidence such as:

- Severity
- Duration
- People affected
- Continuity
- Previous incidents

Missing information is not invented by the AI and is treated as unknown.

## Prototype

The prototype is developed using:

- Python
- Streamlit
- Pandas
- IBM watsonx.ai
- IBM Granite
- Excel-based incident data

## Dataset

The current prototype uses a **simulated dataset of 50 water-loss incidents** representing different locations, incident types, durations, impacts, continuity, and previous incidents.

The dataset is intended for prototype demonstration and is not claimed to represent measured real-world water consumption or actual water-loss quantities.

## Workflow

**Water-Loss Report → IBM Granite → Historical Check → Priority Scoring → Hotspot Detection → Recommended Intervention**

## Sustainability

AquaSense AI supports **UN Sustainable Development Goal 6 (Clean Water and Sanitation)** by promoting data-driven management of water-loss incidents and encouraging timely intervention and preventive maintenance.

## Future Scope

The system can be extended in the future by connecting it with real campus data, water-flow sensors, maintenance systems, and a trusted knowledge base for water-management guidance.

## Important Note

The IBM Cloud API key should be entered at runtime and must never be stored in the source code or uploaded to GitHub.