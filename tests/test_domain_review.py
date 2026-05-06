import unittest

from src.amber_tool_trace_stack.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(43, 37, 28, 45)
        self.assertEqual(review_score(item), 84)
        self.assertEqual(review_lane(item), "hold")


if __name__ == "__main__":
    unittest.main()
