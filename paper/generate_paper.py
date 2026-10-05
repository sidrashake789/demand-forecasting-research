"""Generate a summary PDF report of the research paper using fpdf2."""

from pathlib import Path
from fpdf import FPDF

ROOT = Path(__file__).resolve().parent
PDF_OUTPUT = ROOT / "paper_summary.pdf"

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 12)
        self.cell(0, 10, 'A Hybrid Framework for Demand Forecasting - Summary', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title & Author Info
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(0, 10, 'A Hybrid Framework for Demand Forecasting', 0, 1, 'L')
    pdf.set_font('helvetica', 'I', 11)
    pdf.cell(0, 8, 'Sidra Shaikh | Department of Management Information Systems | University of Houston', 0, 1, 'L')
    pdf.ln(5)
    
    # Abstract
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 8, 'Abstract', 0, 1, 'L')
    pdf.set_font('helvetica', '', 10)
    abstract_text = (
        "Predicting retail demand accurately is a major challenge for supply chain planning. "
        "Traditional forecasting tools usually look only at past sales and pricing numbers, which means "
        "they tend to struggle when sudden real-world shifts happen, such as bad weather or public health crises. "
        "In this project, I built a hybrid demand forecasting framework that combines historical sales data with "
        "external context scores for weather and epidemic conditions. Using a Random Forest regressor trained on "
        "76,000 transaction records, I compared a standard baseline model against my context-aware hybrid model. "
        "The results show that the baseline model produced a Mean Absolute Percentage Error (MAPE) of 43.51%, "
        "while the hybrid model lowered that error to 39.37%, achieving a 4.14 percentage point improvement."
    )
    pdf.multi_cell(0, 6, abstract_text)
    pdf.ln(5)
    
    # Key Results Table / Summary
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 8, 'Performance Comparison', 0, 1, 'L')
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 6, "• Baseline Model MAPE: 43.51% (Features: Inventory Level, Units Ordered, Price, Discount, Competitor Pricing)")
    pdf.multi_cell(0, 6, "• Hybrid Model MAPE: 39.37% (Features: Inventory Level, Units Ordered, Price, Weather_Score, Epidemic_Score)")
    pdf.multi_cell(0, 6, "• Error Reduction: 4.14 absolute percentage points (9.5% relative decrease).")
    pdf.ln(5)
    
    # Methodology Notes
    pdf.set_font('helvetica', 'B', 12)
    pdf.cell(0, 8, 'Methodology Highlights', 0, 1, 'L')
    pdf.set_font('helvetica', '', 10)
    pdf.multi_cell(0, 6, "- Model Architecture: Random Forest Regressor (n_estimators=100, random_state=42).")
    pdf.multi_cell(0, 6, "- Evaluation Metric: Modified MAPE with epsilon smoothing (epsilon = 1.0) to handle zero-sales rows cleanly.")
    pdf.multi_cell(0, 6, "- Train/Test Split: 80/20 partition (60,800 training rows and 15,200 testing rows).")
    
    pdf.output(str(PDF_OUTPUT))
    print(f"PDF summary successfully generated at: {PDF_OUTPUT}")

if __name__ == '__main__':
    generate_pdf()