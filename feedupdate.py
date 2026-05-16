#!/usr/bin/env python3

python3 - <<'PY'
from pathlib import Path
import re

path = Path("index.html")
text = path.read_text(encoding="utf-8")

pattern = re.compile(
	r'(\s*<div class="stream-status" id="streamStatus">.*?</div>\s*'
	r'<div class="stream-embed" id="streamEmbed">.*?</div>\s*'
	r'(?:<div class="status-title" style="margin-top:20px;">.*?</div>\s*)?'
	r'<div class="stream-embed spacex-embed">.*?</div>\s*'
	r'(?:<div style="font-size:11px;color:#888;text-align:center;margin:-6px 0 12px 0;font-family:\'Segoe UI\',Tahoma,Geneva,Verdana,sans-serif;letter-spacing:0.5px;">.*?</div>\s*)?'
	r'<div class="status-title" style="margin-top:20px;">.*?</div>\s*'
	r'<div class="stream-embed">.*?</div>\s*'
	r'<div style="font-size:11px;color:#888;text-align:center;margin:-6px 0 12px 0;font-family:\'Segoe UI\',Tahoma,Geneva,Verdana,sans-serif;letter-spacing:0.5px;">.*?</div>\s*'
	r'<div class="weather-card">.*?</div>)',
	re.S
)

replacement = '''
			<div class="stream-status" id="streamStatus">🔴 LAUNCHED — Watch recorded-launch coverage</div>
			<div class="stream-embed" id="streamEmbed">
				<iframe src="https://www.youtube.com/embed/9J8pbaLkRuE"
					title="NASA CRS-34 Recorded Launch Coverage"
					allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
					allowfullscreen></iframe>
			</div>
			<div style="font-size:11px;color:#888;text-align:center;margin:-6px 0 12px 0;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;letter-spacing:0.5px;">NASA recorded launch coverage</div>

			<div class="status-title" style="margin-top:20px;">🛰️ ISS Live Views — NASA</div>
			<div class="stream-embed">
				<iframe src="https://www.youtube.com/embed/FuuC4dpSQ1M?vq=highres"
					title="NASA ISS Live Stream"
					allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
					allowfullscreen></iframe>
			</div>
			<div style="font-size:11px;color:#888;text-align:center;margin:-6px 0 12px 0;font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;letter-spacing:0.5px;">Live High-Definition Views from the International Space Station</div>

			<div class="weather-card">
				<div class="status-title" style="margin-bottom:8px; color:#333;">Coverage includes</div>
				✓ NASA recorded launch coverage<br>
				✓ Post-launch highlights<br>
				✓ Mission replay coverage<br>
				✓ Live ISS views
			</div>
'''

new_text, count = pattern.subn(replacement, text, count=1)

if count != 1:
	raise SystemExit("Could not find the expected live feed block to replace")
	
path.write_text(new_text, encoding="utf-8")
print("Replaced live feed section with two-stream layout in index.html")
PY