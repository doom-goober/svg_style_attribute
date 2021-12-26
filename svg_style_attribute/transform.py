import xml.etree.ElementTree as et
import tinycss

def transform(source, destination):
  tree = et.ElementTree(file=source)
  toStyleAttribute(tree)
  f = open(destination, "wb")
  tree.write(f)

def toStyleAttribute(tree):
  namespaces = {'svg': 'http://www.w3.org/2000/svg'} # add more as needed
  #find the defs/style
  root = tree.getroot()
  classLookup = {}
  for style in root.findall("./svg:defs/svg:style", namespaces):
    parser = tinycss.make_parser('page3')
    stylesheet = parser.parse_stylesheet(style.text)
    addToClassLookup (classLookup, stylesheet)
  #find all the valid SVG nodes
  for child in root.iter():
    tag = substringAfter("}", child.tag)
    if (tag in [
                    # only attempt to group elements that the content model allows to be children of a <g>

                    # SVG 1.1 (see https://www.w3.org/TR/SVG/struct.html#GElement)
                    'animate', 'animateColor', 'animateMotion', 'animateTransform', 'set',  # animation elements
                    'desc', 'metadata', 'title',                                            # descriptive elements
                    'circle', 'ellipse', 'line', 'path', 'polygon', 'polyline', 'rect',     # shape elements
                    'defs', 'g', 'svg', 'symbol', 'use',                                    # structural elements
                    'linearGradient', 'radialGradient',                                     # gradient elements
                    'a', 'altGlyphDef', 'clipPath', 'color-profile', 'cursor', 'filter',
                    'font', 'font-face', 'foreignObject', 'image', 'marker', 'mask',
                    'pattern', 'script', 'style', 'switch', 'text', 'view',

                    # SVG 1.2 (see https://www.w3.org/TR/SVGTiny12/elementTable.html)
                    'animation', 'audio', 'discard', 'handler', 'listener',
                    'prefetch', 'solidColor', 'textArea', 'video'
    ]):
      #see if they have class attribute
      existingClass = child.get("class")
      if (existingClass != None and existingClass != ""):
        existingStyle = child.get("style")
        #add style attribute if needed
        if (existingStyle == None):
          existingStyle = ""
        classStyle = classLookup[existingClass]
        if (classStyle != None):
          #append style to style attribute
          child.set("style", existingStyle + classLookup[existingClass])

def addToClassLookup(lookup, stylesheet):
  for rule in stylesheet.rules:
    selectorText = rule.selector.as_css()
    if (not selectorText.startswith(".")):
      continue
    selectorText = selectorText[1:]
    declarations = rule.declarations
    declarationText = ""
    for declaration in declarations:
      declarationText = declarationText + declaration.name + ":" + declaration.value.as_css() + ";"
    lookup[selectorText] = declarationText

def substringAfter(search_text, text):
  return text[text.index(search_text) + len(search_text):]

def dumpMethods(object):
  object_methods = [method_name for method_name in dir(object) if callable(getattr(object, method_name))]
  for method in object_methods:
    print(method)

def dumpMembers(object):
  for text in object:
    print(text)
