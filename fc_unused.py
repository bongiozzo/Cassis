def alias_used(name=""):
    doc = App.ActiveDocument
    for o in doc.Objects:
        if hasattr(o, "ExpressionEngine"):
            for exp in o.ExpressionEngine:
                if name in exp[1] or name is None:
                    return True
    return False

spreadsheet = doc.getObject("Spreadsheet")

if spreadsheet:
    aliases = {}

    for row in range(1, 101):
        for col in range(26):
            cell = f"{chr(65 + col)}{row}"
            alias = spreadsheet.getAlias(cell)
            if alias:
                aliases[alias] = spreadsheet.get(cell)

for alias in aliases.keys():
    if not alias_used(alias):
        print("Alias {} unused".format(alias))

# Alias lamp_bolt_o2_f unused
# Alias tube_d_o unused
# Alias back_t unused
# Alias lock_z_o unused
# Alias placement_replace unused
