# Captide API Case Studies & Example Notebooks

Welcome to the **Captide API Examples** repository. This collection of Jupyter notebooks demonstrates practical applications of the Captide API, focusing on the processing of unstructured financial information from global financial reports.

## ℹ️ Overview

[Captide](www.captide.co) is redefining how financial institutions build AI capabilities with a full-stack platform that integrates LLM-ready financial reports and advanced agentic AI systems for deep analytical reasoning. At its core is a curated library of financial disclosures from over 14,000 public companies, preprocessed and structured for optimal use with large language models. On top of this, Captide has built domain-specific AI agents that read, interpret, and reason over this data—augmenting a wide range of high-value tasks, from investment research to equity modeling.

Essentially, Captide enables organisations to deploy multi-agent architectures, embed AI across their financial workflows, and distil insights from millions of corporate filings—all without the complexity of designing or maintaining RAG infrastructure. Here are five major use cases where Captide’s API can add value:
- **Custom Investment Tools**: Integrate real-time querying of financial documents and AI-generated insights into research platforms, dashboards, or client-facing apps.
- **Dynamic Equity Research Models**: Automate model updates by extracting both structured data and unstructured commentary from filings, providing deeper context behind the numbers.
- **Automated Fundamental Analysis**: Convert raw filings into clean data or summaries to auto-generate reports, update key fundamentals, and trigger metric-based alerts.
- **Data Mining at Scale**: Extract financial metrics, disclosures, commentary, and custom analytics from unstructured documents to build a research-ready data layer.
- **Real-Time Event Tracking**: Monitor changes in filings—like executive shifts, M&A activity, or guidance updates—and set automated alerts to drive event-based strategies.

These notebooks serve as educational resources for developers, data analysts, and financial professionals interested in leveraging the Captide API for various use cases.

## 🏁 Getting Started with the API


To access the API, please contact our sales team by filling out [form](https://www.captide.co/company/api-request) or by sending an email to [sales@captide.co](mailto:sales@captide.co). Once you get access to an API key. Once you receive your API key, you can explore detailed information about available endpoints in our [documentation](https://docs.captide.co).

Below is a quick guide to using the most popular endpoints:

### 1. Agentic RAG with citations

Calls Captide's AI agents and returns cited answers sourced exclusively from content within SEC filings and earnings calls.

```
headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = json.dumps({
    "query": "Summarize Snapchat's convertible debt balance"
})

response = requests.post(
    "https://rest-api.captide.co/api/v1/rag/agent-query-stream",
    headers=headers,
    data=payload
)
```

The responses are sent as Server-Sent Events (SSE) and include:
1. `full_answer`: Synthesized response.

2. `markdown_chunks`: Segmented answer for streaming.

3. `id_mapping`: Links each part of the answer to its source.

4. `done`: Indicates completion of the response generation.


### 2. Agentic chunk retrieval

Retrieves highly relevant document excerpts from corporate filings and earnings calls based on your queries.

```
headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = json.dumps({
    "query": "What are the key risks mentioned in the latest 10-K of Apple?"
})

response = requests.post(
    "https://rest-api.captide.co/api/v1/rag/chunks",
    headers=headers,
    data=payload
)
```

The response includes:
1. `text`: Plain-text excerpt.

2. `text_with_ids`: Markdown with inline formatting and annotations.

3. `metadata`: Filing type, date, ticker symbol, etc.

4. `source_link`: Direct link to the full source document.


## 🧬 Repository Structure

```
captide-api-examples/
├── notebooks/
│   ├── net_income_to_adjusted_ebitda.ipynb
│   ├── multi_company_comparison.ipynb
│   └── api_usage_basics.ipynb
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

- `notebooks/`: Contains Jupyter notebooks with different case studies.
- `.env.example`: Template for environment variables, including the API key.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `requirements.txt`: Lists Python dependencies required to run the notebooks.

## 🤝 Contributing
Contributions are welcome! If you have a use case or example you'd like to share:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature-name.
3. Add your notebook to the notebooks/ directory.
4. Commit your changes: git commit -m 'Add new case study notebook'.
5. Push to your fork: git push origin feature/your-feature-name.
6. Submit a pull request.

Please ensure that any new notebooks adhere to the existing structure and include necessary documentation within the notebook itself.