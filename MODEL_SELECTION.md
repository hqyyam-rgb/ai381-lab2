# Model selection

## The question
The model predicts the probability that a customer will leave the service (churn). A wrong prediction may cause the business to miss a customer who needs retention support or waste resources contacting a customer who would have stayed.

## Candidates

| Candidate | Why I tried it | AUC | F1 | F1 per slice (lowest) | p95 latency (ms) | Size (KB) | MLflow run ID |
|---|---|---:|---:|---:|---:|---:|---|
| Logistic Regression | Simple, fast, and easy to interpret | 0.7982 | 0.4948 | 0.2500 | 4.1682 | 3.5479 | fd634d456f3143fbaee6860f777f2afb |
| Random Forest | Tests a tree-based ensemble model | 0.7589 | 0.4536 | 0.2222 | 17.4098 | 3160.0957 | aadc1608227d465cbea538120683dda2 |
| Gradient Boosting | Tests a boosting-based ensemble model | 0.7476 | 0.4167 | 0.2222 | 4.5758 | 141.6445 | e6ecaa75b1e346e8bee342a4c0ca5815 |

## The champion
I selected Logistic Regression as the champion. It achieved the highest AUC (0.7982) and F1 (0.4948), while staying well below the 25 ms latency budget. It also had the smallest model size (3.55 KB). I accepted that its lowest contract-slice F1 was only 0.2500, so performance on smaller contract groups needs further investigation.

## My promotion rules
- Latency budget (p95): 25 ms, because predictions should be returned quickly by the API.
- Minimum gain to replace the champion (F1 points): 0.005, to avoid replacing the champion for a negligible improvement.

## What I would check next
I would check the number of customers in each contract slice and monitor slice-level performance over time. A small group or changing customer behavior could make the current results less reliable in production.
