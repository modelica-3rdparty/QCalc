#!/usr/bin/env python
# Clean up the HTML help files by making custom replacements.
#
# The first argument is the directory, which defaults to the present directory.
#
# Created by Kevin Davies, 5/30/2012

import re, glob, sys, os, datetime

## Settings

# Replacement pairs
now = datetime.datetime.now()
rpls = [
    # Update the image links.
    ('img src=".*?([^/]+\.png)', r'img src="images/\1'),
    ('img src=".*?([^/]+\.svg)', r'img src="images/\1'),
    ('img src=".*?([^/]+\.gif)', r'img src="images/\1'),
    ('img src=".*?([^/]+\.pdf)', r'img src="images/\1'),
    ('img src=".*?([^/]+\.ico)', r'img src="images/\1'),
    # QCalc.html will be index.html.
    ('QCalc\.html', 'index.html'),
    # Change the title of the main page.
    ('<title>QCalc</title>', '<title>QCalc - Modelica units based on quantity calculus</title>'),
    # Add meta title and keywords.
    ('<meta name="HTML-Generator" content="Dymola">', r"""<meta name="title" content="Modelica units based on quantity calculus">
<meta name="keywords" content="quantities unit conversion natural SI CGS Planck Hartree">
<meta name="date" content="%d-%d-%d">""" % (now.year, now.month, now.day)),
    # Change the meta description of the main page.
    ('<meta name="description" content="Modelica units based on quantity calculus">', '<meta name="description" content="Free, open-source Modelica library of units based on quantity calculus">'),
    # Add Google custom search and the download link.
    ("""(Icons</a></li> *
 *</ul> *
)( *</div>)""", r"""\1
  <h3>Search</h3>
    <script>
      (function() {
      var cx = '001356158537703621276:db7jag_aoya';
      var gcse = document.createElement('script');
      gcse.type = 'text/javascript';
      gcse.async = true;
      gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
          '//www.google.com/cse/cse.js?cx=' + cx;
      var s = document.getElementsByTagName('script')[0];
      s.parentNode.insertBefore(gcse, s);
      })();
    </script>
    <gcse:search></gcse:search>

  <h3>Download</h3>
    <ul>
      <li><span itemprop="downloadUrl">Latest: <a href="https://github.com/kdavies4/QCalc/archive/vx.x.x.zip">vx.x.x</a></span></li>
    </ul>
\2"""),
    # Add Microdata markup.
    ('\n<div class="sidebar">', """\n<span itemscope itemtype="http://schema.org/SoftwareApplication">
<div class="sidebar">"""),
    ('\n</body>\n?</html>', '\n</span></body></html>'),
    ('<p class="sidebar-title">QCalc</p>', '<p itemprop="name" class="sidebar-title">QCalc</p>'),
    ('img src="images/icon.gif" class="logo"', 'img itemprop="image" src="images/icon.gif" class="logo"'),
    ('<img src="images/QCalc.Assemblies.Cells.CellD.png" width="600"/>', '<img id="_screenshot8" itemprop="screenshot" src="images/QCalc.Assemblies.Cells.CellD.png" width="600"/>'),
    ("Kevin Davies, Georgia Tech Research Corporation", """<span id="_author5" itemprop="author" itemscope itemtype="http://schema.org/Person">
<span itemprop="name">Kevin Davies</span></span>,
<span id="_publisher7" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
<span itemprop="name">Georgia Tech Research Corporation</span></span>"""),
    # Move the style sheet.
    ('"\.\./Resources/Documentation/ModelicaDoc\.css"', '"stylesheets/ModelicaDoc.css"'),
    # Add the Google Analytics script.
    ('(<link rel="shortcut icon" href=".*\.ico">\n)(</head>)', r"""\1<script type="text/javascript" src="javascripts/analytics.js"></script>
\2"""),
    # Move the icon.
    ('"\.\./Resources/Documentation/favicon\.ico"', '"images/favicon.ico"'),
    # Remove the self-reference.
    ("""Updates to this package may be available at.*
 *<a href="http://kdavies4\.github\.com/QCalc/">.*
 *Development is being carried out at""", 'The development site is'),
    ]

# Directory specification
if (len(sys.argv) > 1):
    directory = sys.argv[1]
else:
    directory = '.'

## Procedure
# Compile the regular expressions.
for i, rpl in enumerate(rpls):
    rpls[i] = (re.compile(rpl[0]), rpl[1])

# Replace strings.
for fname in glob.glob(os.path.join(directory, '*.html')):
    # Read the source file.
    print "Processing " + fname + "..."
    src = open(fname, 'r')
    text = src.read()
    src.close()

    # Make the replacements.
    for rpl in rpls:
        text = rpl[0].sub(rpl[1], text)

    # Re-write the file.
    src = open(fname, 'w')
    src.write(text)
    src.close()
