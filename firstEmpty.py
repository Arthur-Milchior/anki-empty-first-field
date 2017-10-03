# Copyright: Damien Elmes <anki@ichi2.net> and Arthur Milchior <arthur@milchior.fr>
# -*- coding: utf-8 -*-
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""Allows to add note with empty first field. 
It is add-on number 46741504

Feel free to contribute on https://github.com/Arthur-Milchior/anki-empty-first-field."""
from aqt.addcards import AddCards
from aqt.utils import tooltip, showWarning,askUser

def myAddNote(self, note):
        note.model()['did'] = self.deckChooser.selectedId()
        ret = note.dupeOrEmpty()
        if ret == 1:
            tooltip(_(
                "The first field is empty."))
        if '{{cloze:' in note.model()['tmpls'][0]['qfmt']:
            if not self.mw.col.models._availClozeOrds(
                    note.model(), note.joinedFields(), False):
                if not askUser(_("You have a cloze deletion note type "
                "but have not made any cloze deletions. Proceed?")):
                    return
        cards = self.mw.col.addNote(note)
        if not cards:
            showWarning(_("""\
The input you have provided would make an empty \
question on all cards."""), help="AddItems")
            return
        self.addHistory(note)
        self.mw.requireReset()
        return note

AddCards.addNote = myAddNote
