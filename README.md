# svg_style_attribute
## Usage
```
python run.py .\test.svg .\test_style.svg
```
Converts test.svg which has styles defined in defs/style and uses CSS class selectors into test_style.svg which has the CSS styles in a style attribute.
## Why?
Adobe Illustrator exports SVGs with defs/style XML nodes. Inkscape can read SVGs with defs/style XML nodes but the Inkscape exporter to HTML5 only works with nodes with style attribute. This tool converts SVGs to in-line style attribute.
## Example
Original input:
```
  <defs
     id="defs835">
    <style
       id="style833">.cls-1{fill:#df8679;}</style>
  </defs>
  <path
     class="cls-1"
     d="M76.1,40.73H70.8a4,4,0,0,1-4-4h0a4,4,0,0,1,4-4h5.3a4,4,0,0,1,4,4h0A4,4,0,0,1,76.1,40.73Z"
     id="path837" />
```
Modified output:
```
  <ns0:defs id="defs835">
    <ns0:style id="style833">.cls-1{fill:#df8679;}.cls-2{fill:#dfd2cd;}.cls-3{fill:#616d3e;}.cls-4{fill:#7c8c57;}.cls-5{fill:#1d1d1b;}.cls-6{fill:#fcaa97;}.cls-7{fill:#5d3523;}.cls-8{fill:#fde8df;}.cls-9{fill:#e36a11;}.cls-10{fill:#ba5517;}.cls-11{fill:#974915;}.cls-12{fill:#bb5b17;}.cls-13{fill:none;stroke:#ffeee7;stroke-miterlimit:10;stroke-width:0.25px;}.cls-14{fill:#dd3615;}.cls-15{fill:#b62a13;}.cls-16{fill:#8ecece;isolation:isolate;opacity:0.45;}</ns0:style>
  </ns0:defs>
  <ns0:path class="cls-1" d="M76.1,40.73H70.8a4,4,0,0,1-4-4h0a4,4,0,0,1,4-4h5.3a4,4,0,0,1,4,4h0A4,4,0,0,1,76.1,40.73Z" id="path837" style="fill:#df8679;" />
```
## Limitations
The tool is a very simple tool which only handles class style CSS selectors. Any complicated selectors in defs/style will not work. It also only appends the styles to whatever is in the style attribute or adds a new style attribute. It doesn't check for duplicate styles or overriding styles. Finally, the tool doesn't handle the default SVG namespace correctly and instead renames the SVG namespace to be ns0.
