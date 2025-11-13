import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Load sample data (replace with your dataset later)
data = pd.read_csv("data/data.csv")

# Split into reference and current data
reference_data = data.sample(80, random_state=42)
current_data = data.sample(80, random_state=7)

# Create Evidently report for data drift
report = Report(metrics=[DataDriftPreset()])

# Run the report
report.run(reference_data=reference_data, current_data=current_data)

# Save to HTML
report.save_html("reports/data_drift_report.html")

print("✅ Data drift report generated successfully! Check reports/data_drift_report.html")
