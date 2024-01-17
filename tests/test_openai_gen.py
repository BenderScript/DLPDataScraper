import unittest

from dlp_data_gen.openai_assistant import OpenAIAssistant


class TestOpenAI(unittest.TestCase):
    dlp_gen_assistant = None

    @classmethod
    def setUpClass(cls):
        # Initialize the Assistant class
        cls.dlp_gen_assistant = OpenAIAssistant(text_data="openai/text_data", pdf_data="openai/pdf_data",
                                                dlp_categories_file="dlp/dlp_categories.md")

    @classmethod
    def tearDownClass(cls):
        cls.dlp_gen_assistant.assistant.delete_by_id(cls.dlp_gen_assistant.assistant.assistant_id)

    def test_dlp_gen(self):
        self.dlp_gen_assistant.run()


if __name__ == '__main__':
    unittest.main()
