# RTSP Multi-Stream Viewer

This is a Python GUI application that displays multiple RTSP camera stream in a grid layout. This application is design for 24/7 running. It has some mandatory features such automatic reconnection, switching between grid and cycle mode, and keyboard controls.

## Project Overview

### System Requirements & Constraints

This application is to be run on a **Dell Wyse 3040**, a thin client with non-upgradable hardware, which imposes the following constraints:

- **Ram**: 2GB
- **Storage**: 8GB/16GB
- **Processor**:  Intel Atom x5 Z-8350
- **Processor speed**: 1.44GHz
- **Graphics**: Intel HD Graphics 400

### Project Structure

```
├── main.py                      # Entry point, initializes app
├── config.yaml                  # User-editable YAML configuration
├── app/
│   ├── __init__.py
│   ├── config_loader.py         # Config parser and validator
│   ├── error_handler.py         # Centralize error handler
│   └── app_logger.py            # Rotating log system with memory monitoring
├── core/
│   ├── __init__.py
│   ├── stream_manager.py        # Stream lifecycle, reconnection logic
│   └── mpv_player.py            # MPV wrapper, monitors stream health
├── gui/
│   ├── __init__.py
│   ├── app_window.py            # Main window, manages grid/cycle modes
│   ├── widget_stream.py         # Individual stream container (video or placeholder)
│   └── widget_placeholder.py    # "No Camera"/"Connection Lost"/"Connecting" display
└── utils/
    └── keyboard_handler.py      # Maps keys to actions
```

## Key Features

- **Automatic stream reconnection**

  - Detects when a camera stream loses connection
  - Automatically attempts reconnection at configured intervals
  - Marks stream as permanently failed after max retry attempts
  - Failed streams can be manually retried with keyboard shortcut

- **Keyboard controls**

  - Switch to grid mode
  - Switch to cycle mode
  - Next stream (cycle mode)
  - Previous stream (cycle mode)
  - Restart all streams
  - Retry all failed streams
  - Quit applications
  - Restart applications

- **Configuration**

  YAML-based, user-configurable configuration

  - Stream URLS and names
  - Viewer grid dimensions
    - Rows x columns
  - Reconnection settings
  - MPV player options
  - Logging settings
