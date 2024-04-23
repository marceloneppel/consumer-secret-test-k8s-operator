# Copyright 2024 Ubuntu
# See LICENSE file for licensing details.
#
# Learn more about testing at: https://juju.is/docs/sdk/testing

import unittest

import ops
import ops.testing
from charm import ConsumerSecretTestK8SOperatorCharm


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = ops.testing.Harness(ConsumerSecretTestK8SOperatorCharm)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()

    def test_pebble_ready(self):
        # Simulate the start event.
        self.harness.charm.on.start.emit()
        # Ensure we set an ActiveStatus with no message.
        self.assertEqual(self.harness.model.unit.status, ops.ActiveStatus())
