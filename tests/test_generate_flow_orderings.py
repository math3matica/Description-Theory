import unittest

from generate_flow_orderings import generate_description_set


class GenerateDescriptionSetTests(unittest.TestCase):
    def test_1_to_1_contains_both_orientations(self):
        self.assertEqual(
            generate_description_set(1),
            ["(a) > (b)", "(b) > (a)"],
        )

    def test_1_to_2_uses_nested_background_and_all_associated_orders(self):
        self.assertEqual(
            generate_description_set(2),
            [
                "(a) > ((b) > (c))",
                "(a) > ((c) > (b))",
                "(b) > ((a) > (c))",
                "(b) > ((c) > (a))",
                "(c) > ((a) > (b))",
                "(c) > ((b) > (a))",
            ],
        )

    def test_1_to_4_sets_have_expected_complete_permutation_counts(self):
        expected_counts = {1: 2, 2: 6, 3: 24, 4: 120}
        for n, expected in expected_counts.items():
            with self.subTest(n=n):
                descriptions = generate_description_set(n)
                self.assertEqual(len(descriptions), expected)
                self.assertEqual(len(set(descriptions)), expected)

    def test_n_must_be_at_least_one(self):
        for n in (0, -1):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    generate_description_set(n)


if __name__ == "__main__":
    unittest.main()
