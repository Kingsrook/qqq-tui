from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from com.kingsrook.qqq.qqq_tui.ui.HomeScreen import HomeScreen


class QQQTexualClient(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [
        ("b", "push_screen('HomeScreen')", "HomeScreen"),
        ("x", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def on_mount(self) -> None:
        self.install_screen(HomeScreen(), name="HomeScreen")
