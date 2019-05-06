import unittest

from main import Solution

class Tests(unittest.TestCase):
	def test_case1(self):
		""" Check if the entire program runs as expected """
		solution = Solution()
		self.assertEqual(solution.run(True, "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.-"), "the wizard quickly jinxed the gnomes before they vaporized.")

	def test_case2(self):
		""" Check if the encrypt_text() runs as expected """
		solution = Solution()
		self.assertEqual(solution.encrypt_text("The wizard quickly jinxed the gnomes before they vaporized."), "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.- ")

	def test_case3(self):
		""" Check if the decrypt_text runs as expected """
		solution = Solution()
		self.assertEqual(solution.decrypt_text("..- .... ..-. .-.. --- .-    ...-"), "Invalid Morse Code Or Spacing")

	def test_case4(self):
		""" Check if the entire program runs as expected """
		solution = Solution()
		self.assertEqual(solution.run(True, ""), "Invalid Morse Code Or Spacing")


if __name__ == "__main__":
	unittest.main()