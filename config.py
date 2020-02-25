import sys

from aqt import mw
from aqt.utils import showWarning

userOption = None
addonName = "Adding card: empty first field/list of tags"
version = 2


def getUserOption(key=None, default=None):
    global userOption
    if userOption is None:
        userOption = mw.addonManager.getConfig(__name__)
    if key is None:
        return userOption
    if key in userOption:
        return userOption[key]
    else:
        return default


lastVersion = getUserOption(version)
if lastVersion < version:
    # update code
    pass
if lastVersion > version:
    showWarning(f"Please update add-on {addonName}. It seems that your configuration file is made for a more recent version of the add-on.")


def writeConfig():
    mw.addonManager.writeConfig(__name__, userOption)


def update(_):
    global userOption, fromName
    userOption = None
    fromName = None


mw.addonManager.setConfigUpdatedAction(__name__, update)

fromName = None


def getFromName(name):
    global fromName
    if fromName is None:
        fromName = dict()
        for dic in getUserOption("columns"):
            fromName[dic["name"]] = dic
    return fromName.get(name)
