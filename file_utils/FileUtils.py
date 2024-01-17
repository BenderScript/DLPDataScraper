import os
import platform

from fpdf import FPDF


class FileUtils:

    def __init__(self, font_path=None):
        if font_path is None:
            self.font_path = self.get_font_path()

    def get_font_path(self):
        """
        Get the font path depending on the operating system.
        """
        if platform.system() == 'Darwin':  # macOS
            return "/Library/Fonts/Arial Unicode.ttf"
        elif platform.system() == 'Windows':
            return "C:/Windows/Fonts/arialuni.ttf"  # Adjust if necessary
        elif platform.system() == 'Linux':
            return "/usr/share/fonts/truetype/freefont/FreeSans.ttf"  # Adjust if necessary
        else:
            raise OSError("Unsupported operating system")

    def convert_single_txt_to_pdf(self, filename: str, text_data, pdf_data):
        """
        Convert a single text file in the input directory to a PDF file in the output directory.
        """
        if not os.path.exists(pdf_data):
            os.makedirs(pdf_data)

        if filename.endswith('.txt'):
            input_file_path = os.path.join(text_data, filename)
            output_file_path = os.path.join(pdf_data, filename.replace('.txt', '.pdf'))

            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('CustomFont', '', self.font_path, uni=True)
            pdf.set_font('CustomFont', '', 12)

            with open(input_file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    cleaned_line = line.replace('\r', '').strip()
                    pdf.cell(200, 10, txt=cleaned_line, ln=True)

            pdf.output(output_file_path)

    def convert_txt_to_pdf(self, text_data, pdf_data):
        """
        Convert all text text_data in the input directory to PDF text_data in the output directory.
        """
        if not os.path.exists(pdf_data):
            os.makedirs(pdf_data)

        for filename in os.listdir(text_data):
            if filename.endswith('.txt'):
                input_file_path = os.path.join(text_data, filename)
                output_file_path = os.path.join(pdf_data, filename.replace('.txt', '.pdf'))

                pdf = FPDF()
                pdf.add_page()
                pdf.add_font('CustomFont', '', self.font_path, uni=True)
                pdf.set_font('CustomFont', '', 12)

                with open(input_file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        cleaned_line = line.replace('\r', '').strip()  # Strips carriage return and trailing spaces
                        pdf.cell(200, 10, txt=cleaned_line, ln=True)

                pdf.output(output_file_path)

        print("Conversion completed.")
