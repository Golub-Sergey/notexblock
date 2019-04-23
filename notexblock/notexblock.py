"""XBlock whih add notes in block notes."""

import pkg_resources
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


class NoteXBlock(XBlock):
    """
    Allows student make notes.
    """

    notes = String(default="", scope=Scope.user_state, help="A simple block for add notes")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        Buid XBlock view.
        """
        html = self.resource_string("static/html/notexblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/notexblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/notexblock.js"))
        frag.initialize_js('NoteXBlock')
        return frag

    @XBlock.json_handler
    def add_note(self, data, suffix=''):
        """
        Handler, which add note in block notes.
        """
        notes = data['notes']
        return {"notes": notes}

    @staticmethod
    def workbench_scenarios():
        """Display current XBlock in the workbench."""
        return [
            ("NoteXBlock",
             """<notexblock/>
             """),
            ("Multiple NoteXBlock",
             """<vertical_demo>
                <notexblock/>
                <notexblock/>
                <notexblock/>
                </vertical_demo>
             """),
        ]
