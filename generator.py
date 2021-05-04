def generate(lines):
    data = []
    title = None
    for line in lines.split('\n'):
        if len(line.strip()) == 0:
            continue
        
        if title is None:
            title = line.strip()
            continue
        vals = line.split(' ')
        vardata = {'var': vals[0].strip(), 'typ': vals[1].strip()}
        data.append(vardata)

    abbr = title[0].lower()

    def cap(x):
        return x[0].upper() + x[1:]

    # interface
    outstr = "type I%s interface {\n" % title
    for datum in data:
        outstr += "    %s() %s\n" % (datum['var'].capitalize(), datum['typ'])
    outstr += "}"

    # struct
    outstr += "\n\ntype %s struct {\n" % title
    for datum in data:
        outstr += "    %s %s\n" % (datum['var'], datum['typ'])
    outstr += "}"

    # constructors
    outstr += "\n\nfunc New%s(%s) *%s {\n" % (title, ", ".join("%s %s" % (datum['var'], datum['typ']) for datum in data), title)
    outstr += "    return &%s{\n" % title
    for datum in data:
        outstr += "        %s: %s,\n" % (datum['var'], datum['var'])
    outstr += "    }\n"
    outstr += "}"

    outstr += "\n\nfunc NewEmpty%s() *%s {\n    return &%s{}\n}" % (title, title, title)

    # getters
    for datum in data:
        outstr += "\n\nfunc (%s *%s) %s() %s {\n    return %s.%s\n}" % (abbr, title, cap(datum['var']), datum['typ'], abbr, datum['var'])

    # setters
    for datum in data:
        outstr += "\n\nfunc (%s *%s) Set%s(%s %s) {\n    %s.%s = %s\n}" % (abbr, title, cap(datum['var']), datum['var'], datum['typ'], abbr, datum['var'], datum['var'])

    return outstr
