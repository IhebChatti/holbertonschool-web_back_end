#!/usr/bin/env python3
"""[test_client]
"""
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """[TestGithubOrgClient]
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """[test_org]
        """
        client = GithubOrgClient(org_name)
        response = client.org
        self.assertEqual(response, mock_get.return_value)
        mock_get.assert_called_once
