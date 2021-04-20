#!/usr/bin/env python3
"""[test_utils]
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """[TestAccessNestedMap]
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, answer):
        """[test_access_nested_map]
        """
        self.assertEqual(access_nested_map(nested_map, path), answer)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """[test_access_nested_map_exception]
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """[TestGetJson]
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """[test_get_json]
        """
        mock_get.return_value = test_payload
        response = get_json(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """[TestMemoize]
    """
    def test_memoize(self):
        """[test_memoize]
        """
        class TestClass:
            """[TestClass]
            """
            def a_method(self):
                """[a_method]
                """
                return 42

            @memoize
            def a_property(self):
                """[a_property]
                """
                return self.a_method()

        with patch.object(TestClass, "a_method") as mocked:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mocked.assert_called_once
