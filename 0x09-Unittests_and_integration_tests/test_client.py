#!/usr/bin/env python3
"""[test_client]
"""
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
import unittest
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError


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

    def test_public_repos_url(self):
        """[test_public_repos_url]
        """
        with patch.object(GithubOrgClient, "org",
                          new_callable=PropertyMock,
                          return_value={
                              "repos_url": "holbertonschool"
                              }) as mock_get:
            json = {"repos_url": "holbertonschool"}
            client = GithubOrgClient(json.get("repos_url"))
            response = client._public_repos_url
            mock_get.assert_called_once
            self.assertEqual(response, mock_get.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "holbertonschool"}])
    def test_public_repos(self, mock_get):
        """[test_public_repos]
        """
        url = "https://api.github.com/"
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value=url) as mocked:
            client = GithubOrgClient("hoberton")
            response = client.public_repos()
            self.assertEqual(response, ["holbertonschool"])
            mock_get.assert_called_once
            mocked.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, repo, key, expected):
        """[test_has_license]
        """
        client = GithubOrgClient("holberton")
        response = client.has_license(repo, key)
        self.assertEqual(expected, response)



@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """[TestIntegrationGithubOrgClient]
    """
    @classmethod
    def setUpClass(cls):
        """[setUpClass]
        """
        cls.get_patcher = patch('requests.get',HTTPError)

    @classmethod
    def tearDownClass(cls):
        """[tearDownClass]
        """
        cls.get_patcher.stop()

    def test_public_repository_without_license(self):
        """[test_public_repository_without_license]
        """
        class_test = GithubOrgClient("holbertonschool")
        assert True

    def test_public_repository_with_license(self):
        """[test_public_repository_with_license]
        """
        class_test = GithubOrgClient("holbertonschool")
        assert True