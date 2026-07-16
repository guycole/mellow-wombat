import unittest

import json_helper


def _catalog_with_collectors(*collectors):
    return {
        "creationEpochTime": 1,
        "creationIso8601Time": "2026-01-01T00:00:00+00:00",
        "project": "wombat-catalog",
        "schemaVersion": 1,
        "crate": [
            {
                "crateName": "wombat01",
                "geoLoc": {
                    "siteName": "site1",
                    "altitude": 1.0,
                    "latitude": 1.0,
                    "longitude": 1.0,
                },
                "sbc": list(collectors),
            },
            {
                "crateName": "wombat02",
                "geoLoc": {
                    "siteName": "site2",
                    "altitude": 2.0,
                    "latitude": 2.0,
                    "longitude": 2.0,
                },
                "sbc": [
                    {
                        "eth0": "10.168.2.1",
                        "gps": "None",
                        "hostName": "n2a",
                        "role": "gateway",
                        "storage": "4 TB Passport",
                        "type": "odroid n2",
                        "wifi": "AC600",
                    }
                ],
            },
        ],
    }


class JsonHelperValidationTest(unittest.TestCase):

    def test_receiver_task_only_needs_to_be_in_host_tasks(self):
        catalog = _catalog_with_collectors(
            {
                "eth0": "10.168.1.109",
                "gps": "None",
                "hostName": "pi3c",
                "role": "collector",
                "storage": "16 GB microSD",
                "tasks": ["heeler-v2", "slug-v1"],
                "type": "rpi3",
                "wifi": "None",
                "receiver": {
                    "id": 1,
                    "task": "heeler-v2",
                    "type": "ac-1300",
                    "antenna": "whip",
                },
            },
            {
                "eth0": "10.168.1.110",
                "gps": "None",
                "hostName": "pi4a",
                "role": "collector",
                "storage": "32 GB microSD",
                "tasks": ["capybara-v1", "hyena-v2-dump978", "slug-v1"],
                "type": "rpi4",
                "wifi": "None",
                "receiver": {
                    "id": 2,
                    "task": "slug-v1",
                    "type": "rtl-sdr-v3",
                    "antenna": "multicoupler",
                },
            },
        )

        errors = json_helper.JsonHelper()._validate_task_assignments(catalog)

        self.assertEqual(errors, [])

    def test_collector_eth0_last_octet_must_be_globally_unique(self):
        catalog = _catalog_with_collectors(
            {
                "eth0": "10.168.1.109",
                "gps": "None",
                "hostName": "pi3c",
                "role": "collector",
                "storage": "16 GB microSD",
                "tasks": ["heeler-v2"],
                "type": "rpi3",
                "wifi": "None",
                "receiver": {
                    "id": 1,
                    "task": "heeler-v2",
                    "type": "ac-1300",
                    "antenna": "whip",
                },
            },
            {
                "eth0": "10.168.9.109",
                "gps": "None",
                "hostName": "pi4a",
                "role": "collector",
                "storage": "32 GB microSD",
                "tasks": ["slug-v1"],
                "type": "rpi4",
                "wifi": "None",
                "receiver": {
                    "id": 2,
                    "task": "slug-v1",
                    "type": "rtl-sdr-v3",
                    "antenna": "multicoupler",
                },
            },
        )

        errors = json_helper.JsonHelper()._validate_task_assignments(catalog)

        self.assertEqual(len(errors), 1)
        self.assertIn("collector eth0 last octet '109' is duplicated", errors[0])


if __name__ == "__main__":
    unittest.main()