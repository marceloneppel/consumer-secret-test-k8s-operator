#!/usr/bin/env python3
# Copyright 2024 Ubuntu
# See LICENSE file for licensing details.

"""Charm the application."""

import logging
from typing import Optional

import ops

logger = logging.getLogger(__name__)


class ConsumerSecretTestK8SOperatorCharm(ops.CharmBase):
    """Charm the application."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.share_secret_action, self._on_share_secret_action)
        self.framework.observe(self.on.start, self._on_start)

    def _on_share_secret_action(self, event: ops.ActionEvent):
        """Handle share-secret action."""
        relation = self._relation()
        if not relation:
            event.fail("Missing relation")
            return

        secret = self.app.add_secret({"key": "value"}, label=relation.name)
        secret.grant(relation)
        event.set_results({"shared-secret": secret.id})

    def _on_start(self, _):
        """Handle start event."""
        self.unit.status = ops.ActiveStatus()

    def _relation(self) -> Optional[ops.Relation]:
        for relation_name in ["consumer", "provider"]:
            if self.framework.model.get_relation(relation_name):
                return self.framework.model.get_relation(relation_name)


if __name__ == "__main__":  # pragma: nocover
    ops.main(ConsumerSecretTestK8SOperatorCharm)  # type: ignore
