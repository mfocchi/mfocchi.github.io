import sys, re, openpyxl

XLSX, OUT = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(XLSX, data_only=True)

MONTHS = {"gen": "Jan", "feb": "Feb", "mar": "Mar", "apr": "Apr", "mag": "May", "giu": "Jun",
          "lug": "Jul", "ago": "Aug", "set": "Sep", "sett": "Sep", "ott": "Oct", "nov": "Nov", "dic": "Dec"}


def s(v):
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    t = re.sub(r"\s+", " ", str(v)).strip()
    t = t.rstrip(":").strip()
    return t.replace("|", "/")


def when(y, m):
    y, m = s(y), s(m).lower()
    m = MONTHS.get(m, m.capitalize())
    return f"{m} {y}".strip()


COUNTRY = {"Marocco": "Morocco", "Turchia": "Turkey", "Thailandia": "Thailand", "Sudafrica": "South Africa"}


def elev(q):
    q = s(q).replace(" m", "").replace(".", "")
    return f" ({q} m)" if q.isdigit() and int(q) > 0 else ""


def length(d):
    d = s(d)
    return f"{d} m" if d.isdigit() else d


def grade(*parts):
    out = []
    for p in parts:
        p = s(p).rstrip("/ ").strip()
        if p and p not in out:
            out.append(p)
    return " · ".join(out)


def nicecase(t):
    return t.title() if t.isupper() and len(t) > 3 else t


def rows(sheet, start=3):
    ws = wb[sheet]
    for r in ws.iter_rows(values_only=True, max_col=14):
        r = list(r) + [None] * 14
        if isinstance(r[0], (int, float)) and s(r[6]) and s(r[4]):
            yield r


def table(header, data):
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    lines += ["| " + " | ".join(row) + " |" for row in data]
    return "\n".join(lines)


NOTES = {"winter ascent": "winter ascent", "first ascent": "**first ascent**",
         "grado norvegese": "", "Scialpinismo": "on skis"}


def note(n):
    n = s(n)
    if n.startswith("Discesa classica"):
        return "descent on foot"
    if n.startswith("Maltempo"):
        return "storm, bivouac below the summit"
    return NOTES.get(n, n)


def route(name, n):
    name = nicecase(s(name))
    n = note(n)
    return f"{name} — {n}" if n else name


def partners(p):
    p = s(p)
    if p.upper() == "FREE-SOLO":
        return "*free solo*"
    return re.sub(r"\s*,\s*", ", ", p)


tabs = []

# --- Rock alpinism
seen, data = set(), []
for r in rows("ALPINISMO ROCCIA"):
    key = (s(r[1]), s(r[6]).lower())
    if key in seen:  # duplicate entry (Tempest): keep the Mont Blanc one
        data = [d for d in data if not (d[0].endswith(key[0]) and d[3].lower() == key[1])]
    seen.add(key)
    g = s(r[9])
    if s(r[13]) == "grado norvegese" and g.startswith("N"):
        g = g[1:] + " (NOR)"
    data.append([when(r[1], r[2]), s(r[3]), nicecase(s(r[4])) + elev(r[5]), route(r[6], r[13]),
                 length(r[7]), grade(r[8], g), partners(r[12])])
tabs.append(("rock", "Rock alpinism", len(data),
             "Multi-pitch rock routes in the mountains. Grades: overall (French alpine scale) · hardest pitch "
             "(UIAA or French). (NOR) = Norwegian grade.",
             table(["Date", "Area", "Peak", "Route", "Length", "Grade", "Partners"], data)))

# --- Ice & mixed alpinism
data = []
for r in rows("ALPINISMO GHIACCIO-MISTO"):
    data.append([when(r[1], r[2]), s(r[3]), s(r[4]) + elev(r[5]), route(r[6], r[12]),
                 length(r[7]), grade(r[8], r[9]), partners(r[11])])
tabs.append(("ice", "Ice & mixed", len(data),
             "Goulottes, north faces, mixed routes and high-altitude summits.",
             table(["Date", "Area", "Peak", "Route", "Length", "Grade", "Partners"], data)))

# --- Ice falls
data = []
for r in rows("CASCATE"):
    data.append([when(r[1], r[2]), s(r[3]), s(r[4]), route(r[6], r[12]),
                 length(r[7]), grade(r[8], r[9]), partners(r[11])])
tabs.append(("falls", "Ice falls", len(data),
             "Frozen waterfalls. Grade: commitment (I–V) · technical (WI).",
             table(["Date", "Area", "Location", "Route", "Length", "Grade", "Partners"], data)))

# --- Ski mountaineering
data = []
for r in rows("SCIALP"):
    data.append([when(r[1], r[2]), s(r[3]), s(r[4]) + elev(r[5]), s(r[6]),
                 length(r[7]), s(r[8]), partners(r[9])])
tabs.append(("ski", "Ski mountaineering", len(data),
             "Ski tours and ski ascents. Grade on the Blachère scale (MS, BS, OS; A = alpine terrain).",
             table(["Date", "Area", "Summit", "Route / start", "Vertical gain", "Grade", "Partners"], data)))

# --- Extra-European
data = []
for r in rows("EXTRAEUROPEA"):
    data.append([when(r[1], r[2]), COUNTRY.get(s(r[3]), s(r[3])), s(r[4]).rstrip(",") + elev(r[5]), route(r[6], r[12]),
                 length(r[7]), grade(r[8], r[9]), partners(r[11])])
