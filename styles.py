from qdarkstyle import load_stylesheet_pyqt6, load_stylesheet_pyqt5

def setupTheme():
    app.setStyle('Fusion')
    app.setStyleSheet(load_stylesheet_pyqt6() if hasattr(app, 'Qt') else load_stylesheet_pyqt5())