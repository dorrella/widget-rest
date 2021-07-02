from .Widget import get_widget
from ..Template import TemplateHandler


class WidgetEntryHandler(TemplateHandler):
    def get(self):
        tokens = self.request.path.split("/")

        # primary key  is the third token
        id = tokens[2]
        if id == "":
            msg = f"bad path {self.request.path}"
            self.err_out(404, msg)
            return

        try:
            widget = get_widget(id)
        except:
            msg = f"bad path {self.request.path}"
            self.err_out(404, msg)
            return
        data = widget.to_json()
        self.write(data)
