#!/bin/bash

# Auto-generate GitHub-style PDF (no manual printing needed!)
# Generic script that works in any lab folder

echo "========================================="
echo "  GitHub-Style Auto PDF Generator"
echo "========================================="
echo ""

# Auto-detect folder name for output filename
FOLDER_NAME=$(basename "$(pwd)")
OUTPUT_NAME="${FOLDER_NAME}_TASKS"
PDF_FILE="${OUTPUT_NAME}.pdf"
HTML_FILE="${OUTPUT_NAME}.html"
TEMP_HTML="${OUTPUT_NAME}_temp.html"
CLEAN_MD="TASKS_clean.md"

echo "Working in folder: $FOLDER_NAME"
echo "Output PDF will be: $PDF_FILE"
echo ""

# Auto cleanup - remove old generated files
echo "Cleaning up old files..."
rm -f "$PDF_FILE" "$HTML_FILE" "$TEMP_HTML" "$CLEAN_MD"
echo ""

# Check if TASKS.md exists
if [ ! -f "TASKS.md" ]; then
    echo "Error: TASKS.md not found!"
    exit 1
fi

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: Pandoc is not installed!"
    echo "Please run: sudo apt install pandoc"
    exit 1
fi

echo "Step 1: Preparing markdown (removing language labels from code blocks)..."

# Create a temporary markdown file with language identifiers removed
sed -E 's/```[a-z]+$/```/g' TASKS.md > "$CLEAN_MD"

echo "Step 2: Creating GitHub-style HTML..."

# Get a nice title from folder name (convert underscores to spaces, capitalize)
TITLE=$(echo "$FOLDER_NAME" | sed 's/_/ /g' | sed 's/\b\(.\)/\u\1/g')

# Create HTML with embedded GitHub styling
cat > "$TEMP_HTML" << HTMLHEADER
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>${TITLE}</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            max-width: 980px;
            margin: 0 auto;
            padding: 45px;
            color: #24292e;
            background-color: #ffffff;
        }
        h1 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; font-size: 2em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
        h2 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; font-size: 1.5em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
        h3 { font-size: 1.25em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
        h4 { font-size: 1em; margin-top: 24px; margin-bottom: 16px; font-weight: 600; }
        p { margin-top: 0; margin-bottom: 16px; }
        ul, ol { padding-left: 2em; margin-top: 0; margin-bottom: 16px; }
        li { margin-bottom: 0.25em; }
        li > p { margin-top: 16px; }
        li + li { margin-top: 0.25em; }
        ul ul, ol ol, ul ol, ol ul { margin-top: 0; margin-bottom: 0; }
        code { 
            background-color: rgba(175,184,193,0.2);
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            border-radius: 3px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
        }
        pre {
            background-color: #f6f8fa;
            border-radius: 3px;
            font-size: 85%;
            line-height: 1.45;
            overflow: auto;
            padding: 16px;
            margin-top: 0;
            margin-bottom: 16px;
            white-space: pre;
        }
        pre code {
            background-color: transparent;
            border: 0;
            display: block;
            line-height: 1.45;
            margin: 0;
            overflow: visible;
            padding: 0;
            white-space: pre;
            word-wrap: normal;
        }
        .sourceCode pre, .sourceCode code, pre.sourceCode code {
            display: block !important;
            white-space: pre !important;
        }
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #e1e4e8;
            border: 0;
        }
        blockquote {
            margin: 0;
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
        }
        strong { font-weight: 600; }
        table {
            border-spacing: 0;
            border-collapse: collapse;
            margin-top: 0;
            margin-bottom: 16px;
        }
        table th, table td {
            padding: 6px 13px;
            border: 1px solid #dfe2e5;
        }
        table tr {
            background-color: #fff;
            border-top: 1px solid #c6cbd1;
        }
        table tr:nth-child(2n) {
            background-color: #f6f8fa;
        }
    </style>
</head>
<body>
HTMLHEADER

# Convert cleaned markdown to HTML and append (no syntax highlighting = one unified code block)
pandoc "$CLEAN_MD" -t html --no-highlight >> "$TEMP_HTML"

# Close HTML
echo '</body></html>' >> "$TEMP_HTML"

echo "Step 3: Converting HTML to PDF..."
echo ""

# Try different PDF conversion tools (in order of preference)
PDF_CREATED=false

# Method 1: Try wkhtmltopdf (best quality)
if command -v wkhtmltopdf &> /dev/null; then
    echo "Using wkhtmltopdf..."
    wkhtmltopdf --enable-local-file-access --print-media-type "$TEMP_HTML" "$PDF_FILE" 2>/dev/null
    if [ -f "$PDF_FILE" ]; then
        PDF_CREATED=true
    fi
fi

# Method 2: Try chromium/chrome headless
if [ "$PDF_CREATED" = false ]; then
    for browser in chromium-browser chromium google-chrome chrome; do
        if command -v $browser &> /dev/null; then
            echo "Using $browser headless mode..."
            $browser --headless --disable-gpu --print-to-pdf="$PDF_FILE" --no-pdf-header-footer "$TEMP_HTML" 2>/dev/null
            if [ -f "$PDF_FILE" ]; then
                PDF_CREATED=true
                break
            fi
        fi
    done
fi

# Method 3: Try weasyprint
if [ "$PDF_CREATED" = false ]; then
    if command -v weasyprint &> /dev/null; then
        echo "Using weasyprint..."
        weasyprint "$TEMP_HTML" "$PDF_FILE" 2>/dev/null
        if [ -f "$PDF_FILE" ]; then
            PDF_CREATED=true
        fi
    fi
fi

# Clean up temporary files
rm -f "$TEMP_HTML" "$CLEAN_MD"

# Check results
if [ "$PDF_CREATED" = true ]; then
    echo ""
    echo "========================================="
    echo "  Success!"
    echo "========================================="
    echo ""
    echo "GitHub-style PDF created: $PDF_FILE"
    echo ""
    ls -lh "$PDF_FILE"
    echo ""
    echo "Open it with: xdg-open \"$PDF_FILE\""
else
    echo ""
    echo "========================================="
    echo "  Installation Required"
    echo "========================================="
    echo ""
    echo "No PDF converter found. Please install one:"
    echo ""
    echo "Option 1 (Recommended):"
    echo "  sudo apt install wkhtmltopdf"
    echo ""
    echo "Option 2:"
    echo "  sudo apt install chromium-browser"
    echo ""
    echo "Option 3:"
    echo "  pip3 install weasyprint"
    echo ""
    echo "Then run this script again."
    exit 1
fi
