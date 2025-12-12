# Credit-Risk-Probability-Model-for-Alternative-Data-Week-4-Challenge-




## Credit Scoring Business Understanding

Short summary (purpose):

We will build a model to predict whether a transaction (or customer) is likely to result in credit loss or an event representative of credit risk. This helps the business manage exposure, set limits, and meet regulatory expectations for model governance.

How Basel II’s emphasis on risk measurement influences our need for an interpretable, well-documented model

Basel II requires banks and financial firms to measure and manage credit risk with robust methodologies and to hold capital proportional to measured risk. Regulators expect sound model governance, documentation, and the ability to explain decisions (why a borrower is risky) for audit and stress testing.

Impact on modeling choices: prioritize explainability, stability, and evidence-based features. Use interpretable approaches (e.g., logistic regression with WoE bins) for baseline models and ensure complex models include explainability tools (SHAP, partial dependence) and extensive documentation.

Since we lack a direct “default” label — why create a proxy and risks of using it

Why a proxy is necessary: If no explicit default flag is provided, we must design a proxy target that captures credit loss or default-like events (e.g., sustained negative balances, chargebacks, seizure events, bounced transactions, or repeated failed payments). Without a proxy we cannot train supervised models.

Example proxy definitions:

proxy_default = 1 if customer has n or more chargebacks/refunds in 90 days OR cumulative negative Value above threshold.

proxy_default = 1 if transaction marked IsVATRegistered=False and refunds > X and last payment failed.

If transactions have FraudResult you could create proxies combining fraud + large refunds as “high credit risk” for behavioral scoring.

Risks / biases when using proxy labels:

Label bias: The proxy may capture operational or fraud patterns rather than true credit default (introduces label noise).

Omitted population: Proxy may miss silent defaulters (e.g., those with low activity).

Temporal leakage: Using future information to label earlier records can leak and inflate model performance. Must label using only data available at prediction time.

Fairness/representation: Proxy may unfairly reflect socio-demographic differences (e.g., country or channel biases).

Trade-offs: Simple interpretable model vs complex high-performance model

Interpretable (e.g., Logistic Regression with WoE)

Pros: Easier to explain; regulatory-friendly; stable if features are well-binned; coefficients interpretable as log-odds.

Cons: May underperform on complex, non-linear interactions.

Complex (e.g., Gradient Boosting / XGBoost / LightGBM)

Pros: Usually higher predictive performance on structured data; handles interactions automatically.

Cons: Harder to explain (mitigate with SHAP); risk of overfitting; need heavier model governance and monitoring.

Recommended approach for a regulated context: Start with a well-documented interpretable model as baseline. If you move to a complex model, provide:

a business-case justification (performance lift vs operational cost),

detailed feature documentation,

local and global explainability artifacts (SHAP summaries, PDPs),

stability and fairness analysis, and

a fallback interpretable model for high-impact decisions.