tabs.append(("extra", "Extra-European", len(data),
             "Expeditions and climbing trips outside Europe, including first ascents in the Karakorum "
             "(Translimes 2017) and the Moroccan Anti-Atlas (2018).",
             table(["Date", "Region", "Peak / wall", "Route", "Length", "Grade", "Partners"], data)))

# --- Multi-pitch sport
data = []
for r in rows("ROCCIA - VIE SPORTIVE"):
    data.append([when(r[1], r[2]), s(r[3]), s(r[4]), nicecase(s(r[6])),
                 length(r[7]), s(r[9]), partners(r[11])])
tabs.append(("sport", "Multi-pitch sport", len(data),
             "Bolted and semi-bolted multi-pitch routes. Grade: hardest pitch (mandatory grade in brackets).",
             table(["Date", "Area", "Crag / wall", "Route", "Length", "Grade", "Partners"], data)))

# --- Talks & press
ws = wb["DIVULGATIVA-CULTURALE"]
lines = []
for raw in str(ws["B4"].value).splitlines():
    t = re.sub(r"\s+", " ", raw).strip()
    if not t or t.startswith("ARTICOLI"):
        continue
    if t == "CONFERENZE E SERATE":
        lines += ["", "### Talks and presentations", ""]
        continue
    if t.startswith("- "):
        m = re.match(r"- (.*?) – (https?://\S+)$", t)
        lines.append(f"- [{m.group(1)}]({m.group(2)})" if m else t)
    else:
        lines += ["", f"### {t}", ""]
press = "\n".join(lines).strip()
tabs.append(("press", "Talks & press", None,
             "Articles about the expeditions and public talks.", press))

# --- Assemble page
css = """<style>
.climb-tabbar { display: flex; flex-wrap: wrap; gap: .4em; margin: 1.5em 0 1em; padding-bottom: .8em;
  border-bottom: 1px solid rgba(128,128,128,.35); }
.climb-tabbar button { font: inherit; font-size: .8em; color: inherit; background: transparent; cursor: pointer;
  padding: .45em .9em; border: 1px solid rgba(128,128,128,.45); border-radius: 999px; opacity: .8; }
.climb-tabbar button:hover { opacity: 1; }
.climb-tabbar button[aria-selected="true"] { opacity: 1; font-weight: bold; background: rgba(128,128,128,.25);
  border-color: currentColor; }
.climb-tabbar .n { opacity: .65; margin-left: .3em; font-weight: normal; }
.climb-panel table { font-size: .72em; }
.climb-panel td:first-child { white-space: nowrap; }
.climb-js .climb-panel { display: none; }
.climb-js .climb-panel.active { display: block; }
.climb-js .climb-panel > h2:first-child { display: none; }
</style>"""

js = """<script>
(function () {
  var bar = document.getElementById('climb-tabbar');
  var panels = document.querySelectorAll('.climb-panel');
  if (!bar || !panels.length) { return; }
  document.documentElement.classList.add('climb-js');
  bar.hidden = false;
  function show(key, push) {
    var found = false;
    for (var i = 0; i < panels.length; i++) {
      var on = panels[i].id === 'climb-' + key;
      panels[i].classList.toggle('active', on);
      found = found || on;
    }
    if (!found) { return show(panels[0].id.replace('climb-', ''), false); }
    var btns = bar.querySelectorAll('button');
    for (var j = 0; j < btns.length; j++) {
      btns[j].setAttribute('aria-selected', btns[j].getAttribute('data-tab') === key ? 'true' : 'false');
    }
    if (push && history.replaceState) { history.replaceState(null, '', '#' + key); }
  }
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (b) { show(b.getAttribute('data-tab'), true); }
  });
  show(location.hash.replace('#', '') || panels[0].id.replace('climb-', ''), false);
})();
</script>"""

out = ["---", 'title: "Climbing"', "permalink: /Climbing/", "header:", "", "---", "",
       "<!-- Tables generated from cv_alpinistico_Michele_Focchi_ordered.xlsx -->", "",
       "Alpinism for me is going out from my comfort zone to approximate my real self. It is getting to know my "
       "limits and accept them. It is experiencing deep emotions that make me feel alive as anything else. It is "
       "pleasure in the movement and contemplation of nature. It makes you enter in a kind of meditative state too, "
       "because you are 100% in the \"here and now\". In a nutshell, for me it is the closest that you can have to "
       "a spiritual experience.", "",
       "Below is my climbing record, grouped by discipline.", "",
       css, ""]
btns = []
for key, label, n, *_r in tabs:
    count = f'<span class="n">{n}</span>' if n else ""
    btns.append(f'<button type="button" role="tab" data-tab="{key}" aria-selected="false">{label}{count}</button>')
out.append('<div class="climb-tabbar" id="climb-tabbar" role="tablist" hidden>' + "".join(btns) + "</div>")
for key, label, n, lead, body in tabs:
    out += ["", f'<div class="climb-panel" id="climb-{key}" markdown="1">', "", f"## {label}", "",
            f"*{lead}*", "", body, "", "</div>"]
out += ["", js, ""]
open(OUT, "w").write("\n".join(out))
print({t[1]: t[2] for t in tabs})
