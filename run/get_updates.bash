#!/usr/bin/env bash
git pull

# systemd сервистің аты store болмаса, атын өзгертіңіз

sudo systemctl daemon-reload
sudo systemctl restart store
sudo systemctl status store
