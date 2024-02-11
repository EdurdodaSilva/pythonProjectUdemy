from unittest import TestCase
from utils.pagination import Make_pagination_range


class TestPagination(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = Make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], list(pagination))


    def test_first_range_is_Static_if_current_page_is_less_than_middle_page(self):
        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=1)['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=2)['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=3)['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=4)['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)


    def test_make_sure_middle_range_are_correct(self):
        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=10)['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=18)['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

    def test_make_pagination_range_ts_static_when_last_pages_in_next(self):

        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=19)['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = Make_pagination_range(
            page_range=list(range(1, 21)), qty_pages=4, current_page=22)['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

