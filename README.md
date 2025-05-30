# Captide API Case Studies & Example Notebooks

Welcome to the **Captide API Examples** repository! This collection of Jupyter notebooks demonstrates practical applications of the Captide API, focusing on financial data analysis and reconciliation processes.

## Overview

[Captide](www.captide.co) is an AI-powered financial modeling and company data API that allows users to query and extract intelligence from over 750,000 financial documents, including SEC filings and earnings call transcripts. By leveraging large language models (LLMs), Captide transforms unstructured data into structured insights, facilitating more efficient and accurate investment analysis.

Captide is designed for quants and developers who need to incorporate rich financial data and insights into their models and applications. Here are five major use cases where Captide’s financial disclosure intelligence API can add value:
- Building Custom Investment Tools: Developers can integrate Captide into internal research tools, stock analysis dashboards, or client-facing applications. The API enables real-time querying of financial documents, allowing users to access AI-generated insights or custom features on-demand.
- Creating Dynamic Equity Research Models: Traditional equity models often require manual data entry and analysis. Captide automates this by extracting both structured data (like financial metrics) and unstructured insights (such as management commentary) from disclosures. This automation allows for the creation of dynamic models that update with new filings and provide contextual understanding behind the numbers.‍‍
- Automating Fundamental Analysis: Instead of manually sifting through lengthy filings, Captide parses raw documents and returns clean data or summaries. This capability enables automatic generation of financial reports, database updates with key fundamentals, and alerts when specific metrics change—all through code.
- Data Mining: Captide unlocks the ability to mine financial documents at scale. You can set up automations to extract everything from financial metrics, disclosure notes, commentary, and custom analytics, turning unstructured documents into a research-ready data layer.
- Tracking Corporate Events in Real Time: Captide makes it easy to monitor key corporate events (such as executive turnover, guidance changes, M&A activity, or litigation disclosures) as they unfold—without manually watching press releases or combing through filings. By tracking changes in query responses across documents in real-time, you can set up automated alerting that triggers event-driven strategies or internal research efforts.

These notebooks serve as educational resources for developers, data analysts, and financial professionals interested in leveraging the Captide API for various use cases.

## Repository Structure
captide-api-examples/
├── notebooks/
│ ├── net_income_to_adjusted_ebitda.ipynb
│ ├── multi_company_comparison.ipynb
│ └── api_usage_basics.ipynb
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md


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