from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

replacements = [
    (
        '<iframe src="https://www.youtube.com/embed/9J8pbaLkRuE?si=6VGuGfUaB6OPNg6L" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
        '<iframe src="https://www.youtube.com/embed/9J8pbaLkRuE" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
    ),
    (
        '<div class="status-title" style="margin-top:20px;">🚀 Space Coast Live — NASASpaceflight</div>',
        '<div class="status-title" style="margin-top:20px;">🚀 Recorded Launch Replay</div>'
    ),
    (
        '<iframe src="https://www.youtube.com/embed/FuuC4dpSQ1M?vq=highres" allow="autoplay; encrypted-media" allowfullscreen></iframe>',
        '<iframe src="https://www.youtube.com/embed/Wgsg7NAxAvk" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
    ),
    (
        'title="Space Coast Live — NASASpaceflight"',
        'title="Recorded Launch Replay"'
    ),
    (
        '🚀 Space Coast Live — NASASpaceflight</div>',
        'CRS-34 recorded launch coverage</div>'
    ),
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new, 1)

old_block = '''            <div class="stream-embed spacex-embed">
                <iframe src="https://www.youtube.com/embed/9J8pbaLkRuE" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>'''

new_block = '''            <div class="status-title" style="margin-top:20px;">🛰️ ISS Live Views — NASA</div>
            <div class="stream-embed spacex-embed">
                <iframe src="https://www.youtube.com/embed/9J8pbaLkRuE" allow="autoplay; encrypted-media" allowfullscreen></iframe>
            </div>
            <div style="font-size:11px;color:#888;text-align:center;margin:-6px 0 12px 0;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;letter-spacing:0.5px;">Live High-Definition Views from the International Space Station</div>'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)

text = text.replace(
    '✓ Real-time telemetry &amp; countdown<br>\n                ✓ Pre-launch mission briefings<br>\n                ✓ Booster landing &amp; recovery<br>\n                ✓ Post-launch analysis',
    '✓ Post-launch highlights<br>\n                ✓ Recorded ascent and stage events<br>\n                ✓ Mission replay coverage<br>\n                ✓ Live ISS views'
)

text = text.replace(
    'Stream goes live at T-60 minutes (5:50 PM EDT)',
    'LAUNCHED — Watch post-launch coverage'
)

path.write_text(text, encoding="utf-8")
print("Updated index.html")