# Captide API Case Studies & Example Notebooks

Welcome to the **Captide API Examples** repository! This collection of Jupyter notebooks demonstrates practical applications of the Captide API, focusing on the processing of unstructured financial information from global financial reports.

## Overview

[Captide](www.captide.co) is redefining how financial institutions build AI capabilities with a full-stack platform that integrates LLM-ready financial reports and advanced agentic AI systems for deep analytical reasoning. At its core is a curated library of financial disclosures from over 14,000 public companies, preprocessed and structured for optimal use with large language models. On top of this, Captide has built domain-specific AI agents that read, interpret, and reason over this data—augmenting a wide range of high-value tasks, from investment research to equity modeling.

Here are five major use cases where Captide’s API can add value:
- **Custom Investment Tools**: Integrate real-time querying of financial documents and AI-generated insights into research platforms, dashboards, or client-facing apps.
- **Dynamic Equity Research Models**: Automate model updates by extracting both structured data and unstructured commentary from filings, providing deeper context behind the numbers.
- **Automated Fundamental Analysis**: Convert raw filings into clean data or summaries to auto-generate reports, update key fundamentals, and trigger metric-based alerts.
- **Data Mining at Scale**: Extract financial metrics, disclosures, commentary, and custom analytics from unstructured documents to build a research-ready data layer.
- **Real-Time Event Tracking**: Monitor changes in filings—like executive shifts, M&A activity, or guidance updates—and set automated alerts to drive event-based strategies.

These notebooks serve as educational resources for developers, data analysts, and financial professionals interested in leveraging the Captide API for various use cases.

## Repository Structure

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