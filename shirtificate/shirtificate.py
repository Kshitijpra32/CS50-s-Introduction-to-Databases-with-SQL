from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

    # Shirt Image
    pdf.image("shirtificate.png", x=15, y=60, w=180)

    # Name on the shirt
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(255, 255, 255)

    # Move text to appropriate Y position (center of the shirt)
    pdf.set_y(125)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # Output
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
