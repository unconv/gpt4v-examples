import subprocess
import os

def take(url, filename="screenshot.jpg", full_page=False ):
    subprocess.run(
        ["node", "screenshot.js", url, str(full_page)],
        capture_output=True
    )

    if filename != "screenshot.jpg":
        os.rename("screenshot.jpg", filename)

    return filename
