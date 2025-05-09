from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from ..widgets import ClickableWidget
from ..utils import get_absolute_path, add_class
from session import session

class CatalogItemWidget(ClickableWidget):
    def __init__(self, item_data, parent=None):
        super().__init__(parent)

        self._item_data = item_data
        self._cart_btn = QPushButton()

        self._init_ui()
        self._connect_signals()

    def _init_ui(self):
        self.setFixedWidth(190)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        image_container = QLabel()
        pixmap = QPixmap(
            get_absolute_path(__file__, "../images/item_placeholder.png")
        )
        image_container.setPixmap(
            pixmap.scaled(190, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        )

        title = QLabel()
        title.setText("Название товара")
        add_class(title, "catalog-item-title")
        title.setWordWrap(True)

        category = QLabel()
        category.setText("Название категории")
        add_class(category, "catalog-item-text") 
        
        colors = QLabel()
        colors.setText("1 цвет")
        add_class(colors, "catalog-item-text") 

        price = QLabel()
        price.setText("2 000 ₽")
        add_class(price, "catalog-item-price")

        layout.addWidget(image_container)
        layout.addSpacing(15)
        layout.addWidget(title)
        layout.addSpacing(2)
        layout.addWidget(category)
        layout.addWidget(colors)
        layout.addSpacing(9)
        layout.addWidget(price)

        self.setLayout(layout)

    def _connect_signals(self):
        self.clicked.connect(self._open_item_page)

    def _open_item_page(self):
        from ..windows import ItemWindow
        window = ItemWindow()

        window.show()
