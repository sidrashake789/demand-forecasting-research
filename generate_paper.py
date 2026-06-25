from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'A Hybrid Framework for Demand Forecasting', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Times', 'B', 14)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Times', '', 12)
        self.multi_cell(0, 7, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Abstract
pdf.chapter_title("Abstract")
pdf.chapter_body("This paper presents a hybrid framework for demand forecasting, bridging the gap between traditional statistical modeling and context-aware predictive analytics. By integrating domain-specific contextual features, we demonstrate a significant improvement in predictive accuracy.")

# Introduction
pdf.chapter_title("1. Introduction")
pdf.chapter_body("Demand forecasting is a foundational element of supply chain efficiency. While historical sales data provides a baseline, it often lacks the nuance required to navigate volatile market conditions. This paper introduces a hybrid approach that combines the Random Forest Regressor with external environment-aware weighting.")

# Methodology & Results (Add as many sections as you need)
pdf.chapter_title("2. Methodology & Results")
pdf.chapter_body("Our research utilized a dataset of 76,000 records. We achieved a baseline MAPE of 43.51 percent. By implementing our hybrid framework, which incorporates weather and epidemic status as predictive weights, we reduced the MAPE to 39.37 percent.")

# Appendices (The Code)
pdf.chapter_title("Appendix: Hybrid Feature Engineering")
pdf.chapter_body("weather_map = {'Sunny': 1.2, 'Cloudy': 1.0, 'Rainy': 0.9, 'Snowy': 0.8}\nepidemic_map = {0: 1.0, 1: 0.6}")

pdf.output('Research_Paper.pdf')
print("PDF successfully generated as 'Research_Paper.pdf'")