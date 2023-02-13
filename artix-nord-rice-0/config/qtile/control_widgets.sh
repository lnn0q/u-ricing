#!/usr/bin/bash
widget=$(eww "windows")

case "$widget" in
  '*dashboard') eww close dashboard
  ;;
  'dashboard') eww open dashboard
  ;;
esac
