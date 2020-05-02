from aqt.addcards import AddCards
from aqt.utils import askUser, tooltip, showWarning
from anki.lang import _
from aqt import gui_hooks

def accept_empty_first_field(problem, note):
    if problem == _("The first field is empty."):
        # recursive call, so that all hooks are run again, removing this problem.
        return gui_hooks.add_cards_will_add_note(None, note)
    else:
        return problem

gui_hooks.add_cards_will_add_note.append(accept_empty_first_field)
